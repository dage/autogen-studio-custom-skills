# filename: skills.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class WebScraper:
    """
    A class that encapsulates the functionality to scrape a single webpage
    and return its full text content.
    """

    def fetch_full_text(self, url: str) -> str:
        """
        Fetches the full text content of a webpage given its URL using Selenium.

        Parameters:
        - url (str): The URL of the webpage.

        Returns:
        - The full text content of the webpage.
        """
        try:
            options = Options()
            options.headless = True
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            options.page_load_strategy = 'eager'  # Wait for the DOMContentLoaded event

            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            driver.set_page_load_timeout(10)  # Set a timeout for page load
            driver.get(url)
            
            # Retry mechanism
            retries = 3
            for _ in range(retries):
                try:
                    full_text = driver.find_element(By.TAG_NAME, 'body').text
                    break
                except Exception as e:
                    print(f"Retrying due to error: {e}")
                    time.sleep(2)
            else:
                full_text = ""

            driver.quit()
            return full_text
        except Exception as e:
            print(f"An error occurred while fetching full text: {e}")
            return ""

# Example usage
# scraper = WebScraper()
# full_text = scraper.fetch_full_text("https://example.com")
# print(full_text)