from bs4 import BeautifulSoup as BS
import requests

def get_links():
    link = "https://mybook.ru/catalog/books/free/?page="
    links = []
    for i in range(1, 21):
        links.append(f'{link}{i}')
    return links














if __name__ == "__main__":
    get_book_links()