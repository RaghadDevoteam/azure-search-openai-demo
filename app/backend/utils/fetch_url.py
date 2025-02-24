import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    """Fetches and extracts text from a webpage."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        text = " ".join([p.get_text() for p in soup.find_all("p")])  # Extract paragraphs
        return text.strip()[:5000]  # Limit characters to avoid exceeding GPT token limits
    except Exception as e:
        return f"Error fetching URL: {e}"

   
   
   
text = extract_text_from_url(url)
index_url_data(url, text)

text = extract_text_from_url(url)
store_url_in_db(url, text)
