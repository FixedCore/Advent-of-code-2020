def find_alpha(txt):
	for i in range(len(txt)):
		if txt[i].isalpha():
			return i
	return -1

def validate_height(h_field):
	height = int(h_field[:find_alpha(h_field)])
	if h_field.find('in') != -1:
		if height >= 59 and height <= 76:
			return True
	elif h_field.find('cm') != -1:
		if height >= 150 and height <= 193:
			return True
	return False

	
def validate_hcl(hcl_field):
	if len(hcl_field) != 7:
		return False
	if hcl_field[0] != '#':
		return False
	for letter in hcl_field[1:]:
		if not letter.isnumeric() and letter not in ['a', 'b', 'c', 'd', 'e', 'f']:
			return False
	return True

def validate_fields(passport):
	if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
		return False
	if len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
		return False
	if len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
		return False
	if not validate_height(passport['hgt']):
		return False
	if not validate_hcl(passport['hcl']):
		return False
	if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False
	if len(passport['pid']) != 9 or not passport['pid'].isnumeric():
		return False
	return True
	
	


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
def is_valid(passport):
	fields = passport.split()
	pass_dict = dict()
	for field in fields:
		separated = field.split(':')
		pass_dict[separated[0]] = separated[1]
	for req in required_fields:
		if req not in pass_dict.keys():
			return 0
	
	
	if validate_fields(pass_dict):
		return 2
	return 1


passports = []
with open('input.txt', 'r') as infile:
	passport_line = ""
	for line in infile:
		if line == "\n":
			passports.append(passport_line)
			passport_line = ""
		else:
			passport_line += line
passports.append(passport_line)

valid1_num=0
valid2_num=0
total_num=0

for passport in passports:
	total_num+=1
	ret = is_valid(passport)
	if ret > 0:
		valid1_num += 1
	if ret > 1:
		valid2_num += 1
		
print("Total passports: " + str(total_num))
print("Siply validated passports: " + str(valid1_num))
print("Complex validated passports: " + str(valid2_num))