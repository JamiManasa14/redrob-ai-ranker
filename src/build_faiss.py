import faiss
import numpy as np

print("Loading embeddings...")

embeddings = np.load("outputs/candidate_embeddings.npy").astype("float32")

print(f"Loaded {len(embeddings)} embeddings")

dimension = embeddings.shape[1]

print(f"Embedding Dimension: {dimension}")

# Create FAISS index
index = faiss.IndexFlatIP(dimension)

# Add embeddings
index.add(embeddings)

print(f"Indexed {index.ntotal} vectors")

faiss.write_index(
    index,
    "outputs/candidate_index.faiss"
)

print("\nFAISS index saved!")