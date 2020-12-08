def test_run_ends(instr, start, visited):
	pc = start
	#visited = [False]*len(instr)
	while visited[pc]==False:
		visited[pc]=True
		if instr[pc][0]=='acc' or instr[pc][0]=='nop':
			pc += 1
		else:
			pc += int(instr[pc][1])
		
		if pc >= len(instr):
			return True
	return False

	
# ENTRY POINT
instructions =  []

with open('input.txt', 'r') as infile:
	for line in infile:
		instructions.append(line.split())

visited = []

pc = 0
acc = 0
#marking all the visited oness
while pc not in visited:
	visited.append(pc)
	if instructions[pc][0] == 'jmp':
		pc += int(instructions[pc][1])
	elif instructions[pc][0] == 'acc':
		acc += int(instructions[pc][1])
		pc += 1
	elif instructions[pc][0] == 'nop':
		pc += 1
		
print("Finished! PC = {}, ACC = {}".format(pc, acc))

visited_in_test = [False]*len(instructions)

for starting_point in visited:
	if instructions[starting_point][0]=='nop':
		instructions[starting_point][0]='jmp'
		visited_in_test[starting_point]=False
		res = test_run_ends(instructions, starting_point, visited_in_test)
		if res:
			print("Found one! Changed position {} from NOP to JMP".format(starting_point))
			break
		else:
			instructions[starting_point][0]='nop'
			
	elif instructions[starting_point][0]=='jmp':
		instructions[starting_point][0]='nop'
		visited_in_test[starting_point]=False
		res = test_run_ends(instructions, starting_point, visited_in_test)
		if res:
			print("Found one! Changed position {} from JMP to NOP".format(starting_point))
			break
		else:
			instructions[starting_point][0]='jmp'

visited = []

pc = 0
acc = 0

while pc < len(instructions) and pc not in visited:
	visited.append(pc)
	if instructions[pc][0] == 'jmp':
		pc += int(instructions[pc][1])
	elif instructions[pc][0] == 'acc':
		acc += int(instructions[pc][1])
		pc += 1
	elif instructions[pc][0] == 'nop':
		pc += 1
		
print("Finished! PC = {}, ACC = {}".format(pc, acc))