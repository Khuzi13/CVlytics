from .skill_bank import FIELD_SKILLS


def detect_resume_field(text):
    text = text.lower()
    scores = {f: sum(1 for s in skills if s in text)
              for f, skills in FIELD_SKILLS.items()}
    return max(scores, key=scores.get)
