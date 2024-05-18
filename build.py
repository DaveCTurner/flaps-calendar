from icalendar import Calendar, Event, vText
from datetime import datetime
import pytz

cal = Calendar()

event = Event()
event['description'] = vText('Flash Company Rehearsal')
event['uid'] = vText('2024-05-18')
event.add('dtstart', datetime(2024, 5, 18, 17, 0, 0, tzinfo=pytz.timezone('Europe/London')))
event['location'] = vText('Clifton Village Hall, Clifton, Yorkshire')

cal.add_component(event)

with open('test.cal', 'wb') as f:
    f.write(cal.to_ical())


