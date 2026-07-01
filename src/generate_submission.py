import pandas as pd

print("Loading final rankings...")

df = pd.read_csv("outputs/final_rankings.csv")

# Sort by score (descending)
# If scores are equal, sort by candidate_id (ascending)
df = (
    df.sort_values(
        by=["final_score", "candidate_id"],
        ascending=[False, True]
    )
    .head(100)
    .reset_index(drop=True)
)

# Generate rank
df["rank"] = range(1, len(df) + 1)

# Submission score
df["score"] = df["final_score"].round(4)

# Generate reasoning
df["reasoning"] = (
    "Semantic="
    + df["semantic_score"].round(3).astype(str)
    + ", SkillMatch="
    + df["skill_match"].round(2).astype(str)
    + ", Exp="
    + df["experience"].astype(str)
    + " yrs"
)

# Final submission
submission = df[
    [
        "candidate_id",
        "rank",
        "score",
        "reasoning",
    ]
]

submission.to_csv(
    "outputs/submission.csv",
    index=False,
)

print("\nSubmission created successfully!\n")
print(submission.head(10))