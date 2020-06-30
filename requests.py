import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'area':75, 'rooms':2, 'bathroom':2, 'hoa (R$)':1000 })

print(r.json())