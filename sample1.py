import re

def asint(n):
	return int(n)

file1 = open("assign2.txt", "r")

Lines = file1.readlines()

numlst = []

sum1 = 0

for line in Lines:
	l = re.findall("[0-9]+", line)
	if len(l)!=0:
		s = sum(list(map(asint, l)))
		sum1 = sum1 + s

		
print(sum1)