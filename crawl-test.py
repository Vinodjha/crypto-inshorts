import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    url = "https://cointelegraph.com/news/"
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)
        print("\n✅ HEADLINE PREVIEW:\n")
        print(result.markdown[:800])  # show preview

asyncio.run(main())
