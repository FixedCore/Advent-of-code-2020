instructions =  []

with open('input.txt', 'r') as infile:
	for line in infile:
		instructions.append(line.split())

executed = [False]*len(instructions)
#print(str(3 + int(instructions[5][1])))

acc = 0 #accumulator
pc  = 0 #program counter

while executed[pc]==False:
	executed[pc]=True
	print("PC: {}, ACC: {}".format(pc, acc))
	print("Instruction: " + str(instructions[pc]))
	if instructions[pc][0] == 'acc':
		acc += int(instructions[pc][1])	
		pc += 1
	elif instructions[pc][0] == 'jmp':
		pc += int(instructions[pc][1])
	elif instructions[pc][0] == 'nop':
		pc += 1
		
print("Accumulator value: {}".format(acc))
		