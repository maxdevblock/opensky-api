#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import opensky_api

api = opensky_api.OpenSkyApi()

icao24 = sys.argv[1]
callsign = sys.argv[2]

fname = "/var/root/OpenSky/{}_{}.json".format(icao24, callsign)
if os.path.isfile(fname):
    with open(fname, "r") as f:
        print(f.read())
else:
    resp = str(
        api.get_flight(icao24=icao24, callsign=callsign)
        ).replace("'", "\""
        ).replace("None", "null"
        ).replace("True", "true"
        ).replace("False", "false")
    with open(fname, "w") as f:
        f.write(resp)
    print(resp)