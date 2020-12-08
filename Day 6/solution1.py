groups = []
ppl_in_group = ""
with open('input.txt', 'r') as infile:
	for line in infile:
		if line == '\n':
			groups.append(ppl_in_group)
			ppl_in_group = ""
		else:
			ppl_in_group += line
	groups.append(ppl_in_group)
	
sum = 0
for g in groups:
	answered = set()
	for c in g:
		if c != '\n':
			answered.add(c)
	sum += len(answered)
	print(sum)
	
	