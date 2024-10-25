import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import pandas as pd


class crawl_class:
    
    def __init__(self, logger, csvfilename):
        self.logger = logger
        self.csv_filename = csvfilename
    
    def is_valid_url(self, base_url, url):
        parsed = urlparse(url)
        return parsed.scheme in ['http', 'https'] and parsed.netloc == urlparse(base_url).netloc and not parsed.path.endswith(tuple(['.jpg', '.jpeg', '.png', '.gif']))

    def extract_sentences(self, text, keyword):
        sentences = text.split('.')
        return [sentence.strip() + '.' for sentence in sentences if keyword.lower() in sentence.lower()]

    def crawl_and_search(self, base_url, url, keyword, visited=set()):
        response = requests.get(url)
        if (response.status_code != 200) or (url in visited):
            return False
        self.logger.info(f"Visiting: {url}")  # Logging instead of printing
        visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        keyword_sentences = []

        sentences = self.extract_sentences(response.text, keyword)
        if sentences:
            for sentence in sentences:
                keyword_sentences.append({"URL": url, "Sentence": sentence, "Keyword": keyword})
        if len(keyword_sentences) > 0:
            self.save_to_csv(keyword_sentences)
        
        for link in links:
            full_link = urljoin(url, link['href'])
            if self.is_valid_url(base_url, full_link) and full_link not in visited:
                self.crawl_and_search(base_url, full_link, keyword, visited)
        
        return True

    def save_to_csv(self, data):
        exist_df = pd.read_csv(self.csv_filename)
        df = pd.DataFrame(data)
        new_df = pd.concat([exist_df, df], ignore_index=True)
        new_df.to_csv(self.csv_filename, index=False)
        self.logger.info(f"{len(df)} instances updated to {self.csv_filename}.")
