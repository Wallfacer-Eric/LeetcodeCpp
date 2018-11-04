str1="google"
str2="egle"
str1=list(str1)
str2=list(str2)
set1=set(str1)
set2=set(str2)
set2 = set1.intersection(set2)
i=0
while i<len(str2):
	if str2[i] in set2:
		i+=1
	else:
		str2 = str2[:i]+str[i+1:]
i=0
j=0
while i<len(str1) and j<len(str2):
	if str1[i]!=str2[j]:
		i+=1
	else:
		i+=1
		j+=1
if j!=len(str2):
	print(False)
else:
	print(True)