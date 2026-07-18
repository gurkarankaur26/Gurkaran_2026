import json
import re

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from icici_agentic.agentic import run_agent


def home(request):
    return render(request, "chatbot/index.html")


@csrf_exempt
def chat(request):

    if request.method == "POST":

        data = json.loads(request.body)

        question = data.get("message", "").strip()

        # Retrieve conversation history
        history = request.session.get("history", "")

        # If this is a reply to a clarification question,
        # combine it with the original question.
        if request.session.get("pending_question"):

            question = (
                request.session["pending_question"]
                + "\n"
                + question
            )

        # Add current user message to history
        history += f"\nUser: {question}"

        response = run_agent(
            question,
            history
        )

        action = response["action"]
        answer = response["message"]

        # Clean response
        answer = re.sub(r"ACTION\s*\d*", "", answer)
        answer = answer.replace("ANSWER:", "").strip()
        answer = answer.replace("ASKUSER:", "").strip()

        # Get updated history from agent
        history = response.get("history", history)

        if action == "ASKUSER":

            # Remember the original question
            request.session["pending_question"] = question

            # Save assistant question in history
            history += f"\nAssistant: {answer}"

            request.session["history"] = history

        elif action == "ANSWER":

            # Conversation completed
            request.session.pop("history", None)
            request.session.pop("pending_question", None)

        return JsonResponse({
            "action": action,
            "answer": answer
        })

    return JsonResponse(
        {"error": "Invalid request"},
        status=400
    )