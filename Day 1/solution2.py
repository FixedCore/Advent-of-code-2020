# brute force xd
numbers = []
with open('input1.txt','r') as infile:
	for line in infile:
		numbers.append(int(line))

for num1 in numbers:
	for num2 in numbers:
		for num3 in numbers:
			if num1 + num2 + num3 ==2020:
				print("Found a solution! {} * {} * {} = {}".format(num1, num2, num3, num1*num2*num3))
				