import json
import os

import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDINGS_FILE = "embeddings.json"


# ---------------------------------------------------
# EMBEDDING
# ---------------------------------------------------

def get_embedding(text):

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding


# ---------------------------------------------------
# COSINE SIMILARITY
# ---------------------------------------------------

def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

def keyword_overlap_score(query, document):

    query_words = set(
        query.lower().split()
    )

    text = (
        document.get("title", "") + " " +
        document.get("category", "") + " " +
        document.get("tags", "")
    ).lower()

    doc_words = set(text.split())

    overlap = query_words.intersection(doc_words)

    if len(query_words) == 0:
        return 0

    return len(overlap) / len(query_words)
# ---------------------------------------------------
# RANK DOCUMENTS
# ---------------------------------------------------

def rank_documents(query, query_embedding, documents):

    ranked = []

    for doc in documents:

       embedding_score = cosine_similarity(
        query_embedding,
        doc["embedding"]
        )

       keyword_score = keyword_overlap_score(
            query,
            doc
        )

       final_score = (
            0.8 * embedding_score +
            0.2 * keyword_score
        )

       ranked.append({
            **doc,
            "embedding_score": float(embedding_score),
            "keyword_score": float(keyword_score),
            "score": float(final_score)
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked


# ---------------------------------------------------
# SEMANTIC SEARCH
# ---------------------------------------------------

def search_documents(
        query,
        threshold=0.55,
        max_results=5,
        documents=None):
    """
    Search documents using embeddings.

    Parameters
    ----------
    query : str
        User query.

    threshold : float
        Minimum similarity score.

    max_results : int
        Maximum documents to return.

    documents : list | None
        None -> search entire knowledge base.
        List -> search only these documents.
    """

    query_embedding = get_embedding(query)

    # First search over the full KB
    if documents is None:

        with open(
            EMBEDDINGS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            documents = json.load(f)

    ranked = rank_documents(
        query,
        query_embedding,
        documents
    )
    
   # print("\nTop Retrieval Results\n")

    # for doc in ranked[:10]:
    #     print( f"{doc['score']:.3f}  {doc['filename']}"
    # )

    filtered = [
        doc
        for doc in ranked
        if doc["score"] >= threshold
    ]

    if filtered:
        return filtered[:max_results]
    
    

    return ranked[:max_results]


# ---------------------------------------------------
# TEST
# ---------------------------------------------------

if __name__ == "__main__":

    while True:

        question = input("\nQuestion: ")

        if question.lower() in [
            "exit",
            "quit"
        ]:
            break

        matches = search_documents(question)

        print("\nTop Matches\n")

        for i, match in enumerate(matches, start=1):

            print(f"{i}. {match['filename']}")
            print(f"   Score    : {match['score']:.3f}")
            print(f"   Title    : {match['title']}")
            print(f"   Category : {match['category']}")
            print(f"   Tags     : {match['tags']}")
            print()