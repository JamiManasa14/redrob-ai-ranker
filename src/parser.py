import json
from pathlib import Path

DATA_PATH = Path("data/candidates.jsonl")


def load_candidates():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def parse_candidate(candidate):
    profile = candidate["profile"]

    parsed = {
        "candidate_id": candidate["candidate_id"],
        "name": profile.get("anonymized_name"),
        "headline": profile.get("headline"),
        "summary": profile.get("summary"),
        "location": profile.get("location"),
        "country": profile.get("country"),
        "experience": profile.get("years_of_experience"),
        "current_title": profile.get("current_title"),
        "current_company": profile.get("current_company"),
        "skills": [s["name"] for s in candidate["skills"]],
        "companies": [c["company"] for c in candidate["career_history"]],
        "job_titles": [c["title"] for c in candidate["career_history"]],
        "education": [
            e["degree"] + " " + e["field_of_study"]
            for e in candidate["education"]
        ],
        "languages": [
            l["language"] for l in candidate["languages"]
        ],
        "profile_score": candidate["redrob_signals"]["profile_completeness_score"],
        "github_score": candidate["redrob_signals"]["github_activity_score"],
        "open_to_work": candidate["redrob_signals"]["open_to_work_flag"],
        "notice_period": candidate["redrob_signals"]["notice_period_days"],
    }

    return parsed


if __name__ == "__main__":

    candidates = load_candidates()

    parsed = parse_candidate(candidates[0])

    for key, value in parsed.items():
        print(f"{key}: {value}")