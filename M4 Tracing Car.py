car = "-----1--3------2---4--"
car = car.replace("-","")
car = list(car)
if len(car)<1: print([])
if len(car)==1: print([1])
start = car[0]
ans = [1]
for i in range(1,len(car)):
	if car[i]>=start:
		ans[-1]+=1
	else:
		start = car[i]
		ans.append(1)
print(ans)