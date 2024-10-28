import sys
import asyncio
from scraper import LinkedInScraper

async def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <LinkedIn_username> <LinkedIn_password>")
        return

    username = sys.argv[1]
    password = sys.argv[2]

    scraper = LinkedInScraper(username, password)
    await scraper.run() 
    scraper.close()

if __name__ == "__main__":
    asyncio.run(main())
