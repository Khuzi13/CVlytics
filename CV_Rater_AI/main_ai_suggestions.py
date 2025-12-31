# from google import genai

# client = genai.Client(api_key="AIzaSyAASk_BrET04eNf13LpJRBJB9sQH0Cd52o")

# def gemini_ai_suggestions(resume_text: str):
#     prompt = f"""
# You are an ATS resume expert.

# Analyze the resume and return:
# 1. Two missing important skills.
# 2. Two formatting / structure improvements.

# Resume:
# {resume_text}

# Return only 4 bullet points.
# """

#     response = client.models.generate_content(
#         model="gemini-1.5-flash",
#         contents=prompt
#     )

#     raw = response.text.strip()
#     return [line.strip("-• ") for line in raw.split("\n") if line.strip()]


from google import genai

API_KEY = "AIzaSyAH9EiNiBVC7h8IJIXpPeWqRhQsQqeYOMI"
client = genai.Client(api_key=API_KEY)

def generate_ai_suggestions(resume_text, jd_text=None):
    try:
        prompt = f"""
Analyze this resume and give 5 improvement suggestions.

Resume:
{resume_text}

Job Description:
{jd_text if jd_text else "Not Provided"}
"""

        response = client.models.generate_content(
            model="models/gemini-2.0-flash",
            contents=prompt
        )

        return [s.strip() for s in response.text.split("\n") if s.strip()]

    except Exception as e:
        return [f"AI suggestions error: {str(e)}"]

if __name__ == "__main__":
    text = "I am a data science student skilled in python and sql."
    print(generate_ai_suggestions(text))
