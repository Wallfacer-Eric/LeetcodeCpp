salary = [1,2,3,4,5,6,7,8,2,3,5,2,5,2,5,7,1]
target = 1
salary.sort()
sum_s = [0]
for i in salary:
	sum_s.append(sum_s[-1]+i)
sum_s.pop(0)
print(salary)
print(sum_s)
for i in range(len(sum_s)-1,-1,-1):
	if sum_s[i-1]+(len(sum_s)-i)*salary[i-1]<target:
		cap = (target-sum_s[i-1])/(len(sum_s)-i)
		print(cap)
		print(i,sum_s[i-1],cap,len(sum_s)-i)
if i==0:
	print(target/len(salary))