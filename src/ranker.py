from feature_extractor import extract_features
from parser import load_candidates


def calculate_score(features):
    score = 0

    # Experience (max ~20 points)
    score += min(features["experience"] * 2, 20)

    # Profile quality
    score += features["profile_score"] * 0.20

    # GitHub activity
    score += features["github_score"]

    # Recruiter response
    score += features["response_rate"] * 10

    # Availability
    if features["open_to_work"]:
        score += 5

    if features["notice_period"] <= 30:
        score += 5
    elif features["notice_period"] <= 60:
        score += 2

    # Technical capability
    if features["has_vector_db"]:
        score += 10

    if features["has_embeddings"]:
        score += 10

    if features["has_llm"]:
        score += 10

    if features["has_retrieval"]:
        score += 10

    return round(score, 2)


def rank_candidates():
    candidates = load_candidates()

    ranked = []

    for candidate in candidates:
        features = extract_features(candidate)
        score = calculate_score(features)

        ranked.append({
            "candidate_id": features["candidate_id"],
            "score": score,
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)

    return ranked


if __name__ == "__main__":
    import pandas as pd

    ranked = rank_candidates()

    df = pd.DataFrame(ranked)

    df.to_csv("outputs/baseline_rankings.csv", index=False)

    print(df.head(10))
    print("\nSaved to outputs/baseline_rankings.csv")