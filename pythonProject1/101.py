
if response.status_code == 200:
    print("github is running")
repositories = response.json()

for i in repositories:
    if "DEVOPS" in i["name"].upper():
        print(i["name"])