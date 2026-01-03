import requests
from bs4 import BeautifulSoup
import re


class SECFilingProcessor:
    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def download_filing(self, url: str) -> str:
        """
        Download SEC filing HTML content from URL
        """
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.text

    def clean_html(self, html_content: str) -> str:
        """
        Convert HTML to clean plain text
        """
        soup = BeautifulSoup(html_content, "html.parser")

        # Remove scripts and styles
        for tag in soup(["script", "style"]):
            tag.decompose()

        text = soup.get_text(separator=" ")

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text

    def process_filing(self, url: str) -> str:
        """
        Full pipeline: download + clean
        """
        html = self.download_filing(url)
        clean_text = self.clean_html(html)
        return clean_text
