with open('test_input.txt', 'r') as infile:
	my_timestamp = int(infile.readline())
	buses_line = infile.readline()
	
line_split = buses_line.split(',')

buses = [(line_split.index(x), int(x)) for x in line_split if x != 'x']

buses_d = dict()
for b in buses:
	buses_d[b[0]] = b[1]

