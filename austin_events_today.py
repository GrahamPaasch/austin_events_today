from lxml import html
import requests

page_number = 0
data = []
print("Gathering data!")
while page_number < 100:
    # Get the page HTML
    page_number += 1
    print(f"Gathered from page {page_number}!")
    html_page = requests.get(f'https://do512.com/events/today/?page={page_number}')
    tree = html.fromstring(html_page.content)
    # Grab the events and the start times from the HTML
    events = tree.xpath('//div[@itemprop="event"]')
    start_times = tree.xpath('//div[@class="ds-event-time dtstart"]/text()')
    # Map together the events and the start times
    mapped_events_and_times = [[start_time.replace("\n","").strip().split(' ')[0].upper(), f"https://do512.com{event.get('data-permalink')}"] for event, start_time in zip(events, start_times)]
    # Finish gathering data if the url goes to a blank page
    if not mapped_events_and_times:
        print("All data gathered!")
        break
    # Give back data in a list of lists
    data.extend(mapped_events_and_times)

# Sort the data by start time
def sorting_key(list_element):
    return int(list_element[0].replace(":","").replace("AM","").replace("PM",""))

'''
    # Clean up and sort the start times
    start_times = [start_time.replace("\n","").strip().split(' ')[0].upper() for start_time in start_times]

    start_times.sort(key=numbers_only)
    am_times = [time for time in start_times if "AM" in time]
    pm_times = [time for time in start_times if "PM" in time]
    times = am_times + pm_times
    #
    for time, event in zip(times, events):
        link = f"https://do512.com{event.get('data-permalink')}"
        print(f"{time} | {link}")
'''
'''
event_times = [event.replace("\n","").strip().split(' ')[0].upper() for event in events]

def numbers_only(time):
    return int(time.replace(":","").replace("AM","").replace("PM",""))

event_times.sort(key=numbers_only)

am_events = [time for time in event_times if "AM" in time]
pm_events = [time for time in event_times if "PM" in time]

link = ""
for event in am_events:
    print(f"{event} | {link}")
for event in pm_events:
    print(f"{event} | {link}")
'''