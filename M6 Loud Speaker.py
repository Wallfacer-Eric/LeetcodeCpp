import bisect
intervals = [[3,8],[7,10],[13,15]]
loud = [50,30,40]
for i in range(len(loud)):
	intervals[i].append(loud[i])
out = []
intervals.sort(key=lambda x:x[0])
i=0
while i<len(intervals):
	print(out)
	print(intervals)
	if out and intervals[i][0] <= out[-1][1]:
		if intervals[i][0] == out[-1][1] and intervals[i][2]!=out[-1][2]:
			out.append(intervals[i])
			i+=1
			continue
		if intervals[i][2]>out[-1][2]:
			if out[-1][1]<=intervals[i][1]:
				out[-1][1] = intervals[i][0]
				out.append(intervals[i])
			else:
				new = [intervals[i][1],out[-1][1],out[-1][2]]
				pos = bisect.bisect_left([start[0] for start in intervals],new[0])
				intervals.insert(pos,new)
		elif intervals[i][2]==out[-1][2]:
			out[-1][1] = max(out[-1][1], intervals[i][1])
		else:
			if out[-1][1]<intervals[i][1]:
				new = [out[-1][1],intervals[i][1],intervals[i][2]]
				print('new',new)
				pos = bisect.bisect_left([start[0] for start in intervals],new[0])
				intervals.insert(pos,new)
	else:
		out.append(intervals[i])
	i+=1
print(out)