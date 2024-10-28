from playwright.async_api import Page

class PostHandler:
    def __init__(self, page: Page):
        self.page = page

    async def extract_data(self, post_element):
        try:
            content_element = await post_element.query_selector("div.feed-shared-text")
            content = await content_element.inner_text() if content_element else "No content"
            timestamp_element = await post_element.query_selector("span.feed-shared-actor__sub-description")
            timestamp = await timestamp_element.inner_text() if timestamp_element else "No timestamp"
            likes_element = await post_element.query_selector("span.social-details-social-counts__reactions-count")
            likes = await likes_element.inner_text() if likes_element else "0"
            comments_element = await post_element.query_selector("span.social-details-social-counts__comments-count")
            comments = await comments_element.inner_text() if comments_element else "0"

            return {
                "content": content.strip(),
                "timestamp": timestamp.strip(),
                "likes": likes.strip(),
                "comments": comments.strip()
            }
        except Exception as e:
            print(f"Error extracting post data: {e}")
            return None