# 큐가 꽉 찼는지 확인하는 함수

def isQueueFull():
	global SIZE, Queue, front, rear

	if (rear == SIZE-1 and front == -1):
		return True
	elif (rear != SIZE-1):
		return False
	else:
		for i in range(front+1, SIZE):
			Queue[i-1] = Queue[i]
			Queue[i] = None
		front -= 1
		rear -= 1
		return False

# 큐에 데이터를 삽입하는 함수

def enQueue(data):
	global SIZE, Queue, front, rear

	if isQueueFull():
		print("Queue is Full")
		return
	rear += 1
	Queue[rear] = data

# 큐가 비었는지 확인하는 함수

def isQueueEmpty():
	if (rear == front):
		return True
	else:
		return False

# 큐에서 데이터를 추출하는 함수

def deQueue():
	global SIZE, Queue, front, rear

	if isQueueEmpty():
		print("Queue is Empty")
		return None
	front += 1
	data = Queue[front]
	Queue[front] = None
	return data

# 큐에서 추출될 데이터를 확인하는 함수

def peek():
	if isQueueEmpty():
		print("Queue is Empty")
		return None
	retdata = Queue[front+1]
	return retdata

if __name__ == "__main__":
	SIZE = 5
	Queue = [None for _ in range(SIZE)]
	front = rear = -1

	while True:
		print("----- ----- -----")
		select = input("Insert(I) / Extract(E) / Verify(V) / eXit(X)")
		print("----- ----- -----")

		if select == 'I' or select == 'i':
			data = input("Enter the data to be inserted.")
			enQueue(data)

			print("----- Queue State -----")
			print("front = ", front, " | rear = ", rear)
			print('[Exit] <--', end=' ')

			for i in range(0, len(Queue), 1):
				print(Queue[i], end=' ')
			print('<-- [Start]')
			print("----- ----- ----- -----")


		elif select == "E" or select == "e":
			data = deQueue()
			print("Extracted Data -->", data)

			print("----- Queue State -----")
			print("front = ", front, " | rear = ", rear)
			print('[Exit] <--', end=' ')

			for i in range(0, len(Queue), 1):
				print(Queue[i], end=' ')
			print('<-- [Start]')
			print("----- ----- ----- -----")


		elif select == "V" or select == "v":
			data = peek()
			print("Verified Data -->", data)

			print("----- Queue State -----")
			print("front = ", front, " | rear = ", rear)
			print('[Exit] <--', end=' ')

			for i in range(0, len(Queue), 1):
				print(Queue[i], end=' ')
			print('<-- [Start]')
			print("----- ----- ----- -----")


		else:
			break

	print("Exit!!!")