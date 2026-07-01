# Redrob AI Ranker

An AI-powered candidate ranking system that combines semantic search, skill matching, recruiter signals, and hybrid scoring to recommend the best candidates for a given job description.

---

# Overview

Traditional keyword matching often fails to identify strong candidates whose resumes use different terminology from the job description.

This project improves candidate ranking using modern NLP techniques by combining:

- Semantic Search (Sentence Transformers)
- Vector Search (FAISS)
- Skill Matching
- Candidate Experience
- Recruiter Signals
- Hybrid Weighted Ranking

The system processes over **100,000 candidate profiles** efficiently and produces explainable rankings.

---

# Architecture

```
                Job Description
                       │
              Read DOCX & Clean Text
                       │
             Sentence Transformer
                       │
                 JD Embedding
                       │
         ┌─────────────┴─────────────┐
         │                           │
Candidate Embeddings            Skill Extraction
         │                           │
         │                     Required Skills
         │                           │
         └─────────────┬─────────────┘
                       │
                FAISS Search
                       │
             Top Semantic Candidates
                       │
          Feature Extraction
                       │
      Experience / Skills / GitHub /
      Response Rate / Open to Work
                       │
              Hybrid Ranker
                       │
             Final Candidate Ranking
                       │
               submission.csv
```

---

# Features

## Semantic Search

Uses

- sentence-transformers/all-MiniLM-L6-v2

to generate dense vector embeddings for

- Job Description
- Candidate Profiles

Similarity is computed using cosine similarity.

---

## Vector Search

Uses FAISS for efficient Approximate Nearest Neighbor Search.

Advantages

- Fast retrieval
- Scales to large datasets
- Suitable for production systems

---

## Skill Matching

Required skills are extracted from the Job Description.

Candidate skills are normalized and matched against required skills.

Skill Match Score

```
Matched Skills / Required Skills
```

---

## Feature Engineering

The following candidate features are used.

| Feature | Description |
|----------|-------------|
| Semantic Score | Cosine similarity |
| Skill Match | Required skills matched |
| Experience | Years of experience |
| GitHub Activity | Recruiter signal |
| Profile Completeness | Recruiter signal |
| Recruiter Response Rate | Recruiter signal |
| Open To Work | Boolean signal |

---

# Hybrid Ranking Formula

```
Final Score =
0.50 × Semantic Score
+ 0.20 × Experience
+ 0.15 × Skill Match
+ 0.05 × Profile Score
+ 0.03 × GitHub Score
+ 0.03 × Recruiter Response Rate
+ 0.02 × Open To Work
```

---

# Project Structure

```
redrob-ai-ranker/

data/
    candidates.jsonl
    job_description.docx
    validate_submission.py

outputs/
    candidate_embeddings.npy
    candidate_ids.json
    semantic_scores.csv
    final_rankings.csv
    submission.csv

src/
    embedding_service.py
    read_jd.py
    parser.py
    feature_extractor.py
    skill_extractor.py
    skill_matcher.py
    build_embeddings.py
    build_faiss.py
    faiss_search.py
    hybrid_ranker.py
    generate_submission.py

requirements.txt
README.md
```

---

# Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Generate candidate embeddings

```bash
python src/build_embeddings.py
```

Build FAISS index

```bash
python src/build_faiss.py
```

Semantic Search

```bash
python src/faiss_search.py
```

Hybrid Ranking

```bash
python src/hybrid_ranker.py
```

Generate Submission

```bash
python src/generate_submission.py
```

Validate Submission

```bash
python data/validate_submission.py outputs/submission.csv
```

---

# Output

The final output file

```
outputs/submission.csv
```

contains

- Candidate ID
- Rank
- Score
- Explainable Reasoning

---

# Technologies Used

- Python
- Sentence Transformers
- Hugging Face
- FAISS
- NumPy
- Pandas
- Scikit-learn
- python-docx

---

# Future Improvements

- Cross-Encoder Re-ranking
- Learning-to-Rank (LightGBM/XGBoost)
- Better Skill Ontology
- Synonym-based Skill Matching
- LLM-based Candidate Explanation
- Real-time API Deployment

---

# Author

Jami Manasa
