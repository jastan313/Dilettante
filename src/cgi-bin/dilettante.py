#!C:\Users\Jason Tan\Desktop\Python\python.exe -u

import cgi
import cgitb; cgitb.enable() # for troubleshooting
import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Exemplar")
data = r.text
soup = BeautifulSoup(data)

print("Content-type: text/html\n\n")
print("<html><head></head><body>")

for link in soup.find_all('a'):
    print(link)
    print(link.get('href'))
    print('<br>')

print("</body></html>")