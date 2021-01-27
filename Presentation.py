import urllib.request
import feedparser
import numpy as np

base_url = 'http://export.arxiv.org/api/query?'
search_query = urllib.parse.quote("ti:novel")
i=0

papers = np.zeros((10))
# papers['2021'], papers['2020'], papers['2019'] = 
year = "2021" 
 
# def findPapers()
# while "published" == "2021":
for i in range(0, 1000):
    query = 'search_query=%s&start=%i&max_results=%i&sortBy=submittedDate&sortOrder=descending' % (search_query,
                                                             i,
                                                             i+1)

    response = urllib.request.urlopen(base_url+query).read()
    # parse the response using feedparser
    feed = feedparser.parse(response)

    if feed.entries[i]['published'][:4]=="2021":
#         print(feed.entries[i]['published'])
#         print(feed.entries[i]['title'])
        papers[0] = papers[0] + 1
        
    elif feed.entries[i]['published'][:4]=="2020":
        papers[1] = papers[1] + 1
        print(feed.entries[i]['published'])
#         print(feed.entries[i]['title'])
    elif feed.entries[i]['published'][:4]=="2019":
        papers[2] = papers[2] + 1
#         print(feed.entries[i]['published'])
#         print(feed.entries[i]['title'])
