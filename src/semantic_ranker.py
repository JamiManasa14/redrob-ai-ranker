import json

from sklearn.metrics.pairwise import cosine_similarity

from embedding_service import get_embedding
from parser import parse_candidate
from read_jd import read_job_description


# ------------------------
# Load Candidates
# ------------------------

candidates = []

with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        candidates.append(json.loads(line))


# ------------------------
# Read Job Description
# ------------------------

jd_text = read_job_description("data/job_description.docx")

print("Generating JD embedding...")

jd_embedding = get_embedding(jd_text)

print("Done!\n")


results = []


for candidate in candidates:

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
    """

    candidate_embedding = get_embedding(text)

    similarity = cosine_similarity(
        [jd_embedding],
        [candidate_embedding]
    )[0][0]

    results.append(
        (
            profile["candidate_id"],
            similarity
        )
    )


results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("Top 10 Semantic Matches\n")

for i, (cid, score) in enumerate(results[:10], 1):

    print(
        f"{i:2d}. {cid}   {score:.4f}"
    )