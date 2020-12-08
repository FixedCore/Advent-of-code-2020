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
	highest_seat = 0
	for line in infile:
		seat_nr = get_seat_nr(line)
		highest_seat = max(highest_seat, seat_nr)

print("Highest seat number: " + str(highest_seat))