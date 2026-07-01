from skill_extractor import extract_skills


def skill_match_score(jd_text, candidate_skills):
    """
    Returns:
        score: float between 0 and 1
        matched_skills: list
        required_skills: list
    """

    required = set(extract_skills(jd_text))

    candidate = set()

    for skill in candidate_skills:
        candidate.add(skill.lower())

    matched = required.intersection(candidate)

    if len(required) == 0:
        return 0.0, [], []

    score = len(matched) / len(required)

    return score, sorted(list(matched)), sorted(list(required))