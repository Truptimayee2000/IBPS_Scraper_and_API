from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

URL = "https://www.ibps.in/index.php/recruitment/"

def fetch_ibps_jobs():
    print("🔍 Launching Chrome browser...")

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # comment out to debug visually
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(URL)

    try:
        # Wait for recruitment section to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.elementor-widget-container"))
        )
        print("✅ Recruitment content loaded.")
    except Exception:
        print("⚠️ Recruitment section not found.")
        driver.quit()
        return

    time.sleep(3)  # allow full content load
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    # Find all links inside recruitment section
    content_divs = soup.select("div.elementor-widget-container")
    jobs = []

    for div in content_divs:
        for link in div.find_all("a", href=True):
            title = link.get_text(strip=True)
            href = link["href"]

            # Clean relative URLs
            if href and not href.startswith("http"):
                href = f"https://www.ibps.in/{href.lstrip('/')}"

            if title:
                jobs.append({
                    "Job_Title": title,
                    "Location": "India",
                    "Publish_Date": "N/A",  # IBPS does not show publish date on page
                    "Link": href
                })

    if not jobs:
        print("⚠️ No job listings found.")
        return

    # Remove duplicates
    df = pd.DataFrame(jobs).drop_duplicates(subset=["Link"])

    # Save CSV
    output_path = os.path.join(os.getcwd(), "ibps_jobs.csv")
    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"✅ Saved {len(df)} job listings to: {output_path}")


if __name__ == "__main__":
    fetch_ibps_jobs()
