def count_options(adapters, it):
	if it == len(adapters)-1:
		return 1
	else:
		return sum([count_options(adapters, i) for i in range(it+1, it+4) if i < len(adapters) and adapters[i]-adapters[it] <= 3])

adapters = []
max_adapter = 0
with open('input.txt', 'r') as infile:
	for line in infile:
		this_adapter = int(line)
		max_adapter = max(max_adapter, this_adapter)
		adapters.append(this_adapter)
		
adapters.append(max_adapter+3)
adapters.sort()

print(count_options(adapters, 0))