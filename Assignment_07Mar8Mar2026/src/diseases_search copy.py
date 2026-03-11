import openai
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
from get_embeddings import get_embedding
openai_key=''
file_path = Path('C:/Users/Lenovo/Documents/openrouter_key/ML_KEY.txt').expanduser()
try:
    with open(file_path, 'r') as file:
        # Your file operations here
        openai_key = file.read()
        #print("File opened successfully.")
except FileNotFoundError:
    print(f"Error: The file was not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
# Set OpenRouter API key
os.environ["OPENROUTER_API_KEY"] = openai_key
# 1. Setup OpenRouter
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_key,
)

# 2. Disease Dataset
data = {
    "Flu": "fever, cough, sore throat, fatigue",
    "Cold": "runny nose, sneezing, congestion",
    "COVID-19": "fever, cough, loss of taste, shortness of breath"
}


# 4. Create Database
disease_vectors = {disease: get_embedding(symptoms) for disease, symptoms in data.items()}

# 5. User Input
user_symptoms = "I have a high fever and a cough"
user_vec = get_embedding(user_symptoms)

# 6. Find Closest Disease
similarities = {
    disease: cosine_similarity([user_vec], [vec])[0][0]
    for disease, vec in disease_vectors.items()
}
best_match = max(similarities, key=similarities.get)
print(f"Closest disease: {best_match} (Score: {similarities[best_match]})")
