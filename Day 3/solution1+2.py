map = []
with open('input.txt','r') as infile:
	for line in infile:
		map.append(line)
		
height = len(map)
width = len(map[0]) -1

tree_options=dict()


for direction in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
	pos_down = 0
	pos_right=0
	tree_counter=0
	
	while pos_down < height:
		if map[pos_down][pos_right % width] == '#':
			tree_counter += 1
		pos_right +=direction[0]
		pos_down += direction[1]
	tree_options[direction] = tree_counter
	

print(tree_options)
tree_multiplied = 1
for val in tree_options.values():
	tree_multiplied *= val
print("Multiplied: " + str(tree_multiplied))
