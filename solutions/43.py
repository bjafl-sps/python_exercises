'''
An anagram is a type of word play, the result of rearranging 
the letters of a word or phrase to produce a new word or phrase,
using all the original letters exactly once; e.g., orchestra = carthorse. 
Using the word list at http://wiki.puzzlers.org/pub/wordlists/unixdict.txt, 
write a program that finds the sets of words that share the same characters
that contain the most words in them.
'''

import urllib.request
import time


def anagram():
    start = time.time()
    
    f = urllib.request.urlopen('http://wiki.puzzlers.org/pub/wordlists/unixdict.txt')
    text = f.read().decode()
    words = text.split('\n')  
    d = { ''.join(sorted(i)):[] for i in words}
    
    for i in words:
        d[''.join(sorted(i))].append(i)    
    max_len = max( len(v) for v in d.values())    
    
    for v in d.values():
        if len(v)==max_len:
            print(v)
            
    end = time.time()
    print(end - start)
    

anagram()