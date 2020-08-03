9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.' \
temp = None
highest = None
counts = dict()
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
for line in handle:

    words = (line.split())
    for word in words: #histogram part
        if word == "From":
            i = words.index(word)
            counts[words[i + 1]] = counts.get(words[i + 1], 0) + 1
for words, count in counts.items():#Find largest count
    if count is None or temp < count:
        temp = count
        highest = words

print(highest, temp)
