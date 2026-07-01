import json
import faiss
import numpy as np
import pandas as pd

from embedding_service import get_embedding
from read_jd import read_job_description

print("Loading FAISS index...")

index = faiss.read_index(
    "outputs/candidate_index.faiss"
)

with open(
    "outputs/candidate_ids.json",
    "r",
    encoding="utf-8"
) as f:
    candidate_ids = json.load(f)

jd = read_job_description(
    "data/job_description.docx"
)

print("Embedding Job Description...")

jd_embedding = get_embedding(jd).astype("float32")

jd_embedding = np.expand_dims(
    jd_embedding,
    axis=0
)

TOP_K = 1000

scores, indices = index.search(
    jd_embedding,
    TOP_K
)

results = []

for rank in range(TOP_K):

    idx = indices[0][rank]

    score = float(scores[0][rank])

    results.append({

        "rank": rank + 1,

        "candidate_id": candidate_ids[idx],

        "semantic_score": score

    })

df = pd.DataFrame(results)

df.to_csv(
    "outputs/semantic_scores.csv",
    index=False
)

print("\nTop 20 Results\n")

print(df.head(20))

print("\nSaved semantic_scores.csv")