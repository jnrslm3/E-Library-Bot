from bs4 import BeautifulSoup as BS
import requests

def get_links():
    link = "https://mybook.ru/catalog/books/free/?page="
    links = []
    for i in range(1, 21):
        links.append(f'{link}{i}')
    return links

def get_book_links():
    links = get_links()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

    books_links = []

    for url in links: 
        response = requests.get(url, headers=headers)
        soup = BS(response.text, 'html.parser')
        blocks = soup.find_all('div', class_="e4xwgl-1 gEQwGK")
        for b in blocks:
            a = b.find('a').get('href')
            books_links.append(f"https://mybook.ru{a}")
        
    return books_links












if __name__ == "__main__":
    get_book_links()