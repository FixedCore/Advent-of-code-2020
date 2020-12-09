HISTORY_LEN = 25

input = []
with open('input.txt', 'r') as infile:
	for line in infile:
		input.append(int(line))

located_number = 0
possible_parts = set(input[:HISTORY_LEN])

for i in range(HISTORY_LEN, len(input)):
	found = False
	for part in input[i-HISTORY_LEN:i]:
		if input[i]-part in possible_parts:
			found = True
			break
			
	if found == False:
		print("Found number {} at position {}".format(input[i], i))
		located_number = input[i]
		
	possible_parts.discard(input[i-HISTORY_LEN])
	possible_parts.add(input[i])