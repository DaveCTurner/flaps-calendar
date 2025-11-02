To create venv:

    $ python -m venv .
    $ git restore .gitignore
    $ source bin/activate
    $ pip install icalendar pytz pyyaml

To activate venv if already created:

    $ source bin/activate

Then to rebuild calendars:

    $ python ./build.py
