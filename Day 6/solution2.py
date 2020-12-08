def prepare_alphabet():
	alphabet = set()
	for i in range(ord('a'), ord('z')+1):
		alphabet.add(chr(i))
	return alphabet
		

sum = 0
current_set = prepare_alphabet()

with open('input.txt', 'r') as infile:
	for line in infile:
		if line == '\n':
			print(len(current_set))
			sum += len(current_set)
			current_set = prepare_alphabet()
		else:
			person_set = set()
			for c in line:
				person_set.add(c)
			current_set = current_set.intersection(person_set)
	
sum += len(current_set)
print(sum)
	
