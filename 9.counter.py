from collections import Counter
import re

book = open('.\Book.txt')

#Wrap  the file handling in a try except block
try:
    words = []
    for line in book.readlines():
        row = re.findall(r"\w+", line.lower())
        words.extend(row) 
    
    words_quantity = Counter(words)
    
    #sorting primarly "by value" - descending and secondary "by key" - ascending
    print(sorted(words_quantity.items(), key = lambda t: (-t[1], t[0])))
    
except (IOError, OSError):
    print("Could not read file", book)   
    
except FileNotFoundError:
    print("File not found", book)
    
finally:
    book.close()
