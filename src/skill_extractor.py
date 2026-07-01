import re

# Technologies we know how to detect
TECH_KEYWORDS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",
    "go",
    "rust",

    "sql",
    "postgresql",
    "mysql",
    "mongodb",
    "redis",

    "docker",
    "kubernetes",

    "aws",
    "azure",
    "gcp",

    "spark",
    "airflow",
    "hadoop",

    "tensorflow",
    "pytorch",
    "scikit-learn",
    "sklearn",

    "llm",
    "llms",
    "rag",
    "langchain",
    "llamaindex",

    "faiss",
    "milvus",
    "pinecone",
    "qdrant",
    "weaviate",

    "bert",
    "transformers",
    "sentence-transformers",

    "openai",
    "anthropic",

    "lora",
    "qlora",
    "peft",

    "git",
    "github",

    "linux",

    "rest",
    "fastapi",
    "flask",

    "xgboost",

    "nlp",
    "machine learning",
    "deep learning",

    "elasticsearch",
    "opensearch",

    "vector database",
    "embeddings",

    "fine-tuning",

    "prompt engineering",

    "retrieval",

    "agentic ai"
}


def extract_skills(text):

    text = text.lower()

    found = []

    for skill in TECH_KEYWORDS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    return sorted(found)