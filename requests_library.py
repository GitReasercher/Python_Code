import requests

response = requests.get('https://github.com/GitReasercher/Python_Code')

#Основные атрибуты ответа:
status = response.status_code # Код состояния HTTP (например, 200 для успеха)
text_content = response.text # Содержимое ответа в виде текста
json_content = response.json() # Декодирует JSON-ответ в объект Python

response = requests.get('https://api.github.com')
print(response.status_code) # 200 — успех, 404 — не найдено
print(response.text)         # Весь текст ответа

response = requests.get("https://www.google.com")

print(status)

headers = response.headers

print(headers)
print(response.text[:100])


headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get('https://www.wikipedia.org', headers = headers)

print(response.status_code)

response = requests.get('https://jsonplaceholder.typicode.com')

if response.status_code == 200:
    data = response.json()
    print(f"Заголовок поста: {data['title']}")
else:
    raise StopAsyncIteration (f'Error! Code: {response.status_code}')

