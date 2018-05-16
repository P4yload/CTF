#!/usr/bin/python3

#removes duplicate lines from file1, prints the uniques and put only unique into new file
#0.0.0.0 LOL
#0.0.0.0 LOL

#becomes 0.0.0.0 LOL in the next file

lines = open('file1.txt', 'r').readlines()

lines_set = set(lines)

out  = open('cleaned.txt', 'w')

for line in lines_set:
    print(line)
    out.write(line)

