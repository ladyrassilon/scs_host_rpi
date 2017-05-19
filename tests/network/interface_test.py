#!/usr/bin/env python3

"""
Created on 4 Nov 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.data.json import JSONify

from scs_host.network.interface import Interface


# --------------------------------------------------------------------------------------------------------------------

interfaces = Interface.find_all()

for interface in interfaces:
    print(interface)
print("-")


print(JSONify.dumps(interfaces))
print("-")


interface = Interface.find("wlan0")
print(interface)
print("-")

