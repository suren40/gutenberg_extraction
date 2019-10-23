'''
Crawling the mp3 files from https;//gutenberg.org site

'''
import requests,csv
from lxml import html
URL = 'https://www.gutenberg.org/browse/categories/3'
NAME_OF_LINK_FILE = 'links.csv'

def crawl_link():
    response = requests.get(URL)
    tree = html.fromstring(response.content)
    root = tree.xpath("//h2/following-sibling::ul/li/a")
    for item in root:
        name = item.xpath('./text()')[0].strip()
        path = item.xpath('./@href')[0].strip()
        link = 'https://gutenberg.org'+path
        with open(NAME_OF_LINK_FILE,'a',newline='') as file:
            the_writer = csv.writer(file)
            the_writer.writerow([name,link])
            file.close()




if __name__ == "__main__":
    with open(NAME_OF_LINK_FILE,'w',newline='') as file:
        the_writer = csv.writer(file)
        header = ['NAME','LINK']
        the_writer.writerow(header)
        file.close()

    print("Crawling started!!")
    crawl_link()
    print('Crawling Done!')

    