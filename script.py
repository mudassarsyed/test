import requests,json
response=requests.get('http://0.0.0.0:3000/testjsonfile')
print (json.dumps(response.json()))