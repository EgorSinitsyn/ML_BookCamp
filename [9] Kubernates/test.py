import requests
import json

req = {
    "url": "http://bit.ly/mlbookcamp-pants"
}

# url = 'http://localhost:9696/predict'
#url = 'http://localhost:8080/predict'
#url = 'http://176.9.120.80:9696/predict'
#url = 'http://ec2-34-242-222-140.eu-west-1.compute.amazonaws.com:9696/predict'
#url = 'http://a8f14b32b4e8447b2b6671425bc6f613-721967091.eu-west-1.elb.amazonaws.com/predict'

url = 'http://ae0b820c610ad4386ac3f2f4d7602ae5-1939140193.us-east-1.elb.amazonaws.com/predict'

response = requests.post(url, json=req)
response_json = response.json()
print(json.dumps(response_json, indent=4))