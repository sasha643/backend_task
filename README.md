# LinkedIn Scraper

echo "A Python-based scraper using Playwright to extract posts and related data from LinkedIn profiles. This project automates LinkedIn profile scraping, manages data storage, and optionally uses Redis for task handling or caching."

echo ""
echo "Features:"
echo "- Automated Login: Uses Playwright for automated browser interactions."
echo "- Profile Post Scraping: Extracts posts from a given LinkedIn profile URL."
echo "- Data Handling: Stores extracted data in a specified data directory."
echo "- Redis Integration: Supports Redis for task handling or caching if needed."

echo ""
echo "Prerequisites:"
echo "Ensure you have the following installed:"
echo "- Docker and Docker Compose (for a containerized setup)"
echo "- Python 3.12 (if running locally without Docker)"

echo ""
echo "Setup:"

echo ""
echo "1. Clone the Repository"
git clone https://github.com/your-username/linkedin-scraper.git
cd linkedin-scraper

echo ""
echo "2. Configure Environment Variables"
echo "Create a .env file in the root directory to store your LinkedIn credentials."
echo 'LINKEDIN_EMAIL=your-email@example.com' >> .env
echo 'LINKEDIN_PASSWORD=your-password' >> .env
echo "Replace 'your-email@example.com' and 'your-password' with your LinkedIn login credentials."

echo ""
echo "3. Docker Setup"
echo "Build and run the Docker container"
docker build -t linkedin-scraper .
docker run -d --name linkedin_scraper_container linkedin-scraper

echo "This will:"
echo "- Build the Docker image with all dependencies."
echo "- Start the container, which includes Redis and the Playwright-based scraping service."

echo ""
echo "4. Running the Scraper"
echo "The scraper starts automatically when the Docker container runs. It will begin scraping the LinkedIn profile specified in src/main.py."

echo ""
echo "5. Accessing Scraped Data"
echo "Scraped data will be saved in the /app/data directory inside the Docker container. To access this data:"
docker cp linkedin_scraper_container:/app/data ./data

echo ""
echo "Local Setup (Without Docker)"
echo "If you prefer running the scraper locally:"

echo ""
echo "Install Dependencies"
echo "Make sure you have Poetry installed, then run:"
poetry install

echo ""
echo "Install Playwright Browsers"
echo "Install Playwright and its required browsers:"
poetry run playwright install

echo ""
echo "Start Redis"
echo "Install Redis locally and start the Redis server:"
redis-server &

echo ""
echo "Run the Scraper"
python src/main.py

echo ""
echo "Configuration"
echo "LinkedIn Profile URL"
echo "In the src/main.py file, specify the LinkedIn profile URL you wish to scrape:"
echo 'PROFILE_URL = "https://www.linkedin.com/in/your-profile-url/recent-activity/all/"' >> src/main.py
echo "Replace 'your-profile-url' with the LinkedIn profile URL of the person whose posts you want to scrape."

echo ""
echo "Adjusting Scroll Behavior"
echo "The ProfileHandler class in src/handlers/profile_handler.py controls the scrolling behavior. Adjust the number of scrolls or wait time as needed."

echo ""
echo "Project Structure"
echo "
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
"

echo ""
echo "Happy Scraping!"
