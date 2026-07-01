from parser import parse_candidate


def extract_features(candidate):

    profile = parse_candidate(candidate)

    signals = candidate.get("redrob_signals", {})

    skills = candidate.get("skills", [])

    return {
        "candidate_id": profile["candidate_id"],
        "experience": profile["experience"],
        "skills": [s.get("name", "") for s in skills],
        "num_skills": len(skills),
        "github_score": signals.get("github_activity_score", 0),
        "profile_score": signals.get("profile_completeness_score", 0),
        "response_rate": signals.get("recruiter_response_rate", 0),
        "notice_period": signals.get("notice_period_days", 90),
        "open_to_work": signals.get("open_to_work_flag", False),
        "saved_by_recruiters": signals.get("saved_by_recruiters_30d", 0),
        "interview_completion_rate": signals.get("interview_completion_rate", 0),
        "offer_acceptance_rate": signals.get("offer_acceptance_rate", 0),
        "search_appearance": signals.get("search_appearance_30d", 0),
    }
