THE PROBLEM:
    The website do512.com show events unordered, and does not filter out events that 
    have already ended.

THE SOLUTION:
    Use Python requests to scrape do512.com, and to return a list of events that
    start later than the current time.

THE REQUIREMENTS:
    1) Must be runnable from an android qpython app.
    2) Must return the starttime, and a clickable link to the event.

FUTURE FEATURES TO CONSIDER:
    1) Listing events chronologically for future dates.
    2) Taking into account the time it takes to travel to an event.
       Not including events that cannot be traveled to on time.

NOTE:
    1) The austin_events_today.py file is the easiest to use, but cannot be run on
       a smartphone.
    2) I was able to run austin_events_today_mobile.py on my android smartphone, using
       the app QPython, and setting the file up to run as a webapp at http://localhost:8080,
       but the output is really difficult to read through, and I wasn't able to figure out
       how to format it better.