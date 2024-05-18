from icalendar import Calendar, Event, vText
from datetime import datetime
import pytz

cal = Calendar()
cal['prodid']       = vText('-//DCT//DCT//EN')
cal['version']      = vText('2.0')
cal['name']         = vText('Flash Company Morris')
cal['x-wr-calname'] = vText('Flash Company Morris')
cal['color']        = vText('gold')

event = Event()
event['summary']     = vText('Flash Company Rehearsal')
event['description'] = vText('Regular rehearsal')
event['uid']         = vText('2024-05-18')
event.add('dtstart', datetime(2024, 5, 18, 17, 0, 0, tzinfo=pytz.timezone('Europe/London')))
event.add('dtend',   datetime(2024, 5, 18, 19, 0, 0, tzinfo=pytz.timezone('Europe/London')))
event['location']    = vText('Clifton Village Hall, Otley, North Yorkshire, LS21 2ES')

cal.add_component(event)

with open('test.cal', 'wb') as f:
    f.write(cal.to_ical())


