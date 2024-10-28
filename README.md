# LinkedIn Scraper

# A Python-based scraper using Playwright to extract posts and related data from LinkedIn profiles. This project automates LinkedIn profile scraping, manages data storage, and optionally uses Redis for task handling or caching.

# Features:
# - Automated Login: Uses Playwright for automated browser interactions.
# - Profile Post Scraping: Extracts posts from a given LinkedIn profile URL.
# - Data Handling: Stores extracted data in a specified data directory.
# - Redis Integration: Supports Redis for task handling or caching if needed.

# Prerequisites:
# Ensure you have the following installed:
# - Docker and Docker Compose (for a containerized setup)
# - Python 3.12 (if running locally without Docker)

# Setup:
# 1. Clone the Repository
git clone https://github.com/your-username/linkedin-scraper.git
cd linkedin-scraper

# 2. Configure Environment Variables
echo "LINKEDIN_EMAIL=your-email@example.com" >> .env
echo "LINKEDIN_PASSWORD=your-password" >> .env

# 3. Docker Setup
# Build and run the Docker container
docker build -t linkedin-scraper .
docker run -d --name linkedin_scraper_container linkedin-scraper

# This will:
# - Build the Docker image with all dependencies.
# - Start the container, which includes Redis and the Playwright-based scraping service.

# 4. Running the Scraper
# The scraper starts automatically when the Docker container runs. It will begin scraping the LinkedIn profile specified in `src/main.py`.

# 5. Accessing Scraped Data
# Scraped data will be saved in the `/app/data` directory inside the Docker container. To access this data:
docker cp linkedin_scraper_container:/app/data ./data

# Local Setup (Without Docker)
# If you prefer running the scraper locally:

# Install Dependencies
# Make sure you have Poetry installed, then run:
poetry install

# Install Playwright Browsers
# Install Playwright and its required browsers:
poetry run playwright install

# Start Redis
# Install Redis locally and start the Redis server:
redis-server &

# Run the Scraper
python src/main.py

# Configuration
# LinkedIn Profile URL
# In the `src/main.py` file, specify the LinkedIn profile URL you wish to scrape:
echo 'PROFILE_URL = "https://www.linkedin.com/in/your-profile-url/recent-activity/all/"' >> src/main.py

# Replace `your-profile-url` with the LinkedIn profile URL of the person whose posts you want to scrape.

# Adjusting Scroll Behavior
# The `ProfileHandler` class in `src/handlers/profile_handler.py` controls the scrolling behavior. Adjust the number of scrolls or wait time as needed.

# Project Structure
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
└── README.md                 # Project documentation (this file)


