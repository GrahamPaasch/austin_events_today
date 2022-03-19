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

event_times = [event.replace("\n","").strip().split(' ')[0].upper() for event in events]

def numbers_only(time):
    return int(time.replace(":","").replace("AM","").replace("PM",""))

event_times.sort(key=numbers_only)

am_events = [time for time in event_times if "AM" in time]
pm_events = [time for time in event_times if "PM" in time]

for event in am_events:
    print(event)
for event in pm_events:
    print(event)

