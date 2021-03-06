#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# down.py -- count down to launch

import sys
import datetime as dt
import time
import argparse
#import pdb


def tdelta2dhms(tdelta):
    #pdb.set_trace()
    dd = tdelta.days
    remain = tdelta.seconds
    hh = remain // 3600
    remain -= hh * 3600
    mm = remain // 60
    remain -= mm * 60
    ss = remain
    return dd, hh, mm, ss


def parseISOdatetime(datestr, timestr, zonestr):
    """Parse date, time, and zone from date-time-zone string as:
      yyyy-mm-dd hh:mm:ss -z[-]zz:zz
    where [-]zz:zz is zone offset from UTC. (West requires '-' to subtract
    from UTC.)  Example:
        ./down.py 2017-02-14 11:34:00 -z-5:00

    """
    #pdb.set_trace()
    delems = [ int(s) for s in datestr.split('-') ]
    telems = [ int(s) for s in timestr.split(':') ]
    zelems = [ int(s) for s in zonestr.split(':') ]

    dtlocal = dt.datetime(delems[0], delems[1], delems[2], telems[0], telems[1], telems[2])
    hemisphere = 1      # initially position - Eastern hemisphere
    if (zelems[0] < 0):
        hemisphere = -1
        zelems[0] *= -1

    timed = dt.timedelta(0, zelems[0]*3600 + zelems[1]*60) * hemisphere
    dtutc = dtlocal - timed

    return dtutc

def parse():
    "parse command line arguments"

    parser = argparse.ArgumentParser(description="Count down to an event.")
    parser.add_argument("datestr", metavar="yyyy-mm-dd", help="event year-month-day")
    parser.add_argument("timestr", metavar="hh:mm:ss", help="event hour:minte:second")
    parser.add_argument("-z", "--zone", dest="zone",
        help="timezone as [-]hh:mm, no whitespace after '-z'", 
        default="00:00")
    parser.add_argument("-c", "--count", dest="count", help="number of iterations",
        type=int, default=999999999)
    parser.add_argument("-i", "--interval", dest="interval", help="seconds between timesteps",
        type=int, default=1)
    parser.add_argument("-n", "--now", dest="show_now", help="show also current time",
        action="store_true", default=False)

    return parser


def main(argv):

    p  = parse()
    args = p.parse_args()
    datestr = args.datestr
    timestr = args.timestr
    if len(timestr) == 5:
        timestr += ':00'
    counter = args.count
    zonestr = args.zone
    interval = args.interval
    show_now = args.show_now
    launch_time = parseISOdatetime(datestr, timestr, zonestr)

    counter -= 1
    #pdb.set_trace()
    now = dt.datetime.utcnow()
    while counter >= 0 and now < launch_time:
        tminus = launch_time - now
        #print ("tminus", tminus)
        dhms = tdelta2dhms(tminus)
        sys.stdout.write ("\rT - %d %02d:%02d:%02d" % dhms)
        if (show_now):
            sys.stdout.write ("  now %02d:%02d:%02d.%06d" %
                (now.hour, now.minute, now.second, now.microsecond) )
        #pdb.set_trace()
        microsec = tminus.microseconds
        sleeptime = interval
        # Allow time to print about 0.3 sec before actual time
        # ... allow for system overhead/lag
        if microsec > 300000:
            sleeptime += 1/10
        else:
            sleeptime -= 1/10

        time.sleep(sleeptime)

        counter -= 1
        now = dt.datetime.utcnow()

    sys.stdout.write ("\n")
    if now >= launch_time:
        print ("Launch");

main(sys.argv)

# vim: set sw=4 tw=80 :
