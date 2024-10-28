from playwright.async_api import Page
import asyncio
from handlers.post_handler import PostHandler

class ProfileHandler:
    def __init__(self, page: Page):
        self.page = page

    async def get_posts(self):
        try:
            await self.page.wait_for_selector("div.pv0.ph5")
            for _ in range(5): 
                await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                await asyncio.sleep(5) 
            post_elements = await self.page.query_selector_all(
                "div.feed-shared-update-v2__control-menu-container.display-flex.flex-column.flex-grow-1"
            )

            post_handler = PostHandler(self.page)

            posts = await asyncio.gather(
                *[post_handler.extract_data(post_element) for post_element in post_elements]
            )
            return [post for post in posts if post] 
        except Exception as e:
            print(f"Error extracting posts: {e}")
            return []
