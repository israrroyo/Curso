import requests
r = requests.get(url='https://api.github.com/users/razeone/repos')
print(r.json())
