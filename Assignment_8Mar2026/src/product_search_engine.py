import openai
import os
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import kagglehub 
from kagglehub import KaggleDatasetAdapter
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

#  Product Dataset:# download dataset
path = kagglehub.dataset_download(
   "PromptCloudHQ/flipkart-products"
)
file_path = os.path.join(
    path,
    "flipkart_com-ecommerce_sample.csv"
)
df = pd.read_csv(file_path)
continue_input = "Y"
while (continue_input.upper() =="Y" or continue_input.upper() == "YES"):
    # Set User Input
    user_description = input("Please enter the product you are looking for:  ")
    user_vec = get_embedding(user_description)    
    #Filter the dataset as per the user input
    data = df[df["description"].str.contains(user_description, case=False, na=False)]   
    if not data.empty:      
        #  Create Database dictionary
        product_vectors = {}
        for name, description in zip(data["product_name"], data["description"]):
            text = f"{name}. Category: {description}"
            embedding = get_embedding(text)
            product_vectors[name] = embedding     
            
        # Find Closest products
        similarities = {}
        for product, vec in product_vectors.items():
            # Calculate similarity and store in the dictionary
            sim = cosine_similarity([user_vec], [vec])[0][0]# fetch the finl similarity score from the first row and first elemen
            similarities[product] = sim
            
        #sorted the products in the descending order of cosine similarity
        sorted_products = sorted(
            similarities.items(),
            key=lambda x: x[1],
            reverse=True
        )
         #print top three similar products
        for product, score in sorted_products[:3]:
                print(product, score)
     
    else:
        print("Sorry!! Product not found") 
         
    continue_input = input("Do you want to conitune search? Enter Y/N:  ")
        
