import requests
import lxml.html

r = requests.get("http://www.techmeme.com")
html = lxml.html.fromstring(r.text)
links = html.xpath("//a/@href")
final = []
for i in links:
    if "http" in links:
        final.append(i)
print final
#check this
