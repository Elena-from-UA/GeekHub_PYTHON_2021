import csv
import requests
from bs4 import BeautifulSoup
import write_db as wdb

def check_in_file(file_csv,line_csv):
    open(f'{file_csv}','a')
    with open(f'{file_csv}',encoding='utf-16', newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            if line == line_csv:
                return False
        return True
            
def get_quotes(soup):
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    for i in range(len(quotes)):
        quote = [quotes[i].text,authors[i].text]
        if check_in_file('quotes.csv',quote):
            with open('quotes.csv', "a",encoding='utf-16', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(quote)           

def get_authors(soup):
    authors = soup.find_all('small', class_='author')
    for author in authors:
        author = [author.text]
        if check_in_file('authors.csv',author):
            with open('authors.csv', "a",encoding='utf-16', newline="") as file:
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
    about_auth = [names.get_text().strip(), born.get_text(), born_loc.get_text(), description.get_text().replace("\n","")]
    if check_in_file('about_authors.csv',about_auth):
        with open('about_authors.csv','a',encoding='utf-16',newline="") as file:  
            writer = csv.writer(file)
            writer.writerow(about_auth)
            
def href_author(soup):
    name_author = soup.find_all('small', class_='author')
    if check_in_file('authors.csv',name_author):
        for link in soup.find_all('a', href = True, text = '(about)'):
            get_about_author(link.get('href'))
        
def main():
    param = 'page/1/' 
    while param != None:
        url = f'https://quotes.toscrape.com/{param}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        get_quotes(soup)
        get_authors(soup)
        href_author(soup)
        try:
            page = soup.find('li', class_='next')
            for i in page.find_all('a'):
                page = i['href']
        except:
            break
        param = page


main()
wdb.main()
