import re
import importlib

# Import modules with hyphens in their names
semantic_search = importlib.import_module('semantic-search')
read_document = importlib.import_module('read-document')
search_documents = semantic_search.search_documents
read_documents = read_document.read_documents

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MAX_ITERATIONS = 5
SYSTEM_PROMPT = """
You are Kajal, the virtual banking assistant for ICICI Bank.

Your job is to answer user questions using ONLY the provided banking documents.

You MUST perform ONLY ONE action:

ACTION 1

ANSWER:
<your complete answer>

ACTION 2

ASKUSER:
<clarification question>

ACTION 3

SEARCH:
<search query>

Do not include anything else.
Do not write ACTION 1, ACTION 2 or ACTION 3.

Rules:

1. Use ANSWER only when sufficient information exists.
2. Use ASKUSER if the user's intent is unclear.
3. Use SEARCH if additional banking information is required. If the retrieved documents do not contain sufficient information to answer the question,
   you MUST use SEARCH instead of ANSWER. Do not return "I don't know" or "insufficient information"
   unless SEARCH has already been attempted and still no relevant information is found. 
4. Never invent banking information.
5. Never mention the knowledge base.
6. Never explain your reasoning.
7. Your name is Kajal.
8. Never refer to yourself as Assistant, AI Assistant, ChatGPT, or ICICI Agentic Assistant.
9. If asked your name, reply that your name is Kajal.
10. When greeting the user for the first time, introduce yourself as:
    "Hello! I'm Kajal, your ICICI Bank assistant."
11. Use clean formatting to make answers easy to read.
12. Do not use any action other than ANSWER, ASKUSER, or SEARCH.
13. Output only the action and its value.
"""
def call_llm(question, history, documents):

    user_prompt = f"""
Current User Question:

{question}

Conversation History:

{history}

Retrieved Documents:

{documents}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    content = response.choices[0].message.content

    if content is None:
        return "ANSWER:\nSorry, I couldn't generate a response."

    return content.strip()

def parse_action(response):

    response = (response or "").strip()

    if response.startswith("ANSWER:"):
        return (
            "ANSWER",
            response.replace("ANSWER:", "").strip()
        )

    if response.startswith("ASKUSER:"):
        return (
            "ASKUSER",
            response.replace("ASKUSER:", "").strip()
        )

    if response.startswith("SEARCH:"):
        return (
            "SEARCH",
            response.replace("SEARCH:", "").strip()
        )

    return ("ANSWER", response)


def run_agent(question):

    history = ""

    retrieved_docs = {}

    search_results = search_documents(question)
    
    #print("\nRetrieved documents:")    

    for doc in search_results:
        #print("-", doc["filename"])
        retrieved_docs[
            doc["filename"]
        ] = doc

    for _ in range(MAX_ITERATIONS):

        docs = read_documents(
            list(retrieved_docs.values())
        )

        document_text = "\n\n".join(

            [
                d["content"]
                for d in docs
            ]
        )

        response = call_llm(

            question,

            history,

            document_text

        )
        
        # print("\n================ DOCUMENTS SENT TO GPT ================\n")
        # print(document_text[:5000])
        # print("\n=======================================================\n")

        #print("\nLLM\n")

       # print(response)

        action, value = parse_action(response)

        if action == "ANSWER":

            return value

        elif action == "ASKUSER":

            print()

            answer = input(value + "\n> ")

            history += (
                f"\nUser: {answer}"
            )

            question += (
                "\n"
                + answer
            )

            search_results = search_documents(answer)

            for doc in search_results:

                retrieved_docs[
                    doc["filename"]
                ] = doc

        elif action == "SEARCH":

            search_results = search_documents(
                value
            )

            for doc in search_results:

                retrieved_docs[
                    doc["filename"]
                ] = doc

    return "Sorry, I couldn't find sufficient information."

if __name__ == "__main__":

    print("\nKajal - ICICI Banking Assistant\n")

    try:
        while True:

            question = input("\nYou: ")

            if question.lower() in ["exit", "quit", "bye"]:
                break

            answer = run_agent(question)

            print("\nKajal:\n")
            print(answer)

    except KeyboardInterrupt:
        print("\n\nShutting down Kajal...")