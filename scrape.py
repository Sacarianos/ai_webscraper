import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Install Chrome and ChromeDriver dynamically
def install_chrome():
    if not os.path.exists("/usr/bin/google-chrome"):
        subprocess.run(
            "wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
            shell=True,
            check=True
        )
        subprocess.run("dpkg -i google-chrome-stable_current_amd64.deb || apt --fix-broken install -y", shell=True, check=True)
        subprocess.run("rm google-chrome-stable_current_amd64.deb", shell=True, check=True)

def install_chromedriver():
    if not os.path.exists("/usr/bin/chromedriver"):
        subprocess.run("apt update && apt install -y chromium-chromedriver", shell=True, check=True)

def scrape_website(website):
    print("Installing Chrome and ChromeDriver...")
    install_chrome()
    install_chromedriver()

    print("Launching browser...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use dynamically installed ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(website)
        print("Page loaded...")
        time.sleep(5)
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
