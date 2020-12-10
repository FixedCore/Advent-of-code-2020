adapters = []
max_adapter = 0
with open('input.txt', 'r') as infile:
	for line in infile:
		this_adapter = int(line)
		max_adapter = max(max_adapter, this_adapter)
		adapters.append(this_adapter)
		
adapters.append(max_adapter + 3)
adapters.sort()

joltage = 0

adapter_sequence = []
joltage_differences = {
1:0,
2:0,
3:0}

while len(adapters) > 0:
	min_adapter = adapters[0]
	adapters.pop(0)
	joltage_differences[min_adapter - joltage] += 1
	joltage = min_adapter
	
print("Result of multiplication: {}".format(joltage_differences[1] * joltage_differences[3]))
	