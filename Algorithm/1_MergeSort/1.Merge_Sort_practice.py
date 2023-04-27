def merge_Sort(a):

	n = len(a)

	if n <= 1:
		return a

	mid = n//2
	g1 = merge_Sort(a[:mid])
	g2 = merge_Sort(a[mid:])

	result = []

	while g1 and g2:

		if g1[0] < g2[0]:
			result.append(g1.pop(0))

		else:
			result.append(g2.pop(0))

	while g1:
		result.append(g1.pop(0))

	while g2:
		result.append(g2.pop(0))

	return result

d = [1,3,5,7,9,10,2,4,6,8,10]

print(merge_Sort(d))