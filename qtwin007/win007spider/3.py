# -*- coding: utf-8 -*-


# from urlparse import urlparse
from urllib import parse

url_str = "http://www.163.com/mail/index.htm?data=2017-05-03"
url = parse.urlparse(url_str)

print ('protocol:',url.scheme)
print ('hostname:',url.hostname)
print ('port:',url.port)
print ('path:',url.path)
print (url.query )
 
i = len(url.path) - 1
while i > 0:
    if url.path[i] == '/':
        break
    i = i - 1
print ('filename:',url.path[i+1:len(url.path)])