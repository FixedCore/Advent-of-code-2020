def find_next_seat(map, start_pos, xdir, ydir):
	if xdir==0 and ydir==0:
		return False
		
	xpos = start_pos[1]+xdir
	ypos = start_pos[0]+ydir
	
	while ypos >= 0 and ypos < len(map) and xpos >= 0 and xpos < len(map[ypos]):
		if map[ypos][xpos] == '#':
			return True
		elif map[ypos][xpos] == 'L':
			return False
		xpos += xdir
		ypos += ydir
	return False

def count_neighbors(map, row, seat):
	ret = 0
	for xdir in [-1, 0, 1]:
		for ydir in [-1, 0, 1]:
			if find_next_seat(map, (row, seat), xdir, ydir):
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
			
			if lobby[active][row_nr][seat_nr] == '#' and n >= 5:
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

