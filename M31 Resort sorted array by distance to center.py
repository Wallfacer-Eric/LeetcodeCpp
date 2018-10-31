import bisect
a = [1,3,4,9,14,23,34,67,91,99]
center = 14
l = bisect.bisect_left(a,center)
r = bisect.bisect_right(a,center)
new = []
if l==r:
	l-=1
else:
	for i in range(l,r):
		new.append(a[i])
	l-=1
while True:
	if l<0:
		new+=a[r:]
		break
	if r>=len(a):
		temp = a[:l+1]
		temp.reverse()
		new+=temp
		break
	if center-a[l]<a[r]-center:
		new.append(a[l])
		l-=1
	elif center-a[l]>a[r]-center:
		new.append(a[r])
		r+=1
	else:
		new.append(a[l])
		new.append(a[r])
		l-=1
		r+=1
print(new)