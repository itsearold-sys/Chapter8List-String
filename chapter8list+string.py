first = open('mbox-short.txt.txt')

count = 0

for line in first:
    line = line.strip()

if line.startswith('From '):
    word = line.split()
    print(word[1])
    count = count + 1

print('There were', count "lines in the file with From as the first word")






















