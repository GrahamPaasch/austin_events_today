from lxml import html
from datetime import datetime
import requests

page_number = 0
data = []
print("Gathering data!")
while page_number < 5:
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

# Convert 12 hour time to 24 hour time
final_answers = []
for i in data:
    time12 = i[0]
    time24 = datetime.strptime(time12, "%I:%M%p")
    out_time = datetime.strftime(time24, "%H:%M")
    final_answers.append([out_time, i[1]])

# Sort the data by start time
def sorting_key(list_element):
    return int(list_element[0].replace(":","").replace("AM","").replace("PM",""))

final_answers.sort(key=sorting_key)

for final_answer in final_answers:
    if '00:' not in final_answer[0]:
        if '01:' not in final_answer[0]:
            time24 = final_answer[0]
            time12 = datetime.strptime(time24, "%H:%M")
            out_time = datetime.strftime(time12, "%I:%M %p")
            print([out_time, final_answer[1]])
        else:
            continue
    else:
        continue

for final_answer in final_answers:
    if '00:' in final_answer[0]:
        time24 = final_answer[0]
        time12 = datetime.strptime(time24, "%H:%M")
        out_time = datetime.strftime(time12, "%I:%M %p")
        print([out_time, final_answer[1]])
    if '01:' in final_answer[0]:
        time24 = final_answer[0]
        time12 = datetime.strptime(time24, "%H:%M")
        out_time = datetime.strftime(time12, "%I:%M %p")
        print([out_time, final_answer[1]])
