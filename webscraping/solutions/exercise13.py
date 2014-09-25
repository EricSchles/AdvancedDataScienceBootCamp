import feedparser

urls = ["http://www.huffingtonpost.com/news/missing-persons/",
        "http://www.icpsr.umich.edu/icpsrweb/ICPSR/feeds/studies?fundingAgency=United+States+Department+of+Justice.+Office+of+Justice+Programs.+National+Institute+of+Justice","http://www.ncmissingpersons.org/feed/"]

for url in urls:
    feed = feedparser.parse(url)
    for key in feed.keys():
        print feed[key]
