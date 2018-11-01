s=['1','1','2','2','3','3','4','4','5','5','6','7','7','8','8','9','9']
def binary(s,lo,hi):
	if lo==hi: return lo
	mid = (lo+hi)//2
	idx = mid
	if mid>0 and s[mid-1]==s[mid]:
		idx=mid-1
	elif mid<len(s)-1 and s[mid+1]==s[mid]:
		idx=mid
	else:
		return mid
	if idx%2==0:
		return binary(s,mid+2,hi)
	else:
		return binary(s,lo,mid-1)
print (s[binary(s,0,len(s))])