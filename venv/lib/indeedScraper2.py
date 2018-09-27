import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://www.indeed.com/jobs?q=entry%20level%20software%20engineer&l=Austin%2C%20TX&radius=50&vjk=72d16abb7ce4ace5')

soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(class_="jobtitle turnstileLink")
companies = soup.find_all(class_="company")
locations = soup.find_all(class_="location")


for title, company, location in zip(titles, companies, locations):
    print(title.get_text())
    print(company.get_text().lstrip())
    print(location.get_text())

    print("-" * 60)

