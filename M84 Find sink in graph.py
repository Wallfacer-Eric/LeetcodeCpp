people = villagers
while len(people)>1:
	if know(people[0],people[1]):
		people.pop(0)
	else:
		people.pop(1)
for i in villagers:
	if i==people[0]: continue
	if know(people[0],i) or not know(i,people[0]):
		return False
return True