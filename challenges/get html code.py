import urllib.request

with urllib.request.urlopen('http://sololearn.com')as response:

    html = response.read()
    
