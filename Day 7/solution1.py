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
	
def count_ancestors_rec(anc, color, graph):
	myBag = [bag for bag in graph if bag.color == color][0]
	for parent_color in myBag.parents:
		if parent_color not in anc:
			anc.add(parent_color)
			count_ancestors_rec(anc, parent_color, graph)
	
def count_ancestors(graph, color):
	ancestors = set()
	count_ancestors_rec(ancestors, color, graph)
	return len(ancestors)
		

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
	
num = count_ancestors(bags, 'shiny gold')
print("Found {} ancestors!".format(num))
	
	
	