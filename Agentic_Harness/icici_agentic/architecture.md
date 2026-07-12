End-to-End Data Pipeline

ICICI Website
      │
      ▼
Crawler
      │
      ▼
Raw Pages
      │
      ▼
Chunking
      │
      ▼
Structured Documents
      │
      ▼
Embedding Generation
      │
      ▼
embeddings.json
      │
      ▼
Agentic Chatbot



Complete Architecture

User
 │
 ▼
agentic.py
 │
 ├── semantic-search.py
 │      │
 │      ├── OpenAI Embeddings
 │      ├── Cosine Similarity
 │      └── Hybrid Ranking
 │
 ├── read-document.py
 │      │
 │      └── knowledge-base/*.txt
 │
 └── GPT-4.1-mini
        │
        ├── ANSWER
        ├── ASKUSER
        └── SEARCH