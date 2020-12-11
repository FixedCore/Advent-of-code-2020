def count_neighbors(map, row, seat):
	ret = 0
	for i in range(row-1, row+2):
		for j in range(seat-1, seat+2):
			if i >=0 and i < len(map) and j >= 0 and j < len(map[row]) and (j != seat or i != row):
				if map[i][j] == '#':
					ret += 1
	return ret

from copy import deepcopy
lobby = [[],[]]
with open('input.txt', 'r') as infile:
	for line in infile:
		lobby[0].append([])
		for c in line:
			if c != '\n':
				lobby[0][len(lobby[0])-1].append(c)

lobby[1] = deepcopy(lobby[0])

active = 0
changed = True
while changed == True:
	changed = False
	for row_nr in range(len(lobby[active])):
		for seat_nr in range(len(lobby[active][0])):
			n = count_neighbors(lobby[active], row_nr, seat_nr)
			
			if lobby[active][row_nr][seat_nr] == 'L' and n == 0:
				lobby[1-active][row_nr][seat_nr] = '#'
				changed = True
			
			if lobby[active][row_nr][seat_nr] == '#' and n >= 4:
				lobby[1-active][row_nr][seat_nr] = 'L'
				changed = True
	lobby[active] = deepcopy(lobby[1-active])
	active = 1-active

taken = 0
for row in lobby[active]:
	for seat in row:
		if seat == '#':
			taken += 1
			
print(taken)

