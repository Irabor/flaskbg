#!/usr/bin/env python
import urllib2
import re

def page(url):
    req = urllib2.Request(url)
    page = urllib2.urlopen(req)
    print(page.read())

page('http://ciu.edu.tr/en')
