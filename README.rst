==================================================
README for a simple text-based countdown in Python
==================================================

Overview
========

Problem: You want to count down to an event (e.g., a rocket launch).
But the web-based animated countdown consumes too much screen space
and battery power (i.e., your laptop's fan turns on when you go to that
web page).
At least, that was the experience that motivated this project...

Solution: a text-based countdown in a small shell or console window.
This one, ``down.py``, is written in Python 3.
Rather than writing a newline each time, this script rewrites the same line.
For example, ::

    $ # EchoStar 23 launch NET February 14, 2017, 11:34am EST
    $ # NET = not/no earlier than
    $ ./down.py 2017-02-14 11:34:00 -z-5:00
    T - 5 12:16:40

Help
====

Here's what you get when you ask for help (``./down.py -h``)::

    usage: down.py [-h] [-z ZONE] [-c COUNT] [-i INTERVAL] [-n]
                   yyyy-mm-dd hh:mm:ss

    Count down to an event.

    positional arguments:
      yyyy-mm-dd            event year-month-day
      hh:mm:ss              event hour:minte:second

    optional arguments:
      -h, --help            show this help message and exit
      -z ZONE, --zone ZONE  timezone as [-]hh:mm, no whitespace after '-z'
      -c COUNT, --count COUNT
                            number of iterations
      -i INTERVAL, --interval INTERVAL
                            seconds between timesteps
      -n, --now             show current time



The output is of the form::

    T - 3 02:35:25

showing the days, hours, minutes, and seconds until the event.

Limitations
===========

The script won't count up for events in the past.

The default count (number of iterations) is 999999999, which taken at
1-second intervals is about 31.6 years.

Examples
========

Launch at 2015-01-01 00:00:00 GMT ::

    ./down.py 2015-01-01 00:00:00

Launch at midnight, June 24, 2014, California time (UTC-7, PDT) ::

    ./down.py 2014-06-24 00:00:00 -z-7:00

Launch at 5:35pm, June 26, 2014, Eastern Daylight Time (UTC-4),
report at 5 second intervals ::

    ./down.py 2014-06-26 00:00:00 -z-4:00

Launch at 11:34am, February 14, 2017, Eastern Standard Time (UTC-5) ::

    ./down.py 2017-02-14 11:34:00 -z-5:00

Same as above, but show the current time in UTC. ::

    ./down.py 2014-06-26 00:00:00 -z-4:00 -n

Same as above, but only increment every 5 seconds (and don't show UTC time).

    ./down.py 2014-06-26 00:00:00 -z-4:00 -i 5


