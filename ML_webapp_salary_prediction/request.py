import requests 

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':1.0})
print(r.json())