from openai import OpenAI
import os
from pathlib import Path
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

# Initialize client with OpenRouter base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

def get_embedding(prompt, model="text-embedding-3-small"):
    try:
        response = client.embeddings.create(
            model=model,
            input=prompt
        )
        return response.data[0].embedding
    except Exception as e:
        print("Error fetching embedding:", e)

# Example usage
if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    embedding = get_embedding(text)

    if embedding:
        print(f"Embedding length: {len(embedding)}")
        print(embedding[:10])  # first 10 values