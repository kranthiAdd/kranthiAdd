# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:18:10 2021

@author: jc550631
"""

from afinn import Afinn
from nltk.corpus import gutenberg
import textwrap
afinn = Afinn()
sentences = (" ".join(wordlist) for wordlist in gutenberg.sents('austen-sense.txt'))
scored_sentences = ((afinn.score(sent), sent) for sent in sentences)
sorted_sentences = sorted(scored_sentences)
print("\n".join(textwrap.wrap(sorted_sentences[0][1], 70)))
#print(scored_sentences)
print (sorted_sentences)

# splitting paragraph into sentences and giving afinn score to eah of the sentences.

from afinn import Afinn

selfReflection = "This first practical took longer than I initially expected, as many elements of java have been " \
                 "forgotten since my last programming class involving it. This made creating the initial game " \
                 "class logic code quite difficult as I had to relook at previous examples from the Programming III " \
                 "class to refamiliarize myself. After this however, I felt more confident and proceeded to write the " \
                 "XML and main activity code quite easy as it was similar to work"
               

sentences = filter(lambda s: len(s) != 0, selfReflection.strip().split("."))

afinn = Afinn()
for sentence in sentences:
    print (sentence, afinn.score(sentence))
