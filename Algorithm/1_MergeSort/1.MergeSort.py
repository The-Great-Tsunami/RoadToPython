def merge_sort(a):

    n = len(a)

#리스트의 길이 n이 1 이하일 경우, 즉 원소가 1개 이하인 경우에는 그대로 반환
    if n <= 1:
        return a

###분할

#리스트 a를 중간 위치를 기준으로 두 개의 리스트로 나눕니다. 이때, 중간 위치는 n // 2로 계산
    mid = n // 2
    g1 = merge_sort(a[:mid])
    g2 = merge_sort(a[mid:])

    result = []

###병합

#g1과 g2 둘 다 비어 있지 않는 경우에 실행
# 이때, g1과 g2 리스트의 첫 번째 원소를 비교하여 작은 값이 result 리스트에 추가
    while g1 and g2:

        if g1[0] < g2[0]:
            result.append(g1.pop(0))

        else:
            result.append(g2.pop(0))
#g1 리스트가 빌 때까지 실행
#g1 리스트에는 이전에 비교하여 작은 값이 추가된 경우, 그 값보다 큰 원소들만 남아 있게 됨.
#따라서, g1 리스트의 모든 원소를 result 리스트에 추가
    while g1:
        result.append(g1.pop(0))
# g2 리스트가 빌 때까지 실행
# g2 리스트에는 이전에 비교하여 작은 값이 추가된 경우, 그 값보다 큰 원소들만 남아 있게 됨.
# 따라서, g2 리스트의 모든 원소를 result 리스트에 추가
    while g2:
        result.append(g2.pop(0))

    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]

print(merge_sort(d))