# -*- coding: utf-8 -*-

"""
Created on Fri Mar 26 12:04:42 2021

@author: jc550631

"""

# Paragraph level Sentiment analysis

from vaderSentiment import SentimentIntensityAnalyzer
# or use this line( if there is an import error) from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like the above line
  


sentences = ["This first practical took longer than I initially expected, as many elements of java have been forgotten since my last programming class involving it. This made creating the initial game class logic code quite difficult as I had to relook at previous examples from the Programming III class to refamiliarize myself. After this however, I felt more confident and proceeded to write the XML and main activity code quite easy as it was similar to work.  "  
             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))
    
    
    
#Sentence level Sentiment Analysis  
from vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer


sentences = ["This first practical took longer than I initially expected, as many elements of java have been forgotten since my last programming class involving it.  "  
             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))