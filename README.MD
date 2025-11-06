## IBPS Job Scraper & Django API
## Overview

This project automatically scrapes job listings from the IBPS Recruitment
 website, stores them in a CSV file, and provides a Django-based web interface and REST API to view the jobs. JWT authentication is used for secure API access.

## Features

* Scrapes job listings (Job Title, Location, Publish Date, Link) from IBPS website.

* Saves jobs to ibps_jobs.csv.

* Django web interface to view jobs.

* JWT-protected API endpoint.

* Admin login: username=admin, password=12345 (auto-created).

* Fully automated script to run scraper and start Django server.


## Setup & Installation

1. Clone the repository:
```bash
    git clone <repository_url>
    cd IBPS_Scraper_and_API
```

2. Create a virtual environment and activate it:
```bash
    python -m venv venv
    venv\Scripts\activate 
```
3. Install dependencies:
```bash
    pip install -r ibps_scraper/requirements.txt
    pip install -r ibps_apis/requirements.txt
```
## Usage

1. Run the all-in-one script:
```bash
    python runall.py
```

This will:

* Create the admin user (admin / 12345) if it doesn’t exist.

* Run the IBPS scraper and save jobs to ibps_jobs.csv.

* Start the Django development server.

2. Open your browser:

* Login page: http://127.0.0.1:8000/

* Username: admin

* Password: 12345

* Jobs page: http://127.0.0.1:8000/jobs/

* JWT API endpoints:

* Obtain token: /api/token/

* Refresh token: /api/token/refresh/
