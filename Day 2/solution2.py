def is_valid(line):
	dash_index = line.find('-')
	for i in range(dash_index, len(line)):
		if(line[i].isalpha()):
			first_letter_index=i
			break
	num_first = int(line[0:dash_index])
	num_last = int(line[dash_index+1:first_letter_index])
	required_letter = line[first_letter_index]
	
	password = line[line.find(':')+1:]
	return (password[num_first]==required_letter) != (password[num_last]==required_letter) # letter present on exactly 1 of the positions

valid_num = 0
with open('input.txt', 'r') as infile:
	for line in infile:
		if is_valid(line):
			valid_num = valid_num + 1
			
print(valid_num)