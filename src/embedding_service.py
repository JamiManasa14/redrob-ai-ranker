from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded!")


def get_embedding(text):
    return model.encode(
        text,
        normalize_embeddings=True
    )


def get_embeddings(texts):
    return model.encode(
        texts,
        batch_size=64,
        show_progress_bar=True,
        normalize_embeddings=True
    )

if __name__ == "__main__":
    text = """
    Built RAG applications using LangChain and FAISS.
    """

    emb = get_embedding(text)

    print("Embedding size:", len(emb))
    print(emb[:10])