intervals = [[1,3],[4,6],[8,12]]
cuts = [1.5,2,5,7,13]
intervals.sort(key=lambda x:x[1])
cuts.sort()
hit = 0
i = 0
for cut in cuts:
	while i<len(intervals) and intervals[i][1]<cut:
		i+=1
	if i< len(intervals) and intervals[i][0]<=cut:
		hit+=1
print(hit)