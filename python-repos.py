import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=languange:python&sort=stars"
headers = {"Accept":  "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
#  The reposnse object is in JSON format, and the json() method converts the information 
# to a Python dictionary.
response_dict = r.json()

# Process results.
print(response_dict.keys())