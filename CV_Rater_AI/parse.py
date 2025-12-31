
import re

SECTION_KEYWORDS = [
    "summary", "experience", "education", "skills",
    "projects", "certifications", "internship"
]

def ats_parse_rate(raw_text: str) -> float:
    if not raw_text.strip():
        return 0.0

    text = raw_text.lower()
    words = re.findall(r"[a-z0-9]{2,}", text)
    total_words = max(len(words), 1)

    section_score = min(40, sum(5 for s in SECTION_KEYWORDS if s in text))
    contact_score = 15 if re.search(r"@", raw_text) else 0
    readability = (len([w for w in words if len(w) > 2]) / total_words) * 20
    noise_penalty = min(10, len(re.findall(r"[#@*&{}<>]", raw_text)) * 0.5)

    final = section_score + contact_score + readability - noise_penalty
    return round(max(0, min(100, final)), 2)
