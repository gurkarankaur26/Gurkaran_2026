flowchart TD

A[User Question] --> B[Generate Query Embedding]

B --> C[Load embeddings.json]

C --> D[Hybrid Search]
D --> E[Top K Documents]

E --> F[Read Documents]

F --> G[Build Prompt]

G --> H[GPT-4.1-mini]

H --> I{Decision}

I -->|ANSWER| J[Return Response]

I -->|ASKUSER| K[Ask Clarification]
K --> A

I -->|SEARCH| L[Search Again]
L --> E