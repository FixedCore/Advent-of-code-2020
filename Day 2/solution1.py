def is_valid(line):
	dash_index = line.find('-')
	for i in range(dash_index, len(line)):
		if(line[i].isalpha()):
			first_letter_index=i
			break
	num_min = int(line[0:dash_index])
	num_max = int(line[dash_index+1:first_letter_index])
	required_letter = line[first_letter_index]
	
	occurences = 0
	for letter in line[first_letter_index+1:]:
		if letter == required_letter:
			occurences += 1
	if num_min <= occurences and occurences <= num_max:
		return True
	else:
		return False

valid_num = 0
with open('input.txt', 'r') as infile:
	for line in infile:
		if is_valid(line):
			valid_num = valid_num + 1
		else:
			print('invalid')
			
print(valid_num)