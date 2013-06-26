import sys



file = open(' ') # Enter the text file with the list of words and ratings here
scores = {}
for line in file:
    term, score = line.split("\t")
    scores[term] = int(score)

print scores.items() # Print every (term, score) pair in the dictionary

def lines(fp):
    print str(len(fp.readlines()))
