from collections import Counter
import re
f = open('MyData','r')
text = f.read()

words = re.findall(r'\b\w+\b', text.lower())

word_counts  = Counter(words)
print("Word Frequencies:\n")
for word,count in word_counts.most_common():
    print(f"{word}: {count}")
