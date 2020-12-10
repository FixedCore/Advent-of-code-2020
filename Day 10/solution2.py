adapters = []
max_adapter = 0
with open('input.txt', 'r') as infile:
	for line in infile:
		this_adapter = int(line)
		max_adapter = max(max_adapter, this_adapter)
		adapters.append(this_adapter)
		
adapters.append(max_adapter+3)
adapters.append(0)
adapters.sort()

options = 1
l = len(adapters)
partial_sums = [0]*len(adapters)
partial_sums[0]=1

for i in range(1, l):
	partial_sums[i] = sum([partial_sums[j] for j in range(i-3,i) if j >= 0 and adapters[i] - adapters[j] <=3])

print(partial_sums[l-1])