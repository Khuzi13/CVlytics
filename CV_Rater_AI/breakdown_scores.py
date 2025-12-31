from .skill_bank import FIELD_SKILLS
from .field_detector import detect_resume_field


SECTION_KEYWORDS = ["summary","profile","experience","education","skills","projects","certification"]
SOFT_SKILLS = ["communication","team","collaborate","lead","responsible","motivated","passionate"]

def formatting_structure_score(text):
    t = text.lower()
    hits = sum(1 for s in SECTION_KEYWORDS if s in t)
    return round((hits / len(SECTION_KEYWORDS)) * 10, 1)

def soft_skills_tone_score(text):
    t = text.lower()
    hits = sum(1 for s in SOFT_SKILLS if s in t)
    return min(10, round(hits * 1.5, 1))

def hard_skills_match(resume, jd):
    field = detect_resume_field(resume)
    skills = FIELD_SKILLS.get(field, [])
    jd_skills = [s for s in skills if s in jd]
    if not jd_skills:
        return 0.0
    matched = sum(1 for s in jd_skills if s in resume)
    return round((matched / len(jd_skills)) * 10, 1)

def hard_skills_strength(resume):
    field = detect_resume_field(resume)
    skills = FIELD_SKILLS.get(field, [])
    if not skills:
        return 0.0
    found = sum(1 for s in skills if s in resume)
    return round((found / len(skills)) * 10, 1)

def detailed_breakdown(resume_text, job_desc):
    resume = resume_text.lower()
    jd = job_desc.lower()

    data = {
        "Formatting_Structure": formatting_structure_score(resume),
        "Soft_Skills_Tone": soft_skills_tone_score(resume)
    }

    if job_desc:
        data["Hard_Skills_Match"] = hard_skills_match(resume, jd)
    else:
        data["Hard_Skills_Strength"] = hard_skills_strength(resume)

    return data
