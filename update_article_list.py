import re

README_FILE = 'README.md'

# List of items (label and link)
articles = [
    "- [Research Institute Andishe Online Germany (AOG)](https://aogdata.wikibase.cloud/wiki/Item:Q12)",
    "- [Faramarz Tabesh](https://aogdata.wikibase.cloud/wiki/Item:Q10)",
    "- [Appearance of instinctive characteristics – Step 1: New Concepts and Ideas](https://aogdata.wikibase.cloud/wiki/Item:Q2)",
    "- [Who´s Elite](https://aogdata.wikibase.cloud/wiki/Item:Q3)"
]

def update_readme(articles):
    # Read README.md content
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Join the article list into a single block
    new_block = '\n'.join(articles)

    # Replace the content between the markers
    updated = re.sub(
        r'<!-- ARTICLE LIST START -->(.*?)<!-- ARTICLE LIST END -->',
        f'<!-- ARTICLE LIST START -->\n{new_block}\n<!-- ARTICLE LIST END -->',
        content,
        flags=re.DOTALL
    )

    # Write the updated content back to README.md
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(updated)

    print("✅ README.md updated successfully.")

# Run the update
if __name__ == "__main__":
    update_readme(articles)

