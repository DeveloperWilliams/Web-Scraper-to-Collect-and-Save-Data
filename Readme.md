# Web Scraper

## Overview
This project is a web scraper built in Python. It fetches data from a specified website, parses the data to extract relevant information, and saves it into a CSV file. The project demonstrates skills in web scraping, data handling, and file operations.

## Features
- Fetches data from a specified website.
- Parses the data to extract relevant information.
- Saves the data into a CSV file.
- Handles errors gracefully.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DeveloperWilliams/Web-Scraper.git
    cd web_scraper
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the scraper:
    ```bash
    python scraper.py
    ```

2. The scraped data will be saved in `data/scraped_data.csv`.

## Configuration

- Modify the `url` variable in `scraper.py` to scrape data from a different website.
- Adjust the selectors in the `parse_content` function to match the structure of the target website.

## Dependencies

- `requests`
- `beautifulsoup4`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
