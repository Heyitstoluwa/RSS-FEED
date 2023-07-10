import feedparser
import requests
from bs4 import BeautifulSoup

# Parse the RSS feed
feed_url = 'https://rss.punchng.com/v1/category/latest_news'  # Replace with the actual RSS feed URL
feed = feedparser.parse(feed_url)

 
# Iterate through the entries/posts in the feed
for entry in feed.entries:
    post_title = entry.title
    post_url = entry.link
    post_author = entry.author
    image_url = entry.url



    # Access the post webpage
    response = requests.get(post_url)
    post_html = response.text

    # Parse the post content
    soup = BeautifulSoup(post_html, 'html.parser')
    post_content = soup.find('div', class_='post-content')  # Replace with the appropriate HTML element that contains the post content

    if post_content:
        # Process the content as needed
        full_content = post_content.get_text()
    

        # Print or do something with the full content
        print(f"Title: {post_title}")
        print(f"Full Content: {full_content}")
        print(f"Author: {post_author}")
        print(f"src: {image_url}")
        print("************************************************************************************************************************************")
