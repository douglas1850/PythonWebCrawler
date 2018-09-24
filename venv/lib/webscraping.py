import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import writer
import httplib2

"""Creating a Python web parser using BeautifulSoup
Using scraping sandbox website: http://books.toscrape.com/index.html
"""

"""to get imports to work in pycharm had to go to Pycharm->preferences->Project Interpreter->Install"""


response = requests.get('http://books.toscrape.com/catalogue/category/books_1/index.html')

soup = BeautifulSoup(response.text, 'html.parser') #pulls in webpage

posts = soup.find_all(class_='product_pod')

with open('books.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Price']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.findAll('a')[1].get_text()

        price = post.findAll(class_='price_color')[0].get_text()
        price = price[1:] #removing weird character from front of price

        print("Title: " + title + "\n"
                                  "Price: " + price + "\n")
        csv_writer.writerow([title, price])

http = httplib2.Http()
status, response = http.request('http://books.toscrape.com/catalogue/category/books_1/index.html')

for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])