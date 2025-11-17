import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"   # Public news site
OUTPUT_FILE = "headlines.txt"


def fetch_headlines():
    try:
        response = requests.get(URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # BBC uses <h2> tags for headlines
        headlines = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]

        return headlines

    except Exception as e:
        print("Error fetching headlines:", e)
        return []


def save_to_file(headlines):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")
    print(f"Saved {len(headlines)} headlines to {OUTPUT_FILE}")


def main():
    print("\nFetching top news headlines...\n")
    headlines = fetch_headlines()

    if headlines:
        for i, h in enumerate(headlines[:10], 1):   # Show first 10
            print(f"{i}. {h}")

        save_to_file(headlines)
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()