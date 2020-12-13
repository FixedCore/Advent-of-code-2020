with open('input.txt', 'r') as infile:
	my_timestamp = int(infile.readline())
	buses_line = infile.readline()
	
buses = [int(stamp) for stamp in buses_line.split(',') if stamp != 'x']

found = False
current_stamp = my_timestamp
while not found:
	for bus in buses:
		if current_stamp % bus == 0:
			print("Found a solution! Bus {} departs at {}, so the answer is {}".format(bus, current_stamp, bus *(current_stamp - my_timestamp)))
			found = True
			break
	current_stamp += 1
	