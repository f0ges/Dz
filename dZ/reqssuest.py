import requests

a = requests.get('http://194.87.99.14/students')
a.encoding = 'utf-8'
b = a.text
np = []
print(b)