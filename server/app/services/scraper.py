import requests
from bs4 import BeautifulSoup


def scrape_company_website(url: str):

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title found"

        paragraphs = soup.find_all("p")

        content = " ".join(
            [p.get_text(strip=True) for p in paragraphs[:10]]
        )

        return {
            "success": True,
            "title": title,
            "content": content[:3000]
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }