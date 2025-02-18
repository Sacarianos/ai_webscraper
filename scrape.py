import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup


def scrape_website(website):
    print("Launching browser...")

    chrome_driver_path = "./chromedriver"
    options = webdriver.ChromeOptions()

    # Enable headless mode
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")  
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage") 

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(5)

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    # Extract the body of the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content is not None:
        return str(body_content)
    return "No body content found"

def clean_body_content(body_content):
    
    soup = BeautifulSoup(body_content, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.split("\n") if line.strip())
    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]