from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])




# print(article_texts)
# print(article_links)
# print(article_upvotes)





# import lxml
# with open("website.html") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.prettify())
# # print(soup.p)
#
# all_auchor_tags = soup.find_all(name="a")
# print(all_auchor_tags)
#
#
# for tag in all_auchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# class_is_heading = soup.find_all(class_="heading")
# print(class_is_heading)
#
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)