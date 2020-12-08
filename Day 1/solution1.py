# elegant, hash based
numbers = dict()
with open('input1.txt','r') as infile:
	for line in infile:
		n = int(line)
		numbers[2020-n]=n
	
for key in list(numbers):
	if numbers[key] in numbers:
		print("Found a pair! {} * {} = {}".format(key, numbers[key], key*numbers[key]))