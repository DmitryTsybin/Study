import urllib
import json

result = 0

url = raw_input('Enter URL: ')
print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'


info = json.loads(data)
print 'Comments count:', len(info['comments'])

for item in info['comments']:
    result += int(item['count'])

print 'Result: ' + str(result)
