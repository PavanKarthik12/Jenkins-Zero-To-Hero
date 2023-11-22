import requests
print("Status code for google.com")
print(requests.get("https://www.google.com/").status_code)


