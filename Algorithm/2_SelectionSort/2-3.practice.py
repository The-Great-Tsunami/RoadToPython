max = 30
a =[75,25,6,73,43,46,31,13,60,90,5,43,35,100,28,83,95,35,45,-1]
rank = [0] * max

i = 0
while a[i] != -1:
	rank[i] = 1
	j = 0

	while a[j] != -1:
		if a[j] > a[i]:
			rank[i] += 1
		j += 1
	i += 1

for i in range(len(a)):
	print('%6d점 -> %3d' %(a[i], rank[i]))