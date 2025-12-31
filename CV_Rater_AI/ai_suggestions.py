# from skill_bank import FIELD_SKILLS
# from field_detector import detect_resume_field
# import re

# def ai_suggestions(resume_text):
#     text = resume_text.lower()
#     suggestions = []

#     # ---------- CONTACT ----------
#     email = bool(re.search(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text))
#     phone = bool(re.search(r"\b\d{10,13}\b", text))

#     if not email or not phone:
#         suggestions.append("Contact information is missing or incomplete")
#     else:
#         suggestions.append("Contact information is clear and correct")

#     # ---------- EDUCATION ----------
#     edu_words = ["education","bachelor","master","bs","ms","phd","university","college"]
#     if not any(w in text for w in edu_words):
#         suggestions.append("Education section is missing or weak")
#     else:
#         suggestions.append("Education section is properly formatted")

#     # ---------- FIELD SMART SKILL GAP ----------
#     field = detect_resume_field(text)
#     skills = FIELD_SKILLS.get(field, [])

#     weak_skills = []
#     for s in skills:
#         count = text.count(s)
#         if count == 0:
#             weak_skills.append(s)

#     # show only meaningful suggestions
#     for s in weak_skills[:2]:
#         suggestions.insert(0, f'Consider adding experience with "{s.title()}"')

#     return suggestions


from .skill_bank import FIELD_SKILLS
from .field_detector import detect_resume_field
import re


def ai_suggestions(resume_text, parse_rate):
    text = resume_text.lower()
    suggestions = []

    # ---------- LOW PARSE RATE WARNING ----------
    if parse_rate <= 10:
        return [
            "Your resume content is extremely weak or unreadable.",
            "Please rewrite your CV with proper headings, bullet points and clear text.",
            "Avoid using images-only resumes. Use simple text format.",
            "Use standard fonts and clear section headings for better parsing."
        ]

    # ---------- CONTACT ----------
    email = bool(re.search(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text))
    phone = bool(re.search(r"\b\d{10,13}\b", text))

    if not email or not phone:
        suggestions.append("Contact information is missing or incomplete")
    else:
        suggestions.append("Contact information is clear and correct")

    # ---------- EDUCATION ----------
    edu_words = ["education","bachelor","master","bs","ms","phd","university","college"]
    if not any(w in text for w in edu_words):
        suggestions.append("Education section is missing or weak")
    else:
        suggestions.append("Education section is properly formatted")

    # ---------- FIELD SMART SKILL GAP ----------
    field = detect_resume_field(text)
    skills = FIELD_SKILLS.get(field, [])

    weak_skills = []
    for s in skills:
        if s not in text:
            weak_skills.append(s)

    for s in weak_skills[:2]:
        suggestions.insert(0, f'Consider adding experience with "{s.title()}"')

    return suggestions
