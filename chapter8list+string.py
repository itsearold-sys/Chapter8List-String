first = open('mbox-short.txt.txt')

count = 0

for line in first:
    line = line.strip()

if line.startswith('From '):
    word = line.split()
print(word[1])






















