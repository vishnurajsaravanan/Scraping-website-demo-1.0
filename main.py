from bs4 import BeautifulSoup
import requests
from stream import *

def get_url(url):
    response = requests.get(url)
    return response
web_link = get_url(dat)

def get_data(element1 = []):
    soup = BeautifulSoup(web_link.content,'html.parser')
    result = soup.find_all("div", class_="col-12 col-sm-6 content")
    for i in range(len(result)):
        contents = soup.find_all("div", class_="col-12 col-sm-6 content")[i].h3
        auth_name = soup.find_all(class_="authors-name")[i].a
        dict = {"Content": contents.text, "Author": auth_name.text}
        element1.append(dict)
    return element1

def data(element2 = []):
    soup = BeautifulSoup(web_link.content, "html.parser" )
    elements = soup.find_all('ul')[0]
    for i in range(len(elements)):
        auth_name = soup.find_all('a', class_='dm-user__name')[i]
        heading = soup.find_all('div', class_= "dm-contentListItem__title")[i].a
        auth_content = soup.find_all('div', class_="dm-content-list-item__text dm-content-list-item__text--ellipsis")[i]
        link = soup.find_all('div',class_="dm-content-list-item__text dm-content-list-item__text--ellipsis")[i].a['href']
        data = {"Author name" : auth_name.text,"Heading": heading.text,"Content" : auth_content.text, "Link" : link}
        element2.append(data)
    return element2

def result_data(list = []):
    soup = BeautifulSoup(web_link.content, 'html.parser')
    element = soup.find_all('article', class_="blog-post")[0]
    for i in range(len(element)):
        heading = soup.find_all('h2', class_='lb-bold blog-post-title')[i]
        author_name = soup.find_all('footer', class_="blog-post-meta")[i].a
        time = soup.find_all('footer', class_="blog-post-meta")[i].time
        content = soup.find_all('section',class_="blog-post-excerpt lb-rtxt")[i].p
        dict = {
            "Author": author_name.text,
            "Time": time.text,
            "Heading": heading.text,
            "Content": content.text
        }
        list.append(dict)
    return list
