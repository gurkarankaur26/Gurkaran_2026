import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

KNOWLEDGE_BASE = "knowledge-base"
OUTPUT_FILE = "embeddings.json"


def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


def parse_document(filepath):
    """
    Parses documents with the following format:

    TITLE:
    SOURCE:
    CATEGORY:
    TAGS:
    CONTENT:
    KEY POINTS:
    URL:
    """

    fields = {
        "TITLE": "",
        "SOURCE": "",
        "CATEGORY": "",
        "TAGS": "",
        "CONTENT": "",
        "KEY POINTS": "",
        "URL": ""
    }

    current_field = None

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip()

            found = False
            for field in fields.keys():
                if line.startswith(field + ":"):
                    current_field = field
                    fields[field] = line[len(field)+1:].strip()
                    found = True
                    break

            if not found and current_field:
                fields[current_field] += "\n" + line

    return fields


embeddings = []

for file in Path(KNOWLEDGE_BASE).glob("*.txt"):

    print(f"Processing {file.name}")

    doc = parse_document(file)

    embedding_text = f"""
TITLE:
{doc['TITLE']}

CATEGORY:
{doc['CATEGORY']}

TAGS:
{doc['TAGS']}

KEY POINTS:
{doc['KEY POINTS']}

CONTENT:
{doc['CONTENT']}
"""

    embedding = get_embedding(embedding_text)

    embeddings.append({
        "filename": file.name,
        "title": doc["TITLE"],
        "source": doc["SOURCE"],
        "category": doc["CATEGORY"],
        "tags": doc["TAGS"],
        "url": doc["URL"],
        "embedding": embedding
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(embeddings, f)

print(f"\nCreated embeddings for {len(embeddings)} documents.")
print(f"Saved to {OUTPUT_FILE}")