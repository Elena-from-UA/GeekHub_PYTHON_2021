import csv
import requests
from bs4 import BeautifulSoup
import write_db as wdb

def next_page(param):
    url = f'https://quotes.toscrape.com/{param}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    res = soup.find('li', class_='next')
    try:
        for i in res.find_all('a'):
            return i['href']
    except:
        return None
        
def get_quotes(param):
    url = f'https://quotes.toscrape.com/{param}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_='text')
    for quote in quotes:
        with open('quotes.csv', "a",encoding='utf-16', newline="") as file:
            quote = [quote.text]
            writer = csv.writer(file)
            writer.writerow(quote)

def get_authors(param):
    url = f'https://quotes.toscrape.com/{param}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    authors = soup.find_all('small', class_='author')
    for author in authors:
        with open('authors.csv', "a",encoding='utf-16', newline="") as file:
            author = [author.text]
            writer = csv.writer(file)
            writer.writerow(author)

def get_about_author(param):
    url = f'https://quotes.toscrape.com/{param}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    names = soup.find('h3', class_='author-title')
    born = soup.find('span', class_='author-born-date')
    born_loc = soup.find('span', class_='author-born-location')
    description = soup.find('div', class_='author-description')
    with open('about_authors.csv','a',encoding='utf-16',newline="") as file:
        about_auth = [names.get_text().strip(), born.get_text(), born_loc.get_text(), description.get_text().replace("\n","")]  
        writer = csv.writer(file)
        writer.writerow(about_auth)
            
def href_author(param):
    url = f'https://quotes.toscrape.com/{param}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for link in soup.find_all('a', href = True, text = '(about)'):
        get_about_author(link.get('href'))
        
def main():
    param = 'page/1/'
    page = next_page(param) 
    while param != None: 
        get_quotes(param)
        get_authors(param)
        href_author(param)
        param = page 
        page = next_page(param)


main()
wdb.main()



