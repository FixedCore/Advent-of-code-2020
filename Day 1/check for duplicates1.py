
numbers = set()
with open('input1.txt', 'r') as infile:
	for line in infile:
		v = int(line)
		if v in numbers:
			print("Found a duplicate: " + line)
		else:
			numbers.add(v)
	print(numbers)
	