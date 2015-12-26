import urllib
import json

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    #print json.dumps(js, indent=4)

    location = js['results'][0]['formatted_address']
    place_id = js['results'][0]['place_id']
    print 'Location: ' + location
    print 'Place ID: ' + place_id
