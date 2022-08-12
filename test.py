import requests
import FDS_project

print(FDS_project.dat.head())

response = requests.get("https://catfact.ninja/fact")

for i in response:
    print(i)
