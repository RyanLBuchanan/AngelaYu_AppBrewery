from bs4 import BeautifulSoup
import lxml # If HTML parser does not support



























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