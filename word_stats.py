# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 01:57:24 2020

@author: botan
"""

from operator import itemgetter #For the frequency list
from time import process_time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
start = process_time()
with open('test.txt', encoding="utf8") as file: 
    lines_analysis = file.read()
characters=lines_analysis.lower().replace ('\n', '')
lines = lines_analysis.lower().splitlines()
for x in range(len(lines)):
    lines[x] = lines[x].split(" ")
file.close()
wordlist = []
unique = dict()

token = '''abcdefghijklmnopqrstuvwxyz'''
punc = '''!()-[]{};:'"\, <>./?@#$^&*_~%'''#to delete the punctiations
#but the code just deletes punctiations at beginning and end of a word to keep the meaning.
#for example, it does not delete the apostrophe in the didn't.

numbers = 'on' #if it is on, code deletes numbers


for y in range(len(lines)):
    for z in range(len(lines[y])):
        if numbers=="on":
            x = ''.join(map(lambda c: '' if c in '0123456789' else c, lines[y][z]))
        else:
            x = lines[y][z]

        q=1
        while q==1:
            q=0
            if len(x)>0:
                if x[0] in punc:  
                    x = x[1:]
                    lines[y][z]=x
                    q=1
                
            if len(x)>0:
                if x[-1] in punc:  
                    x = x[:-1]
                    lines[y][z]=x
                    q=1
        
        if len(x) == 0:
            continue
        else:
            wordlist.append(x)
            

print("The number of words are %d.\n" %len(wordlist))
s = len(wordlist)
hstgrm = []

for x in range(s):
    if wordlist[x] in unique:
        unique[wordlist[x]]+=1
    else:
        unique[wordlist[x]]=1
        hstgrm.append(len(wordlist[x])) #for histogram

unique_a = {} 
unique_a = sorted(unique) #alphabetical list
unique_o = {} #this is frequency list
unique_b = {} #this is for alphabetical occurence list


for x in unique_a:
    unique_b[x] = unique[x]
unique_o = sorted(unique_b.items(), key = itemgetter(1), reverse = True) 
print("The number of unique words are %d.\n" %len(unique))
unique_l = {}
unique_l = sorted(unique_a, key=len, reverse=True)
c=0

letter = {}
for x in range(len(hstgrm)):
    if hstgrm[x] in letter:
        letter[hstgrm[x]]+=1
    else:
        letter[hstgrm[x]]=1
        
letter = sorted(letter.items(), key = itemgetter(0), reverse = False)
g=len(unique_l[0])#this variable for aligning the frequency word list properly

#Create and Write on a file part
with open('file1.txt', 'w', encoding="utf8") as f:
    f.write("LIST SORTED BY ALPHABETICAL\n")
    print("\nLIST SORTED BY ALPHABETICAL (Top 10)\n")
    for x in unique_a:
        print(x, file=f)
        if c<10:
            print(str(c+1)+". "+x)
            c += 1
with open('file2.txt', 'w', encoding="utf8") as f:
    f.write("LIST SORTED BY FREQUENCY and PERCENTAGE\n")
    print("\nLIST SORTED BY FREQUENCY and PERCENTAGE (Top 10)\n")
    for x in unique_o:
        print("{:^{}}  {:^10}  {:.2f}%".format(x[0],g, x[1], (x[1]*100/s)), file=f)
        if c>0:
            print("{:>2}  {:>6}  {:^12}  {:.2f}%".format((11-c), x[0], (x[1]), (x[1]*100/s)))
            c -= 1
with open('file3.txt', 'w', encoding="utf8") as f:
    f.write("LIST SORTED BY LENGTH\n")
    print("\nLIST SORTED BY LENGTH (Top 10)\n")
    for x in unique_l:
        print(x, file=f)
        if c<10:
            print(str(c+1)+". "+x)
            c += 1
with open('file4.txt', 'w', encoding="utf8") as f:
    f.write("the number of characters in each word\n")
    for x in range(len(letter)):
        print("The number of {0}-letters words is {1}".format(letter[x][0],letter[x][1]), file=f)



a = max(hstgrm)-min(hstgrm)+1#bins in the histogram

plt.subplot(1,2,1)
plt.hist(hstgrm, bins = a, alpha=0.5, color='#008080',label="word", align='mid') 

plt.xlabel("lengths of the words")
plt.ylabel("occurance")

stop=process_time()
print("\n%.2f seconds(word analysis with chart)" %(stop-start))


#Letter Analysis 
letter_a = {}#for # of each letter
char_u = []

nchar = len(characters)
for x in range(1,126,1):
    if chr(x) in characters:
        if x==32:
            letter_a["space"] = characters.count(chr(x))
        else:
            letter_a["{}".format(chr(x))] = characters.count(chr(x))
        char_u.append(x)
with open('file5.txt', 'w', encoding="utf8") as f:
    f.write("the number and the percentage of each characters in the text\n\n")
    for x in (char_u):
        if x==32:
            print("space  {:^7}  {:.2f}%".format(letter_a["space"],letter_a["space"]*100/nchar), file=f)
        else:
            print("{:>3}  {:^10}  {:.2f}%".format(chr(x),letter_a[chr(x)],letter_a[chr(x)]*100/nchar), file=f)
print("\n%.2f seconds(letter analysis)" %(stop-start))  
#Line Analysis
lines_analysis=lines_analysis.splitlines()
len_of_lines=[]
for x in range(len(lines_analysis)):
    if len(lines_analysis[x]) != 0:
        len_of_lines.append(len(lines_analysis[x]))
print("\nlength of the longest line is {}".format(max(len_of_lines)))
print("length of the shortest line is {}".format(min(len_of_lines)))

a = max(len_of_lines)-min(len_of_lines)
plt.subplot(1,2,2)
plt.hist(len_of_lines, bins = a, alpha=0.5, color='#800017',label="line", align='mid') 

plt.xlabel("lengths of the lines")
plt.ylabel("")

    
stop=process_time()
print("\n%.2f seconds(line analysis)" %(stop-start))

#Word-Line Analysis
chword = []
for x in range(len(lines)):
    chword.append("{}".format(len(lines[x][0])))
    for y in range(1,len(lines[x])):
        chword[x]=chword[x]+" {}".format(len(lines[x][y]))
with open('file6.txt', 'w', encoding="utf8") as f:
    f.write("the number of words in each line\n")
    for x in range(len(lines)):
        print("{}".format(len(lines[x])), file=f)
with open('file7.txt', 'w', encoding="utf8") as f:
    f.write("the number of words in each line\n")
    for x in range(len(chword)):
        print("{}".format(chword[x]), file=f)
'''        
wc = WordCloud(collocations = False, background_color = 'white').generate(characters)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
'''
