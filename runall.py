import subprocess
import sys
import os

# Step 1: Run the scraper
print("🚀 Running IBPS scraper...")
scraper_path = os.path.join("ibps_scraper", "ibps_scraper.py")
subprocess.run([sys.executable, scraper_path], check=True)
print("✅ Scraper finished successfully.")

# Step 2: Start Django server
print("🚀 Starting Django development server...")
manage_path = os.path.join("ibps_apis", "manage.py")
subprocess.run([sys.executable, manage_path, "runserver"], check=True)
