import requests
from bs4 import BeautifulSoup
from csv import writer

"""Creating a Python web parser using BeautifulSoup
Using scraping sandbox website: http://books.toscrape.com/index.html
"""

"""to get imports to work in pycharm had to go to Pycharm->preferences->Project Interpreter->Install"""


response = requests.get('http://books.toscrape.com/catalogue/category/books_1/index.html')

soup = BeautifulSoup(response.text, 'html.parser') #pulls in webpage

posts = soup.find_all(class_='product_pod')

for post in posts:
    title = post.findAll('a')[1].get_text()

    price = post.findAll(class_='price_color')[0].get_text()
    price = price[1:] #removing weird character from front of price

    print("Title: " + title + "\n"
                              "Price: " + price + "\n")