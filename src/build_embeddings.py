import json
import numpy as np

from parser import parse_candidate
from embedding_service import get_embeddings

candidate_ids = []
candidate_texts = []

print("Reading candidates...")

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        profile = parse_candidate(candidate)

        text = f"""
        {profile['headline']}

        {profile['summary']}

        Skills:
        {' '.join(profile['skills'])}

        Companies:
        {' '.join(profile['companies'])}

        Job Titles:
        {' '.join(profile['job_titles'])}

        Education:
        {' '.join(profile['education'])}

        Languages:
        {' '.join(profile['languages'])}
        """

        candidate_ids.append(profile["candidate_id"])
        candidate_texts.append(text)

print(f"Loaded {len(candidate_texts)} candidates")

print("Generating embeddings...")

embeddings = get_embeddings(candidate_texts)

print("Saving...")

np.save("outputs/candidate_embeddings.npy", embeddings)

with open("outputs/candidate_ids.json", "w") as f:
    json.dump(candidate_ids, f)

print("Done!")