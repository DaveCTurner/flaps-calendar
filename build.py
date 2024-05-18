from icalendar import Calendar, Event, vText
from datetime import datetime, date
import pytz
import json

cal = Calendar()
cal['prodid']       = vText('-//DCT//DCT//EN')
cal['version']      = vText('2.0')
cal['name']         = vText('Flash Company Morris')
cal['x-wr-calname'] = vText('Flash Company Morris')
cal['color']        = vText('gold')

with open('flash_company_rehearsals.json', 'r') as f:
    rehearsals_raw = json.load(f)

for rehearsal_date, rehearsal_meta in rehearsals_raw.items():
    summary  = 'Flash Co'
    location = 'Clifton Village Hall, Otley, LS21 2ES'
    date_split = rehearsal_date.split('-')
    start_time = datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]), 17, 0, 0, tzinfo=pytz.timezone('Europe/London'))
    if 'start' in rehearsal_meta:
        summary += ' NB START TIME'
        time_split = rehearsal_meta['start'].split(':')
        start_time = start_time.replace(hour=int(time_split[0]), minute=int(time_split[1]))
    if 'location' in rehearsal_meta:
        location = rehearsal_meta['location']
        summary += ' NB LOCATION'

    event = Event()
    event['uid']         = vText(rehearsal_date)
    event['summary']     = vText(summary)
    event['description'] = vText('Regular Flash Company rehearsal')

    event.add('dtstart',  start_time)
    event.add('duration', vText('PT2H'))
    event['location']    = vText(location)
    event['color']       = vText('gold')
    cal.add_component(event)

with open('flash_company_events.json', 'r') as f:
    events_raw = json.load(f)

for event_raw in events_raw:
    date_start_split = event_raw['start_day'].split('-')
    date_end_split   = event_raw['end_day'  ].split('-')

    event = Event()
    event['uid']         = vText(event_raw['start_day'])
    event['summary']     = vText('Flash Co @ ' + event_raw['name'])
    event['description'] = vText('Flash Company Dance Out')
    event['location']    = vText(event_raw['location'])
    event.add('dtstart', date(int(date_start_split[0]), int(date_start_split[1]), int(date_start_split[2])))
    event.add('dtend',   date(int(date_end_split[0]),   int(date_end_split[1]),   int(date_end_split[2])))
    event['color']       = vText('gold')
    cal.add_component(event)

with open('flash_company.cal', 'wb') as f:
    f.write(cal.to_ical())


