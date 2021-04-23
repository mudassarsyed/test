from datetime import datetime
import requests,json
def jprint(obj):
    text=json.dumps(obj)
    print(text)
parameters = {
    "lat": 40.71,
    "lon": -74
}
response=requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)
responsetimes=response.json()['response']
risetimes=[]
for d in responsetimes:
    time=d['risetime']
    risetimes.append(time)

timestamptimes=[]
for rt in risetimes:
    tstime=datetime.fromtimestamp(rt)
    timestamptimes.append(tstime)
print(timestamptimes)