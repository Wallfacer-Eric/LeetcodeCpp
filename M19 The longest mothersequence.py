d = {"Amazon","eabay","ebey","ekkbay","gtebay"}
s = "ebay"
longseq = ""
longnum = 0
seqq=[]
ls = len(s)
for seq in d:
	print(seq)
	i=0
	j=0
	while i<ls and j<len(seq):
		if s[i]==seq[j]:
			i+=1
			j+=1
		else:
			j+=1
	if i==ls:
		seqq.append(seq)
		if len(seq)>longnum:
			longseq=seq
			longnum=len(seq)
print(longseq)
print(seqq)