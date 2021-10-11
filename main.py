import requests
import pandas
from bs4 import BeautifulSoup
import datetime as date

url_list = []
h1_list = []
title_list = []
meta_description_list = []

current_date = date.datetime.now().strftime("%b %d %Y")
url_text_file = open('urls.txt', 'r', encoding='utf-8')  # Reading file

for urlFromTextFile in url_text_file.readlines():
    url_list.append(urlFromTextFile.rstrip())

for urlFromList in url_list:

    page = requests.get(urlFromList)
    page_content = BeautifulSoup(page.content, 'html.parser')

    h1 = page_content.h1.get_text()

    if h1:
        h1_list.append(h1)
    else:
        h1_list.append('h1 Not Found')

    meta_description = page_content.find('meta', attrs={'name': 'description'})

    if meta_description:
        meta_description_list.append(meta_description['content'])
    else:
        meta_description_list.append('Meta Description Not Found')

    title = page_content.title.get_text()

    if title:
        title_list.append(title)
    else:
        title_list.append('Title not Found')

dataFrame = pandas.DataFrame({  # Defining DataFrame
    'URL': url_list,
    'h1': h1_list,
    'Title': title_list,
    'Meta Description': meta_description_list
})

dataFrame.to_csv('Exported_data_({date})_.csv'.format(  # Writing data to csv file
    date=current_date), index=False)
