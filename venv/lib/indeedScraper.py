import requests
from bs4 import BeautifulSoup, SoupStrainer
from csv import writer

response = requests.get('https://www.indeed.com/m/jobs?q=entry+level+software+engineer&l=Austin%2C+TX')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='jobTitle')

posts2 = soup.find(class_='companyName')


for post in posts:
    title = post.find('a').get_text()
    link = post.find('a', href=True)

    #link['href'] returns the url for job
    jobLink = "http://www.indeed.com/m/"+ link['href']

    #location = post.findParent().find(class_='location').get_text()
    company = post.findParent()

    if(post.findParent().find(class_='location').get_text()) :
        location = post.findParent().find(class_='location').get_text()

    try:
        salary = post.findParent().find(class_='salary').get_text()
    except AttributeError:
        print
        "Salary: -"




    print(title)
    #print(company)
    print(location)
    print(salary)
    print(jobLink)
    print("-" * 40)
