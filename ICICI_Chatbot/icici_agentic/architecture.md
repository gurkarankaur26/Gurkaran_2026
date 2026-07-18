Knowledge Base Creation (Offline)
---------------------------------
ICICI Website / Documents
        ↓
Document Structuring
        ↓
knowledge-base/*.txt
        ↓
Embedding Generation
        ↓
embeddings.json


Runtime Flow (Online)
---------------------
User Question
        ↓
Semantic Search
        ↓
Read Relevant Documents
        ↓
Build Context
        ↓
LLM Agent 
        ↓
┌─────────────┬─────────────┬─────────────┐
│             │             │             │
ANSWER      ASKUSER       SEARCH
│             │             │
Return      Get user      Retrieve more
response    clarification documents
│             │             │
└─────────────┴──────┬──────┘
                     ↓
                Agent Loop
                     ↓
              Final Answer





Component Responsibilities

knowledge-base/

    Stores structured banking documents containing:

    Title
    Category
    Tags
    Key Points
    Content
    URL

embeddings.py
    Generates embeddings for every knowledge base document.
    Uses document metadata and content for richer semantic understanding.
    Stores embeddings in embeddings.json.


semantic_search.py

    Generates query embeddings.
    Calculates:
        Embedding similarity score.
        Keyword overlap score.
        Computes final ranking:
        Final Score =    0.8 × Embedding Similarity +  0.2 × Keyword Match
        Returns the most relevant documents.

read_document.py
    Loads retrieved document contents from disk.
    Builds structured context for the LLM. single formatted context stringFor e.g.
        FILE: fixed_deposit.txt
        TITLE: Fixed Deposit
        CATEGORY: Deposits
        SIMILARITY SCORE: 0.912
    Includes relevance scores to help the model prioritize documents.


agentic.py

Acts as the decision maker.

The LLM can choose only one action:

ANSWER → respond to the user.
ASKUSER → request a single clarification question.
SEARCH → retrieve additional information.
Agent Loop

The chatbot follows an iterative cycle:


Retrieve Information
↓
Reason Using LLM
↓
Search More / Ask User / Answer
↓
Update Context
↓
Repeat

Key Capabilities
Semantic document retrieval using embeddings.
Exact banking product matching using keyword boosting.
Multi-step reasoning through an agent loop.
Clarification questions for recommendation and advisory scenarios.
Multiple retrieval rounds for complex queries.
Multi-document reasoning and comparison.
Conversation-aware decision making.