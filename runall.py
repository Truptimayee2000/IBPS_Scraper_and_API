import subprocess
import sys
import os

# -----------------------------
# Step 0: Set Django settings
# -----------------------------
os.environ['DJANGO_SETTINGS_MODULE'] = 'ibps_api.settings'
sys.path.append(os.path.join(os.getcwd(), 'ibps_apis'))

# Step 0.5: Create admin user automatically (username + password only)
print("🛠 Creating demo admin user (if not exists)...")
create_user_script = """
from django.contrib.auth.models import User

username = 'admin'
password = '12345'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email='', password=password)
    print("✅ Admin user created")
else:
    print("ℹ Admin user already exists")
"""

subprocess.run(
    [sys.executable, "manage.py", "shell", "-c", create_user_script],
    cwd=os.path.join(os.getcwd(), "ibps_apis"),
    check=True
)

# -----------------------------
# Step 1: Run the scraper
# -----------------------------
print("🚀 Running IBPS scraper...")
scraper_path = os.path.join("ibps_scraper", "ibps_scraper.py")
subprocess.run([sys.executable, scraper_path], check=True)
print("✅ Scraper finished successfully.")

# -----------------------------
# Step 2: Start Django server
# -----------------------------
print("🚀 Starting Django development server...")
manage_path = os.path.join("ibps_apis", "manage.py")
subprocess.run([sys.executable, manage_path, "runserver"], check=True)
