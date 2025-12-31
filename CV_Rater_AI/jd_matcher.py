from .pdf_pipeline import extract_text_from_pdf, clean_text
from .skill_bank import FIELD_SKILLS
from .field_detector import detect_resume_field


def job_match_score(pdf_path, job_description):
    resume = clean_text(extract_text_from_pdf(pdf_path))
    jd = clean_text(job_description)

    field = detect_resume_field(resume)
    skills = FIELD_SKILLS.get(field, [])

    jd_skills = [s for s in skills if s in jd]
    if not jd_skills:
        return 0.0

    matched = sum(1 for s in jd_skills if s in resume)
    return round((matched / len(jd_skills)) * 100, 2)


# if __name__ == "__main__":

#     pdf_path = "D:/0_Project/ats_model_2/new_train/Muhammad_Khuzaima_Siddiqui.pdf"   # 👈 YAHAN FILE NAME
#     job_description = """
#     ​I am looking for Associate Data Scientist role for i2c Inc. in our Artificial Intelligence team.​Education: Bachelors in Data Science, Computer Science, Computer Engineering, Software Engineering, IT. Experience: Fresh Candidate - 6 months.​Apply Now: fshafiq@i2cinc.com​Key Responsibilities:​Clean, explore, and analyze transaction and application data using Python and SQL.​Build and evaluate simple supervised models and baseline experiments.​Create features and run feature importance/interpretability checks.​Write clear SQL queries and Python scripts for data pipelines and ad-hoc analysis.​Produce concise reports and visualizations to communicate findings to product and engineering teams.​Collaborate with senior data scientists and engineers to deploy and monitor models.​Skills:​Proficient in Python (pandas, numpy, basic ML libraries).​Strong SQL skills for data extraction and aggregation.​Clear communicator, curious, and willing to learn.​Familiarity with scikit-learn, XGBoost, or basic ML workflows.​Exposure to Spark, Docker, or cloud environments.​Experience with Jupyter notebooks, Git, and simple data visualization (matplotlib/plotly).​#hiring
#     """

#     score = job_match_score(pdf_path, job_description)
#     print("JD Match Score:", score, "%")
