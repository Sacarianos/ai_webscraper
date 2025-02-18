import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching browser...")

    # Use the pre-installed Chrome and ChromeDriver in Streamlit Cloud
    chrome_path = "/usr/bin/google-chrome"
    chromedriver_path = "/usr/bin/chromedriver"

    options = Options()
    options.binary_location = chrome_path
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Launch Chrome with the correct paths
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    return str(body_content) if body_content else "No body content found"

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    return "\n".join(line.strip() for line in cleaned_content.split("\n") if line.strip())

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]
