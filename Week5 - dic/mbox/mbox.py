'''  Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.'''
fh = open('mbox.txt')
dictionary = dict()
biggestNumber = None
sender = ''
for line in fh:
    print (line)
    words = line.split()
    if 'From' in words:
            dictionary[words[1]] = dictionary.get(words[1], 0) + 1

for keys, values in dictionary.items():
    
    if biggestNumber is None or values > biggestNumber:
        biggestNumber = values
        sender = keys

print (sender, biggestNumber)