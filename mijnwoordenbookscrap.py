#!/usr/bin/python
#https://github.com/kennethreitz/python-guide/blob/master/docs/scenarios/scrape.rst

from lxml import html
import requests
import sys
print sys.argv
import fileinput
for w in fileinput.input():
    page = requests.get('http://www.mijnwoordenboek.nl/vertaal/ES/NL/'+w)
    tree = html.fromstring(page.content)
#This will create a list of definitions
    definitions = tree.xpath('//font[@style="color:navy;font-size:10pt"]/b/text()')

    print w+': ', definitions

