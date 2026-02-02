import requests
print("test 1!")
response = requests.get("https://api.github.com")
print(response.status_code)
