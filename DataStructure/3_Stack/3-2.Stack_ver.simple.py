#When inserting, you should check if the stack is already full.
# 삽입할 때는 스택이 이미 꽉차있는지 확인해야한다.

# Therefore, you must first check if the stack is full before inserting data. If the value of top is -1, then the stack is full.
# 따라서 먼저 스택이 꽉 차있는지 확인한 후 데이터를 삽입해야한다. 만약 top 값이 -1이라면 스택은 꽉찬 상태이다.

def isStackFull():
	global SIZE, stack, top
	if (top >= SIZE-1):
		return True
	else:
		return False

def isStackEmpty():
	global SIZE, stack, top
	if (top == -1):
		return True
	else:
		return False

def push(data):
	global SIZE, stack, top

	if (isStackFull()):
		print("Stack is full!")
		return
	top += 1
	stack[top] = data

def pop():
	global SIZE, stack, top

	if(isStackEmpty()):
		print("Stack is Empty")
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek():
	global SIZE, stack, top

	if(isStackEmpty()):
		print("Stack is Empty")
		return None
	data = stack[top]
	return data

if __name__ == '__main__':

	SIZE = int(input("Enter the size of the stack."))  # size of stack
	stack = [None for _ in range(SIZE)]
	top = -1

	while True:
		print("----- ----- -----")
		select = input("Insert(I) / Extract(E) / Verify(V) / eXit(X)")
		print("----- ----- -----")

		if select == 'I' or select == 'i':
			data = input("Enter the data to be inserted.")
			push(data)

			print("-----State of Stack-----")
			for i in range(len(stack) - 1, -1, -1):
				print(stack[i])

		elif select == "E" or select == "e":
			data = pop()
			print("Extracted Data -->", data)

			print("-----State of Stack-----")
			for i in range(len(stack) - 1, -1, -1):
				print(stack[i])

		elif select == "V" or select == "v":
			data = peek()
			print("Verified Data -->", data)

			print("-----State of Stack-----")
			for i in range(len(stack) - 1, -1, -1):
				print(stack[i])

		else:
			break

	print("Exit!!!")
