LinkedIn Scraper

A Python-based scraper using Playwright to extract posts and related data from LinkedIn profiles. The project supports scraping LinkedIn posts from a specific profile URL using an automated browser setup and handles data storage.

Features

Automated Login: Uses Playwright for automated browser interactions.
Profile Post Scraping: Extract posts from a given LinkedIn profile.
Data Handling: Stores extracted data in a specified data directory.
Redis Integration: Uses Redis for task handling or caching if needed.

Prerequisites

Before you start, make sure you have the following installed on your machine:

Docker and Docker Compose (for containerized setup)
Python 3.12 (if running locally without Docker)

Setup

1. Clone the Repository
   
git clone https://github.com/your-username/linkedin-scraper.git
cd linkedin-scraper

2. Environment Variables
   
Create a .env file in the root directory to store your LinkedIn credentials:

LINKEDIN_EMAIL=your-email@example.com
LINKEDIN_PASSWORD=your-password
Replace your-email@example.com and your-password with your LinkedIn login credentials.

3. Docker Setup
   
Build and run the Docker container:

docker build -t linkedin-scraper .
docker run -d --name linkedin_scraper_container linkedin-scraper
This will:
Build the Docker image with the necessary dependencies.
Start the container, which includes Redis and the Playwright-based scraping service.

4. Running the Scraper'
   
The scraper starts automatically when the Docker container is run. It will begin scraping the LinkedIn profile specified in src/main.py.

5. Data Output
   
Scraped data will be saved in the /app/data directory inside the Docker container. To access this data:

docker cp linkedin_scraper_container:/app/data ./data
Local Setup (Without Docker)
If you prefer to run the scraper locally without Docker:

Install Python Dependencies:

Make sure you have poetry installed. Then run:

poetry install
Install Playwright Browsers:

Run the following command to install Playwright and its required browsers:

poetry run playwright install
Start Redis:

Install Redis locally and start the Redis server:

redis-server
Run the Application:

Run the scraper using:

python src/main.py
Configuration
src/main.py
In the src/main.py file, specify the LinkedIn profile URL you wish to scrape:

python

PROFILE_URL = "https://www.linkedin.com/in/your-profile-url/recent-activity/all/"
Replace your-profile-url with the LinkedIn profile URL of the person whose posts you want to scrape.

Adjusting Scroll Behavior
The ProfileHandler class in src/handlers/profile_handler.py controls the scrolling behavior. Adjust the number of scrolls or wait time as needed:

Project Structure

.
├── Dockerfile                # Docker configuration for building the scraper environment
├── pyproject.toml            # Poetry configuration for managing dependencies
├── poetry.lock               # Lockfile for Poetry dependencies
├── src/
│   ├── main.py               # Main entry point for running the scraper
│   ├── handlers/
│   │   ├── profile_handler.py # Handles scraping of LinkedIn profiles
│   │   └── post_handler.py    # Handles extraction of post details
│   ├── data/                 # Directory for storing scraped data
├── .env                      # Environment variables for LinkedIn credentials
└── README.md                 # This file
