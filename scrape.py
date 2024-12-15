import requests
url = input("input url")
r =requests.get("http://archive.org/wayback/available?url="+url)