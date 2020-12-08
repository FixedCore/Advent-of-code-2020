class Bag:
	def __init__(self, color):
		self.color = color # string, 2 words
		self.parents = set() # set of strings, parent's names
		self.children = set() # set of tuples, child's name and number of this kind
		
	def give_parent(self, parent):
		self.parents.add(parent)
		
	def give_parents(self, parents):
		for p in parents:
			self.parents.add(p)
		
	def give_child(self, child):
		self.children.add(child)
		
	def give_children(self, children):
		for c in children:
			self.children.add(c)
			
	def __str__(self):
		return self.color + ", parents: " + str(self.parents) + ", children: " + str(self.children)

def splitIntoBags(line):
	if line[0]=="s contain no other":
		return []
		
	bags = []
	for token in line:
		words = token.split()[-3:]
		num = int(words[0])
		color = " ".join(words[1:])
		bags.append((color, num))
	return(bags)
	
def count_descendants_rec(graph, color, sum, mul):
	myBag = [bag for bag in graph if bag.color == color][0]
	for child in myBag.children:
		sum[0] += (child[1] * mul)
		count_descendants_rec(graph, child[0], sum, child[1]*mul)
	
def count_descendants(graph, color):
	sum = [0]
	count_descendants_rec(graph, color, sum, 1)
	return sum[0]

lines = []
with open('input.txt', 'r') as infile:
	for line in infile:
		tokens = [t.strip() for t in line.split('bag')]
		lines.append(tokens)

bags = set()
for line in lines:
	containing = line[0]
	contained = splitIntoBags(line[1:-1])
	# print(str(containing) + " === " + str(contained))
	
	thisBagCandidates = [bag for bag in bags if bag.color == containing]
	
	if len(thisBagCandidates) >= 1:
		thisBag = thisBagCandidates[0]
	else:
		thisBag = Bag(containing)
		bags.add(thisBag)
	
	thisBag.give_children(contained)
	
	for child in contained:
		child_candidates = [bag for bag in bags if bag.color == child[0]]
		
		if len(child_candidates) >= 1:
			this_child = child_candidates[0]
		else:
			this_child = Bag(child[0])
			bags.add(this_child)
		this_child.give_parent(thisBag.color)
	
#for bag in bags:
#	print(bag)
	
num = count_descendants(bags, 'shiny gold')
print("Found {} descendants!".format(num))
	
	
	