HISTORY_LEN = 25

input = []
with open('input.txt', 'r') as infile:
	for line in infile:
		input.append(int(line))

located_number = 0
possible_parts = set(input[:HISTORY_LEN])

# O(len(input) * HISTORY_LEN)
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

pos_lo = 0
pos_hi = 2

# O(len(input)), yay!
while pos_hi <= len(input):
	s = sum(input[pos_lo:pos_hi])
	if s == located_number:
		print("Found a range! Positions from {} to {}".format(pos_lo, pos_hi))
		break
	elif s < located_number:
		pos_hi += 1
	elif s > located_number:
		pos_lo += 1

min_weakness = min(input[pos_lo:pos_hi])
max_weakness = max(input[pos_lo:pos_hi])
print("The resulting weakness is {} + {} = {}".format(min_weakness, max_weakness, min_weakness+max_weakness))