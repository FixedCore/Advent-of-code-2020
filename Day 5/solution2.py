def get_seat_row(line):
	row_nr = 0
	for i in range(7):
		if line[i] == 'B':
			row_nr += (2**(6-i))
	return row_nr
	
def get_seat_col(line):
	col_nr = 0
	for i in range(7, 10):
		if line[i] == 'R':
			col_nr += (2**(9-i))
	return col_nr

def get_seat_nr(line):

	return get_seat_row(line) * 8 + get_seat_col(line)

with open('input.txt','r') as infile:
	taken_seats = set()
	for line in infile:
		taken_seats.add(get_seat_nr(line))
		
for nr in range(min(taken_seats), max(taken_seats)):
	if nr not in taken_seats and nr+1 in taken_seats and nr-1 in taken_seats:
		print("Found the seat! " + str(nr))
