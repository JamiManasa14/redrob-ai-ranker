import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from embedding_service import get_embedding
from read_jd import read_job_description


# ======================================================
# Load Candidate Embeddings
# ======================================================

print("Loading candidate embeddings...")

embeddings = np.load("outputs/candidate_embeddings.npy")

with open("outputs/candidate_ids.json", "r", encoding="utf-8") as f:
    candidate_ids = json.load(f)

print(f"Loaded {len(candidate_ids)} candidate embeddings")


# ======================================================
# Read Job Description
# ======================================================

print("\nReading Job Description...")

jd = read_job_description("data/job_description.docx")

print("Generating Job Description embedding...")

jd_embedding = get_embedding(jd)

print("Done!")


# ======================================================
# Calculate Similarity
# ======================================================

print("\nCalculating semantic similarity...")

scores = cosine_similarity(
    [jd_embedding],
    embeddings
)[0]


# ======================================================
# Rank Candidates
# ======================================================

top_k = 100

top_indices = np.argsort(scores)[::-1][:top_k]

results = []

for rank, idx in enumerate(top_indices, start=1):

    candidate_id = candidate_ids[idx]
    similarity_score = float(scores[idx])

    results.append({
        "rank": rank,
        "candidate_id": candidate_id,
        "semantic_score": round(similarity_score, 6)
    })


# ======================================================
# Display Top 20
# ======================================================

print("\n================ TOP 20 SEMANTIC MATCHES ================\n")

for row in results[:20]:
    print(
        f"{row['rank']:2d}. "
        f"{row['candidate_id']}    "
        f"{row['semantic_score']:.4f}"
    )


# ======================================================
# Save Results
# ======================================================

df = pd.DataFrame(results)

output_path = "outputs/semantic_scores.csv"

df.to_csv(output_path, index=False)

print("\n========================================================")
print(f"Semantic scores saved to: {output_path}")
print("========================================================")