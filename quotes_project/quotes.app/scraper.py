import requests
from bs4 import BeautifulSoup
from .models import Author, Quote

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author_name = quote.find('small', class_='author').get_text()
            tags = ','.join([tag.get_text() for tag in quote.find_all('a', class_='tag')])

            author, created = Author.objects.get_or_create(name=author_name)
            Quote.objects.get_or_create(text=text, author=author, tags=tags)

        next_btn = soup.find('li', class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
