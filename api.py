import requests

donnees = {
    "username":"shinoby",
    "first_name":"William"
}

requests.post('http://localhost:8000/en/')
response = requests.get(("https://swapi.dev/api/people/1/"))
print(response.json()["name"])
print(response.headers)