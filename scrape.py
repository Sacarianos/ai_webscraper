import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import dotenv

dotenv.load_dotenv()


browserlessapi = os.getenv("BROWSERLESS_API")
REMOTE_SELENIUM_URL = f"https://chrome.browserless.io/webdriver?token={browserlessapi}"


def get_driver():
    """Initialize and cache a remote Selenium WebDriver."""
    options = Options()
    options.add_argument("--headless")   
    options.add_argument("--no-sandbox")
    options.set_capability('browserless:token', browserlessapi)

    driver = webdriver.Remote(command_executor='https://chrome.browserless.io/webdriver', options=options)
    return driver

def scrape_website(url):
    """Scrapes the given URL and returns its HTML content."""
    driver = get_driver()
    driver.get(url)
    
    html = driver.page_source
    driver.quit()
    return html
    

def extract_body_content(html_content):
    """Extracts the body content from the HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    return str(soup.body) if soup.body else "No body content found"

def clean_body_content(body_content):
    """Cleans the extracted body content by removing scripts and styles."""
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    return "\n".join(line.strip() for line in cleaned_content.split("\n") if line.strip())

def split_dom_content(dom_content, max_length=6000):
    """Splits the HTML content into smaller chunks for processing."""
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
