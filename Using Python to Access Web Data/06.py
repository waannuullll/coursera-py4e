# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:13:28 2020

@author: Ikhwanul Muslimin
"""

# http://py4e-data.dr-chuck.net/comments_42.json total = total + int(item['count'])
# http://py4e-data.dr-chuck.net/comments_826574.json

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving:', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieved', len(data), 'characters')

info = json.loads(data)
total = 0
i = 0
for item in info['comments']:
    total = total + item['count']
    i = i + 1

print('Count:',i)
print('Sum:',total)