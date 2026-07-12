import json
import os
import time
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

OUTPUT_FILE = "urls.json"

SEARCH_QUERIES = [

    # Accounts
    "ICICI savings account site:icicibank.com",
    "ICICI salary account site:icicibank.com",
    "ICICI current account site:icicibank.com",

    # Deposits
    "ICICI fixed deposit site:icicibank.com",
    "ICICI recurring deposit site:icicibank.com",

    # Credit Cards
    "ICICI credit cards site:icicibank.com",
    "ICICI Amazon Pay Credit Card site:icicibank.com",
    "ICICI Coral Credit Card site:icicibank.com",
    "ICICI Rubyx Credit Card site:icicibank.com",
    "ICICI Sapphiro Credit Card site:icicibank.com",

    # Loans
    "ICICI personal loan site:icicibank.com",
    "ICICI home loan site:icicibank.com",
    "ICICI car loan site:icicibank.com",
    "ICICI two wheeler loan site:icicibank.com",
    "ICICI education loan site:icicibank.com",
    "ICICI gold loan site:icicibank.com",

    # Insurance
    "ICICI insurance site:icicibank.com",

    # Investments
    "ICICI mutual funds site:icicibank.com",
    "ICICI SIP site:icicibank.com",
    "ICICI demat account site:icicibank.com",
    "ICICI trading account site:icicibank.com",

    # Forex
    "ICICI forex site:icicibank.com",

    # NRI
    "ICICI NRI banking site:icicibank.com",

    # Business Banking
    "ICICI business banking site:icicibank.com",

    # FASTag
    "ICICI FASTag site:icicibank.com",

    # iMobile
    "ICICI iMobile site:icicibank.com",

    # Internet Banking
    "ICICI internet banking site:icicibank.com"
]

urls = set()

for query in SEARCH_QUERIES:

    print(f"\nSearching: {query}")

    try:

        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=15
        )

        results = response.get("results", [])

        print(f"Found {len(results)} results")

        for item in results:

            url = item.get("url")

            if not url:
                continue

            if "icicibank.com" not in url:
                continue

            if url.endswith(".pdf"):
                continue

            urls.add(url)

        time.sleep(1)

    except Exception as e:

        print(e)

print("\n--------------------------------")

print(f"Unique URLs : {len(urls)}")

urls = sorted(list(urls))

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

    json.dump(urls, f, indent=4)

print(f"Saved {OUTPUT_FILE}")