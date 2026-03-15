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
# Setup OpenRouter
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=openai_key,
)

#function to create dictionary of page name and its content
def create_data_dictionary_from_files(directory_path):
    data = {}
    
    for filename in os.listdir(directory_path):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        
        # Check if the path points to a file and ends with .txt (optional)
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            try:
                # Open and read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Add to the dictionary with the filename as the key
                data[filename] = content
            except IOError as e:
                print(f"Error reading file {filename}: {e}")
                
    return data


#
data =create_data_dictionary_from_files("pages")
#  Create Database
phrase_vectors = {}
for page_name, page_content in data.items():
    # Generate the embedding for the page content
    embedding = get_embedding(page_content)
    # Store in the new dictionary
    phrase_vectors[page_name] = embedding

# Set User Input
user_description = "Ecosystems are constantly evolving, reacting to both natural and human-induced changes."
user_vec = get_embedding(user_description)

# Find Closest page
similarities = {}
for page_name, vec in phrase_vectors.items():
    # Calculate similarity and store in the dictionary
    sim = cosine_similarity([user_vec], [vec])[0][0]# fetch the finl similarity score from the first row and first elemen
    similarities[page_name] = sim
best_match = None
highest_score = -1.0 # Start with a score lower than any possible cosine similarity (-1 to 1)

for page_name, score in similarities.items():
    if score > highest_score:
        highest_score = score
        best_match = page_name
print(f"Closest page: {best_match} (Score: {similarities[best_match]})")
    