import requests

resp = requests.post("http://localhost:8080", files={'file': open('three.png', 'rb')})

print(resp.text)

print(resp.json())