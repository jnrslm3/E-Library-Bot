from bs4 import BeautifulSoup as BS
import requests

def get_links():
    link = "https://mybook.ru/catalog/books/free/?page="
    links = []
    for i in range(1, 2):
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

def get_book_info():
    links = get_book_links()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

    for url in links:
        response = requests.get(url, headers= headers)
        soup = BS(response.text, 'html.parser')
        main = soup.find('section', class_="hf8eib-0 acq6ib-2 hYqYfq gixdCj")
        title = main.find('h1', class_="sc-bdfBwQ lnjchu-0 jzwvLi gUKDCi sc-1c0xbiw-11 bzVsYa").text
        author = main.find('div', class_="dey4wx-1 jVKkXg").text
        summary = main.find('div', class_="iszfik-2 gAFRve")
        description = summary.find('p').text
        more_info = main.find('div', class_="ant-col sc-1c0xbiw-9 eSjGMZ").text
        rating = main.find('div', class_="ant-col sc-1c0xbiw-5 lotch").text
        l_link = url
        p = main.find('div', class_="hh1ehr-0 kkiIwl").find('picture').find('source').get('srcset').split(',')[0]






if __name__ == "__main__":
    get_book_info()