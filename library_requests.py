import requests as req

response = req.get('https://api.github.com')

print(response.status_code)

print(response.text)