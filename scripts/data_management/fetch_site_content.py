import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
import pandas as pd
import openai


class crawl_class:
    
    def __init__(self, logger, csvfilename, overwrite=False, previous_logfile_path=None):
        self.logger = logger
        self.csv_filename = csvfilename
        self.visited = set()
        self.overwriteexistcsv = overwrite
        if previous_logfile_path is not None:
            self.visited, self.last_visited_url = self.extract_urls_from_logfile(previous_logfile_path)
            self.previous_logfile_path = previous_logfile_path
    
    def extract_urls_from_logfile(self, logfile_path):
        url_pattern = re.compile(r'Visiting: (\S+)')
        visited_urls = set()
        last_visited_url = None
        
        with open(logfile_path, 'r') as file:
            for line in file:
                match = url_pattern.search(line)
                if match:
                    # Extract the URL from the regex match
                    url = match.group(1)
                    # Add to set of visited URLs
                    visited_urls.add(url)
                    # Update the last visited URL
                    last_visited_url = url

        return visited_urls, last_visited_url
    
    def is_valid_url(self, base_url, url):
        parsed = urlparse(url)
        return parsed.scheme in ['http', 'https'] and parsed.netloc == urlparse(base_url).netloc and not parsed.path.endswith(tuple(['.jpg', '.jpeg', '.png', '.gif']))

    def clean_html_content(self, table_elements):
        cleaned_table_contents = []
        for each_e in table_elements:
            text_content = each_e.text.strip() # Get text content and strip whitespace
            sentences = re.split(r'[.!?]\s*', text_content)
            cleaned_sentences = []
            for sentence in sentences:
                clean_sentence = re.sub(r'\s+', ' ', sentence)
                clean_sentence = clean_sentence.replace('\n', ' ').strip() # Replace newline characters and strip leading/trailing spaces
                if len(clean_sentence) > 0:
                    cleaned_sentences.append(clean_sentence)
            cleaned_table_contents.append(''.join(cleaned_sentences))
        return cleaned_table_contents
    
    def extract_sentences(self, table_elements, keyword):
        filtered_contents = []
        for each_e in table_elements:
            text_content = each_e.text.strip()  # Get text content and strip whitespace
            if keyword.lower() in text_content.lower():  # Check if keyword is in text content
                sentences = re.split(r'[.!?]\s*', text_content)
                matching_sentences = []
                for sentence in sentences:
                    clean_sentence = re.sub(r'\s+', ' ', sentence)
                    clean_sentence = clean_sentence.replace('\n', ' ').strip()  # Replace newline characters and strip leading/trailing spaces
                    if keyword in clean_sentence.lower():
                        matching_sentences.append(clean_sentence)
                filtered_contents += matching_sentences  # Append the text content only
        return filtered_contents

    def crawl_and_search(self, base_url, url, keyword, url_filter):
        response = requests.get(url)
        if (response.status_code != 200):
            return {"status": False, "last_visit": url, "comment": f"failed to reach {url}"}
        elif url in self.visited:
            return {"status": False, "last_visit": url, "comment": f"already searched the {url}"}
        self.logger.info(f"Visiting: {url}")  # Logging instead of printing
        self.visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        links = [link['href'] for link in links if url_filter in link['href']]
        
        for link in links:
            full_link = urljoin(base_url, link)
            suburl_response = requests.get(full_link)
            if (suburl_response.status_code != 200):
                self.logger.info(f"Failed to access {full_link}")
            self.logger.info(f"Visiting: {full_link}")
            keyword_sentences = []
            if self.is_valid_url(base_url, full_link) and full_link not in self.visited:
                suburl_soup = BeautifulSoup(suburl_response.text, 'html.parser')
                table_elements = suburl_soup.find_all('td')
                sentences = self.extract_sentences(table_elements, keyword)
                if sentences:
                    for sentence in sentences:
                        keyword_sentences.append({"URL": full_link, "Sentence": sentence, "Keyword": keyword})
            if len(keyword_sentences) > 0:
                self.save_to_csv(keyword_sentences)
        return {"status": True, "last_visit": full_link, "comment": "success"}

    def fetch_by_chatgpt(self, base_url, url, keywords, url_filter):
        response = requests.get(url)
        if (response.status_code != 200):
            return {"status": False, "last_visit": url, "comment": f"failed to reach {url}"}
        elif url in self.visited:
            return {"status": False, "last_visit": url, "comment": f"already searched the {url}"}
        self.logger.info(f"Visiting: {url}")  # Logging instead of printing
        self.visited.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        links = [link['href'] for link in links if url_filter in link['href']]
        for link in links:
            full_link = urljoin(base_url, link)
            suburl_response = requests.get(full_link)
            if (suburl_response.status_code != 200):
                self.logger.info(f"Failed to access {full_link}")
            self.logger.info(f"Visiting: {full_link}")
            keyword_sentences = []
            if self.is_valid_url(base_url, full_link) and full_link not in self.visited:
                suburl_soup = BeautifulSoup(suburl_response.text, 'html.parser')
                table_elements = suburl_soup.find_all('td')
                sentences = self.clean_html_content(table_elements)
                client = openai.OpenAI( api_key="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",)
                response = client.chat.completions.create(model="gpt-3.5-turbo", # model to use from Models Tab
                        messages = [
                                {
                                    "role": "system",
                                    "content": f"Imagine, you are you are educator investigating any evidences in course description, which embed educate students to consider accessibility."
                                },
                                {
                                    "role": "user",
                                    "content": f"Extract sentences related to keywords {keywords} from HTML contents: {'|'.join(sentences)}"
                                },
                                {
                                    "role": "user",
                                    "content": f"Organise extracted sentences by number 1, 2, 3, etc..."
                                }
                            ]
                )
                
                if sentences:
                    for sentence in sentences:
                        keyword_sentences.append({"URL": full_link, "Sentence": response, "Keywords": ''.join(keywords)})
            if len(keyword_sentences) > 0:
                self.save_to_csv(keyword_sentences)
        return {"status": True, "last_visit": full_link, "comment": "success"}
    
    def save_to_csv(self, data):
        exist_df = pd.read_csv(self.csv_filename)
        df = pd.DataFrame(data)
        new_df = pd.concat([exist_df, df], ignore_index=True)
        new_df.to_csv(self.csv_filename, index=False)
        self.logger.info(f"{len(df)} instances updated to {self.csv_filename}.")


class mining_google_scholar_workcloud:
    pass