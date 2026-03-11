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

#  Product Dataset
data = {
     "Cargo Pants": "Durable pants with multiple pockets for functionality and style" ,
      "6-Pocket Pants": "Pants with two front, two back, and two side pockets.",
      "Cargo Joggers": "Pant that ombines the multi-pocket style with an elasticized waistband and cuffs.",
      "Tactical Cargo Pants": "Pants designed for durability, often featuring specialized pockets and, at times, zippers.",
     "Leather Crossbody Bag": "A sustainable, compact bag with an adjustable strap",
     "Polarized Sunglasses": "Stylish eyewear that reduces glare and protects eyes from UV rays",
     "Plant Grow Bags": "Breathable fabric pots for gardening on balconies or patios",
     "Water Pump Sprayer": "A handheld tool for watering plants or applying fertilizer."
}


#  Create Database dictionary
product_vectors = {}
for product, description in data.items():
    # Generate the embedding for the products
    embedding = get_embedding(description)
    # Store in the new dictionary
    product_vectors[product] = embedding

# Set User Input
user_description = "I want pants with multiple pockets"
user_vec = get_embedding(user_description)

# Find Closest products
similarities = {}
for product, vec in product_vectors.items():
    # Calculate similarity and store in the dictionary
    sim = cosine_similarity([user_vec], [vec])[0][0]# fetch the finl similarity score from the first row and first elemen
    similarities[product] = sim
#print top three similar products
ctr =1
for product,score  in similarities.items():    
    print(product)
    ctr+=1
    if ctr == 4:
        break
    
    
