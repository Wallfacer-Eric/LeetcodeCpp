s = [1,2,3,4,5,6,5]
if len(s)<3:
	print(max(s))
def divide(s,lo,hi):
	mid = (lo+hi)//2
	if s[mid]>s[mid-1] and s[mid]>s[mid+1]:
		return s[mid]
	if s[mid]<s[mid+1]:
		return divide(s,mid+1,hi)
	if s[mid]<s[mid-1]:
		return divide(s,lo,mid)
print (divide(s,0,len(s)))