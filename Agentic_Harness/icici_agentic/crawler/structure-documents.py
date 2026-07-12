import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

RAW_DIR = "raw-pages"
OUTPUT_DIR = "../knowledge-base"

CHUNK_SIZE = 3000


PROMPT = """
You are creating a banking knowledge base from the official ICICI Bank website.

Convert the following document into ONE structured knowledge document.

Rules:

- Remove navigation
- Remove footer
- Remove cookie banners
- Remove duplicate information
- Keep only useful banking information
- Preserve important numbers, eligibility, fees, interest rates, processes, FAQs and benefits.

Output EXACTLY in this format.

TITLE:
SOURCE: ICICI Bank
CATEGORY:
TAGS:
CONTENT:
KEY POINTS:
URL:

DOCUMENT:

{document}
"""


def chunk_text(text, chunk_size=3000):
    """
    Split text into fixed-size chunks.
    """
    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start = end

    return chunks


Path(OUTPUT_DIR).mkdir(exist_ok=True)

for file in Path(RAW_DIR).glob("*.txt"):

    print(f"\nProcessing {file.name}")

    with open(file, encoding="utf-8") as f:

        raw = f.read()

    chunks = chunk_text(raw, CHUNK_SIZE)

    print(f"Chunks : {len(chunks)}")

    basename = file.stem

    for i, chunk in enumerate(chunks, start=1):

        print(f"  Chunk {i}")

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            temperature=0,

            messages=[
                {
                    "role": "user",
                    "content": PROMPT.format(
                        document=chunk
                    )
                }
            ]
        )

        kb = response.choices[0].message.content

        output_file = os.path.join(

            OUTPUT_DIR,

            f"{basename}_chunk_{i:03}.txt"

        )

        with open(output_file, "w", encoding="utf-8") as f:

            f.write(kb)

print("\nKnowledge Base Created.")