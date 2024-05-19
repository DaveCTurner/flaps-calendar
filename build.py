from icalendar import Calendar, Event, vText
from datetime import datetime, date, timedelta
import pytz
import yaml

cals = {}

cals['flash'] = Calendar()
cals['flash']['prodid']        = vText('-//DCT//DCT//EN')
cals['flash']['version']       = vText('2.0')
cals['flash']['name']          = vText('Flash Company Morris')
cals['flash']['x-wr-calname']  = vText('Flash Company Morris')
cals['flash']['x-wr-timezone'] = vText('Europe/London')

cals['taps'] = Calendar()
cals['taps']['prodid']        = vText('-//DCT//DCT//EN')
cals['taps']['version']       = vText('2.0')
cals['taps']['name']          = vText('Kitchen Taps Dance')
cals['taps']['x-wr-calname']  = vText('Kitchen Taps Dance')
cals['taps']['x-wr-timezone'] = vText('Europe/London')

with open('rehearsals.yaml', 'r') as f:
    rehearsals_raw = yaml.load(f, Loader=yaml.Loader)

for rehearsal_meta in rehearsals_raw:
    match rehearsal_meta['group']:
        case 'flash':
            summary     = 'Flash Co'
            description =  'Regular Flash Company rehearsal'
            cal = cals['flash']
        case 'taps':
            summary     = 'Taps'
            description =  'Regular Kitchen Taps rehearsal'
            cal = cals['taps']
        case _:
            raise Exception('unknown group: ' + rehearsal_meta['group'])

    location = 'Clifton Village Hall, Otley, LS21 2ES, UK'
    date_split = rehearsal_meta['date'].split('-')
    start_time = datetime(int(date_split[0]), int(date_split[1]), int(date_split[2]), 17, 0, 0, tzinfo=pytz.timezone('Europe/London'))
    if 'start' in rehearsal_meta:
        summary += ' NB START TIME'
        time_split = rehearsal_meta['start'].split(':')
        start_time = start_time.replace(hour=int(time_split[0]), minute=int(time_split[1]))
    if 'location' in rehearsal_meta:
        location = rehearsal_meta['location']
        summary += ' NB LOCATION'

    event = Event()
    event['uid']         = vText('rehearsal-' + rehearsal_meta['date'])
    event['summary']     = vText(summary)
    event['description'] = vText(description)

    event.add('dtstart',  start_time)
    event.add('duration', vText('PT2H'))
    event['location']    = vText(location)
    cal.add_component(event)

with open('events.yaml', 'r') as f:
    events_raw = yaml.load(f, Loader=yaml.Loader)

for event_raw in events_raw:
    for group_name in event_raw['groups']:
        match group_name:
            case 'flash':
                group_name  = 'Flash Co'
                cal = cals['flash']
            case 'taps':
                group_name  = 'Taps'
                cal = cals['taps']
            case _:
                raise Exception('unknown group: ' + rehearsal_meta['group'])

        date_start_split = event_raw['start_day'].split('-')
        date_end_split   = event_raw['end_day'  ].split('-')

        event = Event()
        event['uid']         = vText(event_raw['start_day'])
        event['summary']     = vText(('TBC ' if 'tbc' in event_raw else '') + group_name + ' @ ' + event_raw['name'])
        event['description'] = vText(event_raw['description'])
        event['location']    = vText(event_raw['location'])
        event.add('dtstart', date(int(date_start_split[0]), int(date_start_split[1]), int(date_start_split[2])))
        event.add('dtend',   date(int(date_end_split[0]),   int(date_end_split[1]),   int(date_end_split[2])) + timedelta(days=1))
        cal.add_component(event)

with open('flash_company.cal', 'wb') as f:
    f.write(cals['flash'].to_ical())

with open('kitchen_taps.cal', 'wb') as f:
    f.write(cals['taps'].to_ical())
