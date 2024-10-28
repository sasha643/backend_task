import os
import json
import asyncio
from playwright.async_api import async_playwright
from handlers.profile_handler import ProfileHandler
from queue_manager import QueueManager

class LinkedInScraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.queue = QueueManager()
        self.visited_profiles = set()
        self.login_successful = False

    async def login(self, page):
        """Login to LinkedIn."""
        print("Navigating to login page...")
        await page.goto("https://www.linkedin.com/login", wait_until="load")
        print("Filling in login details...")
        await page.fill("#username", self.username)
        await page.fill("#password", self.password)
        print("Submitting login form...")
        await page.click("button[type='submit']")
        self.login_successful = True
        print("Login successful.")

    async def scrape_profile(self, page, profile_url):
        """Scrape posts from a given profile URL and store them in a file."""
        print(f"Scraping profile: {profile_url}...")
        try:
            await page.goto(profile_url, wait_until="load")
            profile_handler = ProfileHandler(page)
            posts = await profile_handler.get_posts()
            new_profiles = await profile_handler.get_related_profiles()

            # Save posts to a JSON file
            self.save_posts_to_file(profile_url, posts)

            # Push new profiles to the queue and mark the current profile as visited
            self.queue.push_new_profiles(new_profiles)
            self.visited_profiles.add(profile_url)
            print(f"Scraped {len(posts)} posts from {profile_url}.")
            return posts
        except Exception as e:
            print(f"Error scraping {profile_url}: {e}")
            return []

    def save_posts_to_file(self, profile_url, posts):
        """Save scraped posts to a JSON file."""
        dir_path = "C:/Users/Saurabh/Desktop/LinkedIn_scraper/data"
        file_name = "scraped_posts.json"
        file_path = os.path.join(dir_path, file_name)

        # Ensure the directory exists
        os.makedirs(dir_path, exist_ok=True)

        try:
            with open(file_path, "a") as f:
                for post in posts:
                    post['profile_url'] = profile_url  # Include profile URL in the post data
                    json.dump(post, f)
                    f.write('\n')  # New line for each post entry
            print(f"Saved posts from {profile_url} to {file_path}.")
        except Exception as e:
            print(f"Error saving posts to file: {e}")

    async def run(self):
        """Continuously process profiles from the queue until the desired number is reached."""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)  # Set headless=False to see the browser
            page = await browser.new_page()
            
            await self.login(page)
            if not self.login_successful:
                print("Login failed. Please check your credentials.")
                await browser.close()
                return

            while len(self.visited_profiles) < 500:
                profile_url = self.queue.get_next_profile_url()
                if profile_url and profile_url not in self.visited_profiles:
                    try:
                        # Directly use profile_url since it is already a string
                        posts = await self.scrape_profile(page, profile_url)
                    except Exception as e:
                        print(f"Error scraping {profile_url}: {e}")
                else:
                    print("No more profiles to scrape or all profiles have been visited.")
                    break

            await browser.close()

    async def close(self, browser):
        """Close the browser."""
        await browser.close()

