# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 12:11:14 2021

@author: jc550631
"""

with open("Course-Descriptions.txt", 'r') as fh:  
    filedata = fh.read()
#    print("File data sample : ", filedata[:200])
    
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)
#print("stopwords in the package: ",  stopwords)
wordcloud = WordCloud(stopwords=stopwords, max_words=25, \
                      background_color="white").generate(filedata)
import matplotlib.pyplot as mpLib
mpLib.imshow(wordcloud)
mpLib.axis("off")
mpLib.show()

stopwords.update(["many","using", "want", "value"])
print(" stopwords now in the pacakge: ", stopwords)

wordcloud = WordCloud(stopwords=stopwords, max_words=25, \
                      background_color="white").generate(filedata)

import matplotlib.pyplot as mpLib
mpLib.imshow(wordcloud)
mpLib.axis("off")
mpLib.show()
