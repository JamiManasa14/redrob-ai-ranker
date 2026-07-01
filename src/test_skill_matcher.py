import json

from read_jd import read_job_description
from skill_matcher import skill_match_score

jd = read_job_description("data/job_description.docx")

with open("data/sample_candidates.json") as f:
    candidate = json.load(f)[0]

candidate_skills = [
    s["name"]
    for s in candidate["skills"]
]

score, matched, required = skill_match_score(
    jd,
    candidate_skills
)

print("Required Skills:\n")
print(required)

print("\nCandidate Skills:\n")
print(candidate_skills)

print("\nMatched Skills:\n")
print(matched)

print(f"\nSkill Match Score: {score:.2f}")