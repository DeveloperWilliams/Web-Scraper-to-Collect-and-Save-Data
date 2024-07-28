# web_scraper/scraper.py

import requests
from bs4 import BeautifulSoup
import csv
import os

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return None

def parse_content(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        data = []
        for item in soup.select('.item-selector'):
            title = item.select_one('.title-selector').get_text(strip=True)
            description = item.select_one('.description-selector').get_text(strip=True)
            data.append((title, description))
        return data
    except Exception as e:
        print(f"Error parsing content: {e}")
        return None

def save_to_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Description"])
            writer.writerows(data)
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def main():
    url = 'http://example.com/data'
    html_content = fetch_page(url)
    if html_content:
        data = parse_content(html_content)
        if data:
            save_to_csv(data, 'data/scraped_data.csv')

if __name__ == "__main__":
    main()
