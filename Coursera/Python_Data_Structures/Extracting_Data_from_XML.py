import urllib
import xml.etree.ElementTree as ET

result = 0

url = raw_input('Enter URL: ')
print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

root = ET.fromstring(data)
for count in root.iter('count'):
    result += int(count.text)

print 'Result: ' + str(result)
