import os
import re

KNOWLEDGE_BASE = "knowledge-base"


def clean_filename(title):

    # Convert title to lowercase
    name = title.lower()

    # Replace special characters with underscore
    name = re.sub(
        r"[^a-z0-9]+",
        "_",
        name
    )

    # Remove extra underscores
    name = name.strip("_")

    # Limit filename length
    return name[:80]


used_names = set()


for filename in os.listdir(KNOWLEDGE_BASE):

    if not filename.endswith(".txt"):
        continue

    old_path = os.path.join(
        KNOWLEDGE_BASE,
        filename
    )

    title = None

    # Read TITLE from document
    with open(
        old_path,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            if line.startswith("TITLE:"):

                title = line.replace(
                    "TITLE:",
                    ""
                ).strip()

                break


    if not title:
        title = os.path.splitext(filename)[0]


    new_name = clean_filename(title)


    if not new_name:
        new_name = "document"


    # Handle duplicate titles
    base_name = new_name
    counter = 1

    while new_name in used_names:

        counter += 1

        new_name = (
            f"{base_name}_{counter}"
        )


    used_names.add(new_name)


    new_filename = new_name + ".txt"


    new_path = os.path.join(
        KNOWLEDGE_BASE,
        new_filename
    )


    os.rename(
        old_path,
        new_path
    )


    print(
        f"{filename}  -->  {new_filename}"
    )


print("\nRenaming completed.")