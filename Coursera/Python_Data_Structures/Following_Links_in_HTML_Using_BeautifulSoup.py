# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
html = urllib.urlopen(url).read()

count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

soup = BeautifulSoup(html)

urls = []

current_link = ''
while count > 0:
    tags = soup('a')
    current_link = tags[position-1].get('href', None)
    print current_link
    html = urllib.urlopen(current_link).read()
    soup = BeautifulSoup(html)
    count -= 1
