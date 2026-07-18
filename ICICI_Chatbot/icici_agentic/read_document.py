
import os

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

KNOWLEDGE_BASE = os.path.join(
    BASE_DIR,
    "knowledge-base"
)

def read_documents(search_results):
    """
    Reads the contents of the retrieved knowledge base documents.

    Args:
        search_results (list): List returned by semantic_search.py

    Returns:
        list: List of dictionaries containing filename and content.
    """

    documents = []    
   
    for result in search_results:

        path = os.path.join(
            KNOWLEDGE_BASE,
            result["filename"]
        )
        # print(f"Reading: {path}")
        # print(f"Exists : {os.path.exists(path)}")

        if not os.path.exists(path):
            #print(f"[WARNING] File not found: {path}")
            continue

        with open(path, "r", encoding="utf-8") as f:

            documents.append({
                "filename": result["filename"],
                "title": result.get("title", ""),
                "category": result.get("category", ""),
                "score": result.get("score", 0),
                "content": f.read()
            })

    return documents


def build_context(documents):
    """
    Converts the retrieved documents into a context string
    that will be sent to the LLM.
    """

    context = ""

    for doc in documents:

        context += f"""
==================================================
FILE: {doc['filename']}
TITLE: {doc['title']}
CATEGORY: {doc['category']}
SIMILARITY SCORE: {doc['score']:.3f}
==================================================

{doc['content']}

"""

    return context