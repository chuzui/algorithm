# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import re
import subprocess
addresses = ['sg1.vpnreal.com',
             'sg2.vpnreal.com',
             'us1.vpnreal.com',
             'us2.vpnreal.com',
             'us3.vpnreal.com',
             'us4.vpnreal.com',
             'us5.vpnreal.com']

avgRe = u'(?<=平均 = )[0-9]+'
avgPattern = re.compile(avgRe)

avgSpeedList = []
shortestTime = 100000
for address in addresses:

    tmp = subprocess.Popen('ping ' + address, stdout=subprocess.PIPE).stdout.readlines()
    tmpStr = ''.join((x.decode('gb2312') for x in tmp))

    print(tmpStr)
    m = avgPattern.search(tmpStr)
    if not m is None:
        speed = int(m.group())
        if shortestTime > speed:
            shortestTime = speed
            fastestAddress = address

print('the fastest address is ' + fastestAddress)
print('the average time is ' + str(shortestTime) + 'ms\n')
input()