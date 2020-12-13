with open('test_input.txt', 'r') as infile:
	my_timestamp = int(infile.readline())
	buses_line = infile.readline()
	
line_split = buses_line.split(',')

buses = [(line_split.index(x), int(x)) for x in line_split if x != 'x']

buses_d = dict()
for b in buses:
	buses_d[b[0]] = b[1]
	
found = False
multiplier = 1
print(buses_d)

while not found:
	num = buses_d[0] * multiplier
	valid = True
	for k in buses_d.keys():
		if (num + k) % buses_d[k] != 0:
			valid = False
			break
	if valid:
		found = True
		print("Found one! It's {}".format(num))