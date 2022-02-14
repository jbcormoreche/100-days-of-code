# Web Scraping with BeautifulSoup

# Scraping an html file
from bs4 import BeautifulSoup

with open("./Day045-Web_Scraping_BeautifulSoup/website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup)
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.li)  # Find the first instance of a list tag

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.getText())

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())

company_url = soup.select_one("p a")
print(company_url)

name = soup.select_one("#name")
print(name)

headings = soup.select(".heading")
print(headings)

# Scraping a live website
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

upvotes = []
subtexts = soup.find_all(name="td", class_="subtext")
for subtext in subtexts:
    if not subtext.find(name="span", class_="score"):
        upvotes.append(0)
    else:
        upvotes.append(int(subtext.find(name="span", class_="score").getText().split()[0]))

max_number = max(upvotes)
max_index = upvotes.index(max_number)
print(article_texts[max_index])
print(article_links[max_index])
print(f"{max_number} points")

# Day 45 Project - 100 Greatest Movies
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in all_movies]

movies.reverse()

with open("./Day045-Web_Scraping_BeautifulSoup-100_Greatest_Movies/movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
