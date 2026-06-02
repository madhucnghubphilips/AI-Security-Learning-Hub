from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

import faiss
import httpx
import numpy as np

_KB_DIR = Path(__file__).parent / "knowledge_base"
OLLAMA_BASE_URL = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"


@lru_cache(maxsize=1)
def _load_index() -> tuple:
    """Load FAISS index and metadata. Cached after first call."""
    index = faiss.read_index(str(_KB_DIR / "faiss.index"))
    with open(_KB_DIR / "metadata.json", encoding="utf-8") as f:
        metadata = json.load(f)
    return index, metadata


def _embed(text: str) -> np.ndarray:
    """Embed text using nomic-embed-text via Ollama. Returns float32 vector."""
    response = httpx.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json={"model": EMBED_MODEL, "prompt": text},
        timeout=30.0,
    )
    response.raise_for_status()
    return np.array(response.json()["embedding"], dtype=np.float32)


def retrieve(scenario: str, message: str) -> str:
    """Return the knowledge base document most relevant to the given scenario and message.

    Searches the FAISS index across all documents, then returns the best match
    that belongs to the requested scenario. Since each scenario has exactly one
    document, this is deterministic — but the vector search makes the retrieval
    architecturally authentic.

    Returns an empty string if no document exists for the scenario.
    """
    index, metadata = _load_index()

    query_vec = _embed(message).reshape(1, -1)
    faiss.normalize_L2(query_vec)

    # Search across all docs — k = total doc count
    k = min(index.ntotal, len(metadata))
    _, indices = index.search(query_vec, k=k)

    # Return first result that matches the requested scenario
    for idx in indices[0]:
        if 0 <= idx < len(metadata) and metadata[idx]["scenario"] == scenario:
            return metadata[idx]["text"]

    return ""
