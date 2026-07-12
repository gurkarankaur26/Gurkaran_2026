import os
import json
import time
import hashlib
import requests
import trafilatura

from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# ----------------------------------------
# CONFIG
# ----------------------------------------

URLS_FILE = "urls.json"

OUTPUT_DIR = "raw-pages"

REQUEST_TIMEOUT = 30

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
}

# ----------------------------------------
# HELPERS
# ----------------------------------------

def filename_from_url(url):

    parsed = urlparse(url)

    name = parsed.path.strip("/")

    if not name:
        name = "home"

    name = name.replace("/", "_")

    file_hash = hashlib.md5(url.encode()).hexdigest()[:8]

    return f"{name}_{file_hash}.txt"


def download_page(url):

    response = requests.get(
        url,
        timeout=REQUEST_TIMEOUT,
        headers=HEADERS
    )

    response.raise_for_status()

    return response.text


def get_title(html):

    soup = BeautifulSoup(html, "html.parser")

    if soup.title and soup.title.string:
        return soup.title.string.strip()

    return "Untitled"


def extract_text(html):

    text = trafilatura.extract(
        html,
        include_tables=True,
        include_comments=False
    )

    if text is None:
        return ""

    return text.strip()


# ----------------------------------------
# MAIN
# ----------------------------------------

Path(OUTPUT_DIR).mkdir(exist_ok=True)

with open(URLS_FILE, "r", encoding="utf-8") as f:

    urls = json.load(f)

print(f"\nFound {len(urls)} URLs\n")

saved = 0
failed = 0
skipped = 0

for i, url in enumerate(urls, start=1):

    print(f"[{i}/{len(urls)}] {url}")

    try:

        html = download_page(url)

        title = get_title(html)

        text = extract_text(html)

        if len(text) < 200:

            skipped += 1
            print("  -> skipped")
            continue

        filename = filename_from_url(url)

        filepath = os.path.join(
            OUTPUT_DIR,
            filename
        )

        with open(filepath, "w", encoding="utf-8") as f:

            f.write(f"TITLE: {title}\n")
            f.write(f"URL: {url}\n\n")
            f.write(text)

        saved += 1

        print(f"  -> saved {filename}")

        time.sleep(0.5)

    except Exception as e:

        failed += 1

        print(f"  -> ERROR: {e}")

print("\n----------------------------")
print(f"Saved   : {saved}")
print(f"Skipped : {skipped}")
print(f"Failed  : {failed}")
print("----------------------------")