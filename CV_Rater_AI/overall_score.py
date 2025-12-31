def overall_ats_score(ats_score, jd_match, parse_rate):
    return round(
        0.30 * ats_score +
        0.35 * parse_rate +
        0.35 * jd_match,
        2
    )


def overall_score_no_jd(ats_score, parse_rate):
    return round(
        0.6 * ats_score + 
        0.4 * parse_rate,
         2)