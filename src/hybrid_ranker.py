import json
import pandas as pd

from feature_extractor import extract_features
from read_jd import read_job_description
from skill_matcher import skill_match_score

# =====================================================
# Weights
# =====================================================

SEMANTIC_WEIGHT = 0.50
EXPERIENCE_WEIGHT = 0.20
SKILL_MATCH_WEIGHT = 0.15
PROFILE_WEIGHT = 0.05
GITHUB_WEIGHT = 0.03
RESPONSE_WEIGHT = 0.03
OPEN_TO_WORK_WEIGHT = 0.02


# =====================================================
# Load Semantic Scores
# =====================================================

print("Loading semantic scores...")

semantic_df = pd.read_csv("outputs/semantic_scores.csv")

semantic_df = semantic_df.head(1000)

semantic_scores = {
    row["candidate_id"]: row["semantic_score"] for _, row in semantic_df.iterrows()
}


# =====================================================
# Read Job Description
# =====================================================

print("Reading Job Description...")

jd_text = read_job_description("data/job_description.docx")


# =====================================================
# Read Candidates
# =====================================================

print("Reading candidates...")

results = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        features = extract_features(candidate)

        candidate_id = features["candidate_id"]

        if candidate_id not in semantic_scores:
            continue

        semantic = semantic_scores[candidate_id]

        # Normalize features
        experience = min(features["experience"] / 10, 1)

        profile = features["profile_score"] / 100

        github = max(features["github_score"], 0) / 100

        response = features["response_rate"]

        open_work = 1 if features["open_to_work"] else 0

        # NEW: Actual skill match
        skill_score, matched_skills, required_skills = skill_match_score(
            jd_text, features["skills"]
        )

        final_score = (
            semantic * SEMANTIC_WEIGHT
            + experience * EXPERIENCE_WEIGHT
            + skill_score * SKILL_MATCH_WEIGHT
            + profile * PROFILE_WEIGHT
            + github * GITHUB_WEIGHT
            + response * RESPONSE_WEIGHT
            + open_work * OPEN_TO_WORK_WEIGHT
        )

        results.append(
            {
                "candidate_id": candidate_id,
                "semantic_score": round(semantic, 4),
                "skill_match": round(skill_score, 4),
                "matched_skills": ", ".join(matched_skills),
                "experience": features["experience"],
                "github": features["github_score"],
                "profile_score": features["profile_score"],
                "response_rate": features["response_rate"],
                "open_to_work": features["open_to_work"],
                "final_score": round(final_score, 4),
            }
        )


# =====================================================
# Final Ranking
# =====================================================

df = pd.DataFrame(results)

df = df.sort_values(by="final_score", ascending=False).reset_index(drop=True)

print("\n========== TOP 20 HYBRID RANKINGS ==========\n")

print(df.head(20))

df.to_csv("outputs/final_rankings.csv", index=False)

print("\nSaved outputs/final_rankings.csv")
