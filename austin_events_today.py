from lxml import html
import requests

page_number = 0
more_pages = True
while more_pages:
    page_number += 1
    html_page = requests.get(f'https://do512.com/?page={page_number}')
    tree = html.fromstring(html_page.content)
    events = tree.xpath('//div[@class="ds-event-time dtstart"]/text()')
    more_pages = False

event_times = [event.replace("\n","").strip().split(' ')[0] for event in events]

event_times.sort()

for time in event_times:
    print(time)