import requests
import json

with open('newdata.json', 'r') as f:
    testdata = json.load(f)

r = requests.post('http://127.0.0.1:5000/predict', json={'newdata' : testdata})
data = r.json()
prediction = data['prediction']

counter = 0
for i in prediction:
    counter += 1
    print ('Good day to you. The probability of this being a phishing URL', counter, 'is: ', i)
