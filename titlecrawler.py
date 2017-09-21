import requests
from sys import argv
from bs4 import BeautifulSoup

to_visit = ['http://news.ycombinator.com']
visited = set()

def get_request(url):
    if url not in visited:
        visited.add(url)
        try:
            content = requests.get(url)
            if content.status_code == requests.codes.ok:
                return content.text
        except requests.exceptions.RequestException as e:
            pass

def html_parser(text, url):
    if text:
        html = BeautifulSoup(text, "html.parser")
        if html.title:
            print html.title.string + ' - ' + url
        else:
            print url
        for a in html.find_all('a', href=True):
            url = a['href']
            if url.startswith("http") and url not in visited:
                to_visit.append(url)

if __name__ == "__main__":
    try:
        if len(argv) == 2:
            to_visit = [argv[1]]
        for url in to_visit:
            text = get_request(url)
            html_parser(text, url)
    except KeyboardInterrupt:
        print "\n\nBye :)"
