space = [[0,0],[1,1],[2,2],[3,3],[1,2],[2,1],[0,3],[3,0]]
# first check how many rows
row = {}
for s in space:
	if s[0] in row:
		row[s[0]].add(s[1])
	else:
		row[s[0]] = {s[1]}
area = -1
for r1 in row.keys():
	for r2 in row.keys():
		if r1==r2:continue
		inter = row[r1].intersection(row[r2])
		if len(inter)<2:
			continue
		for c1 in inter:
			for c2 in inter:
				if c1==c2:
					continue
				if area<0:
					area = abs((c1-c2)*(r1-r2))
				else:
					area = min(area, abs((c1-c2)*(r1-r2)))
if area<0:
	print("No rectangle")
else:
	print(area)

