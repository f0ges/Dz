import requests

a = requests.get('http://194.87.99.14/students')
b = a.json()
np = []
print(b)