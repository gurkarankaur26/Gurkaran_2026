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
#  Setup OpenRouter
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_key,
)

#  Disease Dataset
data = {
    "Flu": "fever, cough, sore throat, fatigue",
    "Cold": "runny nose, sneezing, congestion",
    "Dengue": "rash, joint pain",
    "Malaria": "fever, chills",
    "COVID-19": "fever, cough, loss of taste, shortness of breath"
}


#  Create Database dictionary
disease_vectors = {}
for disease, symptoms in data.items():
    # Generate the embedding for the symptoms
    embedding = get_embedding(symptoms)
    # Store in the new dictionary
    disease_vectors[disease] = embedding

# Set User Input
user_symptoms = "I have a high fever, chills and a cough"
user_vec = get_embedding(user_symptoms)

#  Find Closest Disease
similarities = {}
for disease, vec in disease_vectors.items():
    # Calculate similarity and store in the dictionary
    sim = cosine_similarity([user_vec], [vec])[0][0]# fetch the finl similarity score from the first row and first elemen
    similarities[disease] = sim
    
best_match = None
highest_score = -1.0 # Start with a score lower than any possible cosine similarity (-1 to 1)

for disease, score in similarities.items():
    if score > highest_score:
        highest_score = score
        best_match = disease
print(f"Closest disease: {best_match} (Score: {similarities[best_match]})")
    
    
