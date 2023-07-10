from bs4 import BeautifulSoup
import lxml # If HTML parser does not support
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# soup_articles = soup.select(".titleline a")
#
# for article in soup_articles:
#     print(article.text)

articles = soup.find_all(name="a", rel="noreferrer")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(max(article_upvotes))

max_upvote = max(article_upvotes)
max_index = article_upvotes.index(max_upvote)


print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])






















""" Intro exercises"""
# with open("index.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
#
# all_anchors = soup.find_all(name="a")
# # print(all_anchors)
#
# # for tag in all_anchors:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
#
# linkedin_url = soup.select_one(selector="p a")
# # print(linkedin_url)
#
# headings = soup.select(".heading")
# print(headings)