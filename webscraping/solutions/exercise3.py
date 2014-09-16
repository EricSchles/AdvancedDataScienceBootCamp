import requests
import grequests
import lxml.html

def get_links(urls):
    rs = (grequests.get(u) for u in urls)
    responses = grequests.map(rs)
    final_links = []
    for r in responses:
        text = r.text.encode("ascii","ignore")
        try:
            html = lxml.html.fromstring(text)
            links = html.xpath("//a/@href")
            for i in links:
                if "http" in i:
                    final_links.append(i)
        except:
            continue
    return final_links

initial = get_links(["http://www.techmeme.com"])
curr = initial
google_found = False
counter = 0
while not google_found:
    print counter
    new_links = []
    for i in curr:
        print i
        if not i.startswith("http"):
            continue
        if "https://www.google.com" in i:
            google_found = True
    links = get_links(curr)
    if links != None:
        for i in links:
            new_links.append(i)
    curr = new_links
    counter += 1
        #  else:
    #         links = get_links(i)
    #         if links != None:
    #             for i in links:
    #                 new_links.append(i)
    # curr = new_links
    
            
