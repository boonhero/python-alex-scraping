import httplib2
import json
import parse_keys

# populating parse.com of my event app.
def parseMeeting(data, i):
    connection = httplib2.HTTPSConnectionWithTimeout('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/classes/Meeting', json.dumps({
        "Name": data["eventsCollection"][i]['name']['text'],
        "Description": data["eventsCollection"][i]['description']['text'],
        "StartDate": {"__type": "Date", "iso": data["eventsCollection"][i]['start']['local']},
        "EndDate": {"__type": "Date", "iso": data["eventsCollection"][i]['end']['local']},
        "Address": data["eventsCollection"][i]['venue']['longaddress'],
        "Location":
       {
         "__type": "GeoPoint",
         "latitude": float(data["eventsCollection"][i]['venue_latlong'][0]),
         "longitude": float(data["eventsCollection"][i]['venue_latlong'][1])
       },
        "MeetingPicUrl": data["eventsCollection"][i]['logo']['url'],
         "StartUtc": {"__type": "Date", "iso": data["eventsCollection"][i]['start']['utc']},
         "EndUtc": {"__type": "Date", "iso": data["eventsCollection"][i]['end']['utc']},
         "Timezone": data["eventsCollection"][i]['start']['timezone'],
         "Url": data["eventsCollection"][i]['url'],
         "IsVisible": data["eventsCollection"][i]['shareable'],
         "Price": data["eventsCollection"][i]['price_range'],
         "Currency": data["eventsCollection"][i]['currency'],
         "Category": data["eventsCollection"][i]['category']['name'] if 'category' in data["eventsCollection"][i] else "",
         # "EventType": {"__type": "Pointer", "className": "EventType", "objectId": "11PJfsLKVG"},
        "EventType": data["eventsCollection"][i]['format']['short_name'],
         "Capacity": data["eventsCollection"][i]['capacity'],
         "NextOccurrence": {"__type": "Date", "iso": data["eventsCollection"][i]['next_occurrence']['local']},
         "CreatedBy": { "__type": "Pointer", "className": "_User", "objectId": "u7mg8bh3Dl" },
        "MeetingType": "OPEN",
        "Type": "EVENT"
         }), {
           "X-Parse-Application-Id": parse_keys.PARSE_APP_ID,
           "X-Parse-REST-API-Key": parse_keys.REST_KEY,
           "Content-Type": "application/json"
         })
    res = str(connection.getresponse().read())
    print(res)



