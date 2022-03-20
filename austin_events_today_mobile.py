from bottle import route, run

@route('/')
def main():
    from bs4 import BeautifulSoup
    from datetime import datetime
    import requests

    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

    page_number = 0
    data = []
    print("Gathering data!")
    while page_number < 1000:
        # Get the page HTML
        page_number += 1
        print(f"Gathered from page {page_number}!")
        html_page = requests.get(f'https://do512.com/events/today/?page={page_number}')
        soup = BeautifulSoup(html_page.text, 'html.parser')
        # Grab HTML div for each event that contains the event links and the start times
        events = soup.findAll('div',attrs={'itemprop':'event'})
        # If no events are found, terminate the loop
        if len(events) == 0:
            print("All data gathered!")
            break
        # Map together the events and the start times
        mapped_events_and_times = []
        for event in events:
            try:
                mapped_events_and_times.append(
                    [
                        event.find(
                            'div',attrs={'class':'ds-event-time dtstart'}
                            ).getText().replace(
                                "\n",""
                                ).strip().split(' ')[0].upper(), 
                        f"https://do512.com{event.get('data-permalink')}"
                    ]
                )
            except:
                continue
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

    output = []

    for final_answer in final_answers:
        if '00:' not in final_answer[0]:
            if '01:' not in final_answer[0]:
                time24 = final_answer[0]
                time12 = datetime.strptime(time24, "%H:%M")
                out_time = datetime.strftime(time12, "%I:%M %p")
                output.append([out_time, final_answer[1]])
            else:
                continue
        else:
            continue

    for final_answer in final_answers:
        if '00:' in final_answer[0]:
            time24 = final_answer[0]
            time12 = datetime.strptime(time24, "%H:%M")
            out_time = datetime.strftime(time12, "%I:%M %p")
            output.append([out_time, final_answer[1]])
        if '01:' in final_answer[0]:
            time24 = final_answer[0]
            time12 = datetime.strptime(time24, "%H:%M")
            out_time = datetime.strftime(time12, "%I:%M %p")
            output.append([out_time, final_answer[1]])
    
    return '\n'.join(output)

run(host='localhost', port=8080)