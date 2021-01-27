"""Script to count number of publications with a paticular keyword by year published """

import urllib.request
import feedparser
import numpy as np

#keyword = str(novel)


base_url = 'http://export.arxiv.org/api/query?'
search_query = urllib.parse.quote("ti:novel")
i=0

papers = np.zeros((10))
# papers['2021'], papers['2020'], papers['2019'] = 
year = "2021" 
x = 0 
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
        print(papers)
        
    else: 
        x = i 
            
        break 
        
print(x)
        

    
for i in range(x, 1000):
    query = 'search_query=%s&start=%i&max_results=%i&sortBy=submittedDate&sortOrder=descending' % (search_query,
                                                             i,
                                                             i+1)

    response = urllib.request.urlopen(base_url+query).read()
    # parse the response using feedparser
    feed = feedparser.parse(response)

    if feed.entries[i]['published'][:4]=="2020":
#         print(feed.entries[i]['published'])
#         print(feed.entries[i]['title'])
        papers[1] = papers[1] + 1
        print(papers)
        
    else: 
        x = i 
            
        break 
        
print(x)    

for i in range(x, 1000):
    query = 'search_query=%s&start=%i&max_results=%i&sortBy=submittedDate&sortOrder=descending' % (search_query,
                                                             i,
                                                             i+1)

    response = urllib.request.urlopen(base_url+query).read()
    # parse the response using feedparser
    feed = feedparser.parse(response)

    if feed.entries[i]['published'][:4]=="2019":
#         print(feed.entries[i]['published'])
#         print(feed.entries[i]['title'])
        papers[2] = papers[2] + 1
        print(papers)
        
    else: 
        x = i 
            
        break 
        
print(papers)
