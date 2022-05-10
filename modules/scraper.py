import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup("p")
    cite_need_count = 0

    for result in results:
        text = result.get_text()
        if 'citation needed' in text:
            cite_need_count += 1
            
    print(cite_need_count)


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup("p")

    for result in results:
        text = result.get_text()
        if 'citation needed' in text:
            print(text)


url = "https://en.wikipedia.org/wiki/Lynn_Conway"

get_citations_needed_count(url)

get_citations_needed_report(url)