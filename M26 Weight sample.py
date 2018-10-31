import random
import bisect
country = [('CHN',70),('USA',30)]
cumulate = []
s = 0
for c in range(len(country)):
	cumulate.append(country[c][1]+s)
	s+=country[c][1]
res = 0
for i in range(10000):
	sample = random.randint(1,s)
	res+=bisect.bisect_left(cumulate,sample)
print (res)