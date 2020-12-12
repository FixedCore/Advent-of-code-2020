def findFirstNumberPosition(text):
	for i in range(len(text)):
		if text[i].isnumeric():
			return i
			
	return len(text)
	

directions = []
with open('input.txt', 'r') as infile:
	for line in infile:
		i = findFirstNumberPosition(line)
		directions.append([line[:i], int(line[i:])])
		
#geo_dirs = ['N','E','S','W']
#current_dir_index = 1
posX = 0
posY = 0
wpX = 10 #relative to the ship
wpY = 1

for dir in directions:	
	if dir[0]=='L':
		for i in range(dir[1]//90):
			tmp = wpY
			wpY = wpX
			wpX = (-1) * tmp
	elif dir[0]=='R':
		for i in range(dir[1]//90):
			tmp = wpY
			wpY = (-1)*wpX
			wpX = tmp
	elif dir[0]=='F':
		posX += wpX * dir[1]
		posY += wpY * dir[1]	
	elif dir[0]=='N':
		wpY += dir[1]
	elif dir[0]=='E':
		wpX += dir[1]
	elif dir[0]=='S':
		wpY -= dir[1]
	elif dir[0]=='W':
		wpX -= dir[1]
	
print(abs(posX)+abs(posY))