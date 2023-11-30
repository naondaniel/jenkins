import requests
response = requests.post("http://localhost:5001/whatismyname")
# print(response.text)
expected = "saved new car"
actual = response.text
assert expected == actual

