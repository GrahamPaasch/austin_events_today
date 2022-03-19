from lxml import html
import requests

page_number = 0
more_pages = True
while more_pages:
    page_number += 1
    html_page = requests.get(f'https://do512.com/?page={page_number}')
    tree = html.fromstring(html_page.content)
    buyers = tree.xpath('//div[@title="$$$$$$$$$$"]/text()')
    more_pages = False