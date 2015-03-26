#!/usr/bin/env python

import time
import sys
from pprint import pprint
from zapv2 import ZAPv2


# Call this with atack.py http://target.domain.com
# Note - you must include http://
target = str(sys.argv[1])

# Use the line below if ZAP is not listening on 8090
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# do stuff
print 'Accessing target %s' % target
# try have a unique enough session...
zap.urlopen(target)
# Give the sites tree a chance to get updated
time.sleep(2)

print 'Spidering target %s' % target
zap.spider.scan(target)
# Give the Spider a chance to start
time.sleep(2)
while (int(zap.spider.status) < 100):
    print 'Spider progress %: ' + zap.spider.status
    time.sleep(2)

print 'Spider completed'
# Give the passive scanner a chance to finish
time.sleep(5)

print 'Scanning target %s' % target
zap.ascan.scan(target)
while (int(zap.ascan.status) < 100):
    print 'Scan progress %: ' + zap.ascan.status
    time.sleep(5)

print 'Scan completed'

# Report the results

print 'Hosts: ' + ', '.join(zap.core.hosts)
print 'Alerts: '
pprint (zap.core.alerts())
