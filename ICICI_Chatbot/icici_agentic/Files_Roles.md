embeddings.py
    ↓
Creates embeddings.json

semantic_search.py
    ↓
Ranks documents using
0.8 * embeddings +
0.2 * keyword overlap

read_document.py
    ↓
Loads document content
and builds LLM context

agentic.py
    ↓
Runs the SEARCH
ASKUSER
ANSWER loop