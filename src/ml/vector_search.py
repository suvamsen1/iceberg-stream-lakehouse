"""
AI / Vector Ingestion Bridge for Incident Analysis (RAG for Ops).
Extracts telemetry anomaly incident logs, generates dense vector representations,
and provides semantic similarity search for root-cause diagnosis.
"""

import math
from typing import List, Dict, Any, Tuple


class IncidentVectorIndexer:
    """
    Lightweight vector indexer for telemetry incident descriptions and anomalies.
    Enables semantic RAG queries across historical system incidents.
    """

    def __init__(self, dimension: int = 16):
        self.dimension = dimension
        self.index: List[Dict[str, Any]] = []

    def _embed_text(self, text: str) -> List[float]:
        """
        Generates deterministic normalized pseudo-embeddings for incident text
        using character n-gram hashing and L2 normalization.
        """
        vec = [0.0] * self.dimension
        for i, char in enumerate(text.lower()):
            idx = (ord(char) * (i + 1)) % self.dimension
            vec[idx] += 1.0

        # L2 Normalize
        norm = math.sqrt(sum(x * x for x in vec))
        if norm > 0:
            vec = [x / norm for x in vec]
        return vec

    def index_incident(self, incident_id: str, device_id: str, description: str, metadata: Dict[str, Any]):
        """Adds an incident log entry into the vector index."""
        embedding = self._embed_text(description)
        self.index.append({
            "incident_id": incident_id,
            "device_id": device_id,
            "description": description,
            "embedding": embedding,
            "metadata": metadata
        })

    def search_similar_incidents(self, query: str, top_k: int = 3) -> List[Tuple[Dict[str, Any], float]]:
        """Finds top-k semantically similar incidents via cosine similarity."""
        query_vec = self._embed_text(query)
        scores = []
        for item in self.index:
            doc_vec = item["embedding"]
            cos_sim = sum(q * d for q, d in zip(query_vec, doc_vec))
            scores.append((item, round(cos_sim, 4)))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:top_k]
