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
		
geo_dirs = ['N','E','S','W']
current_dir_index = 1
posX = 0
posY = 0

for dir in directions:
	if dir[0]=='L':
		current_dir_index = (current_dir_index - dir[1]//90) % 4
	elif dir[0]=='R':
		current_dir_index = (current_dir_index + dir[1]//90) % 4
	elif dir[0]=='F':
		dir[0]=geo_dirs[current_dir_index]
		
	if dir[0]=='N':
		posY += dir[1]
	elif dir[0]=='E':
		posX += dir[1]
	elif dir[0]=='S':
		posY -= dir[1]
	elif dir[0]=='W':
		posX -= dir[1]

		
print(abs(posX)+abs(posY))