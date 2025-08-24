
## ---- Processing an API Response ---------------------------------------------
import requests
import plotly.express as px

### Make an API call and check the response status ----
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url=url, headers=headers)
print(f"Status code is: {r.status_code}")

### Convert the response object to a dictionary ----
response = r.json()
repo_dicts = response["items"]

### Print details therein ----
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict["name"]}")
    print(f"Owner: {repo_dict["owner"]["login"]}")
    print(f"Repo description: {repo_dict["description"]}")
    print(f"Forks: {repo_dict["forks"]}")
    print(f"License: {repo_dict["license"]["name"]}")

### Plot a bar counting the most-rated repos ----
names, starts, forks = [], [], []

for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    starts.append(int(repo_dict["stargazers_count"]))
    forks.append(int(repo_dict["forks_count"]))

px.bar(
    x=names, 
    y=starts,
    labels={"x": "Repos", "y": "Stars"}
)

px.bar(
    x=names,
    y=forks,
    labels={"x": "Repos", "y": "Forks"}
)
