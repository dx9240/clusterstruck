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
#the user add these phrases, moods, or sentences, or generate them
#this example is for a fictional online retailer called Surf Shop
SAMPLE_COMPLETIONS = [
    "This suit rides smoother than a sea breeze; it's eco-friendly, and ocean-approved.",
    "Minimal drag. Maximum glide. Sustainability you can surf on.",
    "It hugs like kelp and flies like foam. Let’s ride.",
    " A new era in big-wave surfing",
    "Sun, beach, and sea - the perfect escape.",
    "chill out on the beach with your buddies and enjoy the raw freedom of the waves.",
    "We're committed to doing our part to protect the ocean and marine life."
    "When the conditions are perfect a point break can create a really long wave to ride as the wave wraps around a point or headland and then runs along the coastline of a bay or cove. Point breaks can have rock, coral, or sandy bottoms. Most surfers would consider a point break the perfect wave as the actual time riding the surfboard will be the longest.",
    "A proper wax job can be the difference between making the wave of your life and being the laughing stock of the beach. Plus, most of us have enough reasons to fall off our boards without adding a dodgy wax job to the equation.",
    "No fast fashion, no plastic trash—just gear that respects the sea and your style.",
    "Built for the swell, not the spreadsheet.",
    "Ride clean. Surf harder. We’re not just ocean lovers—we’re ocean protectors.",
    "Wipeouts happen. Lame gear shouldn’t be the reason why.",
    "Leave the logos, keep the soul. Surf loud, dress simple.",
    "Our gear is tested by surfers and approved by sea turtles.",
    "Every sale supports reef restoration projects along threatened coastlines.",
    "The ocean gives us everything. We give back with every stitch.",
    "Made for waves, not waste—this wetsuit won’t cost the earth.",
    "From recycled fabric to biodegradable packaging—we’re not just talking change, we’re surfing it.",
    "Sustainability isn’t a trend. It’s a tide we choose to ride, every day.",
    "Sun-faded, sea-soaked, and just right—that’s the good stuff.",
    "The only appointment we keep is sunset.",
    "Ocean drift is a direction."
    "Respect the reef, but charge the set. This suit’s got you covered.",
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