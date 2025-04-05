"""
ClusterStruck – MVP Script
A semantic styling studio for LLM-native content and persona designers.

Goal:
- Input: A list of 20 LLM-generated completions for a given system + user prompt
- Process:
    1. Embed each output using the Mistral Embed API
    2. Cluster the embeddings using HDBSCAN
    3. Group and return completions by cluster
- Output: A list of clusters, each containing 5–10 stylistically similar outputs
"""

# === Imports ===
import os
import requests
import numpy as np
from typing import List, Dict
# from hdbscan import HDBSCAN  # uncomment once HDBSCAN installed


# === Constants ===
MISTRAL_EMBED_URL = "https://api.mistral.ai/v1/embeddings"
MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY")

# Raise an error if the variable is not set
if not MISTRAL_API_KEY:
    raise ValueError("Missing API key! Please set the MISTRAL_API_KEY environment variable.")

# Sample data: LLM-generated completions for testing
SAMPLE_COMPLETIONS = [
    "This suit rides smoother than a sea breeze—eco-friendly, ocean-approved.",
    "Minimal drag. Maximum glide. Sustainability you can surf on.",
    "Seafoam shimmer, neoprene-free dreams. You ready?",
    "It hugs like kelp and flies like foam. Let’s ride.",
    # ...Add 16 more mock completions or generate with Mistral later
]


# === Core Pipeline Functions ===

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """
    Send a list of texts to the Mistral Embed API.
    Return a list of embedding vectors.
    """
    # TODO: Implement Mistral embed API call (batch if needed)
    pass


def cluster_embeddings(vectors: List[List[float]]) -> List[int]:
    """
    Cluster embedding vectors using HDBSCAN.
    Return a list of cluster labels (integers, where -1 = outlier).
    """
    # TODO: Fit HDBSCAN and return cluster assignments
    pass


def group_by_cluster(texts: List[str], labels: List[int]) -> Dict[int, List[str]]:
    """
    Group original completions by their cluster label.
    Return a dict: {cluster_id: [text1, text2, ...]}
    """
    # TODO: Build and return the grouping dictionary
    pass


def print_clusters(grouped_clusters: Dict[int, List[str]]) -> None:
    """
    Print each cluster's ID and the completions it contains.
    """
    for cluster_id, completions in grouped_clusters.items():
        header = f"Cluster {cluster_id}" if cluster_id != -1 else "Outliers"
        print(f"\n=== {header} ===")
        for text in completions:
            print(f"- {text}")


# === Main Entry Point ===

def main():
    print("Embedding texts...")
    embeddings = get_embeddings(SAMPLE_COMPLETIONS)

    print("Clustering embeddings...")
    labels = cluster_embeddings(embeddings)

    print("Grouping by cluster...")
    grouped = group_by_cluster(SAMPLE_COMPLETIONS, labels)

    print("Cluster Results:")
    print_clusters(grouped)


if __name__ == "__main__":
    main()