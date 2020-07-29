# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:38:58 2020

@author: Ikhwanul Muslimin
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving:', url)
html = urllib.request.urlopen(url, context=ctx)
data = html.read()

print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
results = tree.findall('.//count')

print('Count:',len(results))

total = 0
for num in results:
    total = total + int(num.text)
    
print('Sum:',total)