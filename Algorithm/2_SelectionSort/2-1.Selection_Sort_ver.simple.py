arr = [9,5,8,3,2,7,1]

# 가장 작은 놈 찾기
def find_smallest(arr):

	#배열의 가장 앞 원소를 가장 작은 원소로 우선적 지정
	smallest = arr[0]
	smallest_idx = 0

	#0번째를 제외한 나머지 원소에서 반복문을 돌림
	for i in range(1, len(arr)):

		#만약 i번쨰 원소가 현재 가장 작은 원소로 추정되는 놈보다 작으면 이제부터 걔가 제일 작다
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_idx = i

	# 가장 작은 원소의 인덱스를 반환
	return smallest_idx

# 정렬하기
def selection_sort(arr):

	new_arr = [] #정렬된 배열을 저장한 새로운 공간을 만듬

	#원래 배열의 크기 내에서
	for i in range(len(arr)):

		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr

print(selection_sort(arr))




