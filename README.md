# task3.python
Web Scraper for News Headlines

A Python-based web scraping tool that automatically fetches the latest news headlines from a public news website and saves them into a text file.


---

🎯 Objective

To build a simple web scraper that collects top news headlines using:

requests → to fetch webpage HTML

BeautifulSoup → to parse and extract headline tags

open() → to save headlines into a .txt file



---

🛠 Technologies & Libraries Used

Python 3

requests

BeautifulSoup (bs4)

File handling


Install required packages:

pip install requests beautifulsoup4


---

📂 Project Structure

news_scraper/
 ├── scraper.py
 ├── headlines.txt   ← Auto-generated
 └── README.md


---

🚀 Features

Fetches real-time news headlines

Parses HTML safely using BeautifulSoup

Extracts all <h2> tags (commonly used for headlines)

Prints top 10 headlines in the terminal

Saves ALL scraped headlines into headlines.txt

Simple, clean, and functional script structure



---

▶ How to Run the Script

1. Open terminal inside the project folder


2. Run:



python scraper.py

3. The program will show:



Fetching top news headlines...
1. Headline 1
2. Headline 2
...
Saved X headlines to headlines.txt

4. Check the auto-created file:



headlines.txt

It will contain all the scraped headlines.


---

🧠 How It Works (Summary)

1. Sends a request to a news website (BBC News).


2. Downloads the webpage HTML.


3. Uses BeautifulSoup to parse the HTML.


4. Extracts all <h2> elements (headlines).


5. Stores them in a list.


6. Writes each headline to a .txt file.




---

✨ Learning Outcomes

Understanding of web scraping workflow

Working with HTTP requests

HTML parsing using BeautifulSoup

Extracting elements from DOM

Automating text file creation

Python loops & data handling



---
