import urllib.request

with urllib.request.urlopen('http://makemepulse.com')as response:

    html = response.read()
    
