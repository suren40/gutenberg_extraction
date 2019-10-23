"""
Opening the file and downloading the mp3 and readme text
"""


import requests
import pandas as pd
from lxml import html
LINKS = 'original_links.csv'
BASE = 'https://gutenberg.org'


def crawl_name(URL):
    respond = requests.get(URL) 
    page = respond.content
    tree = html.fromstring(page)  
    header = tree.xpath("//h1[@itemprop='name']/text()") 
    sp = header[0].split('by')
    title = sp[0].strip()
    try:
        author = sp[1].strip()
    except IndexError:
        author = tree.xpath('//a[@itemprop="creator"]/text()')[0].strip()
    mp3_path = tree.xpath('//td[@content="audio/mpeg"]/a/@href')
    readme_path = tree.xpath('//td[@content="text/plain; charset=us-ascii"]/a/@href')
    try:
        readme_url = BASE+readme_path[0]
    except:
        readme_url = None
    mp3_url = BASE+mp3_path[0]
    name = URL.replace('https://gutenberg.org/ebooks/','')
    
    doc = requests.get(mp3_url)
    mp3_title = author+'--'+title+'--'+name+'-m-mp3audio.mp3'
    with open(mp3_title,'wb') as f:
        f.write(doc.content)
    
    if readme_url:
        doc = requests.get(readme_url)
        readme_title = author+'--'+title+'--'+name+'-m-readme.txt'
        with open(readme_title,'wb') as f:
            f.write(doc.content)
    else:
        pass


if __name__ == "__main__":
    df = pd.read_csv(LINKS)
    i = 1 
    j =  1
    for link in df['LINK']:
        crawl_name(link)
        print('Completed '+str(i)+ 'original' +str(j))
        i +=1
        

