from article_extractor import get_article
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
from api_key import get_api_key


OPENAI_API_KEY = get_api_key("../../.env")


article_url = "https://edition.cnn.com/2023/11/03/investing/who-is-sam-bankman-fried-ftx-fraud-trial/index.html"
article = get_article(article_url)

article_title = article.title
article_text = article.text

template = """You are a very good assistant that summarizes online articles.

Here's the article you want to summarize.

==================
Title: {article_title}

{article_text}
==================

Write a summary of the previous article.Ensure the summary has the main points of the article. The summary should be concise and easy to understand.
"""
prompt = template.format(article_title=article.title, article_text=article.text)

messages = [HumanMessage(content=prompt)]

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

summary = chat(messages)
print(summary.content)