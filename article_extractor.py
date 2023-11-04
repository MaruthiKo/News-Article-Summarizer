import json
import requests
from newspaper import Article


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


session = requests.Session()

def get_article(article_url):   
    try:
        response = session.get(article_url, headers=headers, timeout=10)

        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()
            return article
        else:
            print(f"Failed to fetch article at {article_url}")
    except Exception as e:
        print(f"Error occured while fetching data at {article_url}: {e}")

# article = get_article("https://edition.cnn.com/2023/11/03/investing/who-is-sam-bankman-fried-ftx-fraud-trial/index.html")
# print(article.title)
# print(article.text)