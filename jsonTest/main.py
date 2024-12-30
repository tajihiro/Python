import requests

url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)
status_code = res.status_code
print(status_code)
print(res.json())
datum = res.json()[0]
print(datum)