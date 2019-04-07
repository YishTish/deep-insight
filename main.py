from bs4 import BeautifulSoup
from sqlalchemy import Table, exists, Column, Integer, String, MetaData
from urllib.request import urlopen, Request
import json

BASE_URL = "https://my-json-server.typicode.com"


def scrape_for_links(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, features="html.parser")
    link_array = []
    for item in soup.find_all('li'):
        for link in item.find_all('a', href=True):
            link_array.append(link['href'])
    return link_array


def update_db(json_array, entity_name):
    if len(json_array) > 0:
        import sqlalchemy
        sample_entity = json_array[0]
        table = Table(entity_name,__table__args
        columns = [sqlalchemy.Column(
            sql
        )]
        for key in sample_entity.keys():
            columns.append(Column(sample_entity[key], type(sample_entity[key])))
        table.columns.



def get_link_content(link):
    print("Getting Content for %s%s" % (BASE_URL, link))
    link_elements = link.split("/")
    entity_name = link_elements[len(link_elements) -1]
    with urlopen("%s%s" % (BASE_URL, link)) as response:
        content = json.loads(response.read())
        update_db(content, entity_name)


if __name__ == '__main__':
    url = "%s/typicode/demo" % BASE_URL
    link_array = scrape_for_links(url)
    for link in link_array:
        get_link_content(link)
