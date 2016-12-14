#!/usr/bin/python
from plistlib import readPlist

plist = readPlist('/Library/Preferences/SystemConfiguration/preferences.plist')
commRemoteAddress = []

for item in plist['NetworkServices']:
    if plist['NetworkServices'][item]['Interface']['Type'] == 'IPSec':
        commRemoteAddress.append(plist['NetworkServices'][item]['IPSec']['RemoteAddress'])
try:
    print '<result>%s</result>' % ', '.join(map(str, commRemoteAddress))
except KeyError:
    print '<result></result>'
