
import requests

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.post(url,)
print(response.json())
