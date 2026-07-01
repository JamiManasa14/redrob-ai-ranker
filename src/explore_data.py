import json
from pathlib import Path

DATA_PATH = Path("data/candidates.jsonl")

# Read first 5 candidates
with open(DATA_PATH, "r", encoding="utf-8") as f:
    candidates = [json.loads(next(f)) for _ in range(5)]

print("=" * 60)
print(f"Loaded {len(candidates)} sample candidates")
print("=" * 60)

print("\nAvailable Fields:\n")
for key in candidates[0].keys():
    print("-", key)

print("\nFirst Candidate:\n")
for key, value in candidates[0].items():
    print(f"\n{key}:")
    print(value)