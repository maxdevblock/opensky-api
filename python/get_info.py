#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import datetime
import opensky_api
import demjson

api = opensky_api.OpenSkyApi()

icao24 = sys.argv[1]
callsign = sys.argv[2]

fname = "/var/root/OpenSky/{}_{}_{}.json".format(
    icao24,
    callsign,
    datetime.datetime.strftime(datetime.datetime.now(), "%Y_%m_%d")
    )
if os.path.isfile(fname):
    with open(fname, "r") as f:
        print(f.read())
else:
    resp = demjson.encode(api.get_flight(icao24=icao24, callsign=callsign))
    with open(fname, "w") as f:
        f.write(resp)
    print(resp)