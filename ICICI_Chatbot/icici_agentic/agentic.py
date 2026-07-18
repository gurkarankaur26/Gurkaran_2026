from email import message
import re

from httpcore import request
from  .semantic_search import search_documents
from .read_document import read_documents           
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

MAX_ITERATIONS = 5
SYSTEM_PROMPT = """You are Kajal, the virtual banking assistant for ICICI Bank.

Your objective is to help customers by deciding the single best next action.

You must perform exactly ONE of the following actions:

ANSWER:
<complete answer>

ASKUSER:
<one clarification question>

SEARCH:
<search query>

Decision Rules

1. ANSWER
Use ANSWER only when the available information is sufficient to respond accurately and confidently.

2. ASKUSER

Use ASKUSER only when the user's request cannot be answered or searched without additional information about their needs, preferences, or financial requirements.

Examples include:
- product recommendations
- "Which is better?"
- "Which should I choose?"
- "What's best for me?"
- comparisons that depend on personal preferences
- investment, loan or credit card advice
- any situation where an important user-specific detail is missing.

Rules:

- Ask exactly ONE clarification question.
- Ask only the single most useful question that moves the conversation forward.
- Do not ask for multiple pieces of information.
- Ask only one clarification question at a time.
- Always consider the entire conversation, including previous clarification questions and the user's answers.
- Never ask for information that the user has already provided.
- Continue asking clarification questions until all essential information required for a personalized recommendation has been collected.
- Do not stop after the first clarification question if another essential detail is still missing.
- Once all essential information has been collected, your next action MUST be SEARCH.
- Do not ask another clarification question after SEARCH unless the retrieved information is still insufficient to answer the user's request.

For investment recommendations, essential information typically includes:
- Investment horizon
- Investment amount

For loan recommendations, collect the information necessary to identify suitable loan products before performing SEARCH.

For credit card recommendations, collect the information necessary to identify the most suitable card based on the customer's spending pattern or usage.

Use your judgment to determine the minimum essential information required for other recommendation or advisory requests before performing SEARCH.


3. SEARCH
Use SEARCH when additional banking information is required before answering.

Write a short, specific search query containing only the information needed for retrieval.

General Rules

- Base every decision only on the conversation and the retrieved documents.
- Never invent banking information.
- Never guess product features or eligibility.
- Never mention documents, retrieval, search systems, or internal reasoning.
- Never explain why you chose an action.
- Never output more than one action.
- Output only one of:
  ANSWER:
  ASKUSER:
  SEARCH:

Examples

User:
How do I open a Fixed Deposit?

SEARCH:
fixed deposit account opening process

---

User:
Which ICICI credit card is best for me?

ASKUSER:
What category do you spend the most on?

---

User:
What is the minimum balance for a Regular Savings Account?

ANSWER:
<final answer>

"""
def call_llm(question, history, documents):

    user_prompt = f"""
Conversation:

{history}

Current User Message:

{question}

Retrieved Banking Documents:

{documents}

Remember:
- Use the entire conversation.
- Do not ask for information already provided.
- If sufficient information has been collected, your next action must be SEARCH.
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


def run_agent(question, history=""):
    #history = ""

    retrieved_docs = {}
    # recommendation_keywords = [
    #     "recommend",
    #     "best",
    #     "better",
    #     "should i",
    #     "which",
    #     "compare",
    #     "suitable",
    #     "invest",
    #     "advice",
    #     "suggest"
    # ]

    # is_recommendation = any(
    #     keyword in question.lower()
    #     for keyword in recommendation_keywords
    # )

    # search_results = []

    # if not is_recommendation:
    #     search_results = search_documents(question)
    search_results = search_documents(question)
    for doc in search_results:
        retrieved_docs[doc["filename"]] = doc
    
    #print("\nRetrieved documents:")    

    

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

        # if action == "ANSWER":

        #     return value

        # elif action == "ASKUSER":

        #     print()

        #     answer = input(value + "\n> ")

        #     history += (
        #         f"\nUser: {answer}"
        #     )

        #     question += (
        #         "\n"
        #         + answer
        #     )

        #     search_results = search_documents(answer)

        #     for doc in search_results:

        #         retrieved_docs[
        #             doc["filename"]
        #         ] = doc
        
        if action == "ANSWER":

            return {
                "action": "ANSWER",
                "message": value,
                "history": history
            }
        
        elif action == "ASKUSER":

            history += f"\nAssistant: {value}"

            return {
                "action": "ASKUSER",
                "message": value,
                "history": history
            }

        elif action == "SEARCH":

            history += f"\nAssistant performed SEARCH: {value}"

            search_results = search_documents(value)

            retrieved_docs.clear()

            for doc in search_results:

                retrieved_docs[
                    doc["filename"]
                ] = doc

            continue
    # return "Sorry, I couldn't find sufficient information."
    return {
    "action": "ANSWER",
    "message": "Sorry, I couldn't find sufficient information."
}

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