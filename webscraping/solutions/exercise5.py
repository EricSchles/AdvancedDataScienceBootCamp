import requests
import lxml.html

def pdf_grab(url):
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    links = html.xpath("//a/@href")
    pdfs = []
    for i in links:
        if "pdf" in i:
            pdfs.append(i)

    for i in pdfs:
        url = i
        file_name = url.split("/")[-1]
        with open(file_name,"wb") as f:
            r = requests.get(url)
            f.write(r.content)

base_url = "http://www.nyc.gov/html/dof/html/forms_reports/property_forms_exemption.shtml"

r = requests.get(base_url)
html = lxml.html.fromstring(r.text)
links = html.xpath("//a/@href")
for i in links:
    if "forms_reports" in i:
        pdf_grab(i)
