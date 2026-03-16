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

#  Product Dataset
# data = {
#      "Cargo Pants": "Durable pants with multiple pockets for functionality and style" ,
#       "6-Pocket Pants": "Pants with two front, two back, and two side pockets.",
#       "Cargo Joggers": "Pant that ombines the multi-pocket style with an elasticized waistband and cuffs.",
#       "Tactical Cargo Pants": "Pants designed for durability, often featuring specialized pockets and, at times, zippers.",
#      "Leather Crossbody Bag": "A sustainable, compact bag with an adjustable strap",
#      "Polarized Sunglasses": "Stylish eyewear that reduces glare and protects eyes from UV rays",
#      "Plant Grow Bags": "Breathable fabric pots for gardening on balconies or patios",
#      "Water Pump Sprayer": "A handheld tool for watering plants or applying fertilizer."
# }
# Set the path to the file you'd like to load
# download dataset
path = kagglehub.dataset_download(
   "PromptCloudHQ/flipkart-products"
)

# p1 = r"C:\Users\Lenovo\.cache\kagglehub\datasets\PromptCloudHQ\flipkart-products\versions\1"
# print(os.listdir(p1))

# p2 = os.path.join(p1, "home")
# print(os.listdir(p2))

# p3 = os.path.join(p2, "sdf")
# print(os.listdir(p3))



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

    # Use head() to get the first 1000 rows
    #data = df.head(100)
    data = df[df["description"].str.contains(user_description, case=False, na=False)]

    #  Create Database dictionary
    product_vectors = {}

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
    #print top three similar products
    sorted_products = sorted(
        similarities.items(),
        key=lambda x: x[1],
        reverse=True
    )
    if sorted_products is None:
        print("Sorry!! Product not found")
    else:
        for product, score in sorted_products[:3]:
            print(product, score)
        
    continue_input = input("Do you want to conitune search? Enter Y/N:  ")
        
