# import pandas as pd

# # CSV load karte hain
# df = pd.read_csv("1_fileee.csv")  # apna path

# # Column jisme check karna hai
# column_name = "text"  # apna column name

# # Match kar ke indices nikalna
# matched_indices = df[df['clean_text'].str.lower().str.contains("job description")].index

# # Rows actual dataframe se delete karna
# df.drop(matched_indices, inplace=True)

# # Agar chahein, cleaned data ko wapas save kar sakte hain
# df.to_csv("data.csv", index=False)

# print("Deleted rows:", len(matched_indices))
# print("Remaining rows:", len(df))
import pandas as pd
import joblib
import re
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score

from xgboost import XGBRegressor

# ---------------- NLTK SETUP ----------------
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# ---------------- TEXT CLEANING (MINIMAL) ----------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    words = [lemmatizer.lemmatize(w) for w in text.split()]
    return " ".join(words)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data.csv")  # columns: text, ats_score
df["clean_text"] = df["text"].apply(clean_text)

X = df["clean_text"]
y = df["ats_score"]


# ---------------- TRAIN / TEST SPLIT ----------------
X_train_text, X_test_text, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ---------------- TF-IDF (FIT ONLY ON TRAIN) ----------------
vectorizer = TfidfVectorizer(
    max_features=3000,
    ngram_range=(1, 2),
    min_df=3,
    max_df=0.9,
    stop_words=None   # IMPORTANT for ATS
)

X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

# ---------------- XGBOOST MODEL ----------------
xgb = XGBRegressor(
    objective="reg:squarederror",
    random_state=42,
    n_jobs=-1
)

param_grid = {
    "n_estimators": [200, 300],
    "max_depth": [4, 6],
    "learning_rate": [0.05, 0.1],
    "subsample": [0.8],
    "colsample_bytree": [0.8]
}

grid = GridSearchCV(
    xgb,
    param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1,
    verbose=1
)

grid.fit(X_train, y_train)
best_model = grid.best_estimator_

# ---------------- EVALUATION ----------------
preds = best_model.predict(X_test)

print("\nXGBoost Best Params:", grid.best_params_)
print("MAE:", mean_absolute_error(y_test, preds))
print("R2 Score:", r2_score(y_test, preds))

# ---------------- SAVE ----------------
joblib.dump(best_model, "ats_xgb_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model & Vectorizer saved successfully!")
