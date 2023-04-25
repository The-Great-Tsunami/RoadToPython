Stack = [None, None, None, None, None]

# You can interpret what 'top = -1' means that the stack is empty.
#'top = -1'이 의미하는 바는 스택이 비었다는 의미로 해석하면 된다.
top = -1

#Insert Data : Push

top += 1
Stack[top] = "Coffee"

top += 1
Stack[top] = "Green Tea"

top += 1
Stack[top] = "Black Tea"


print("-----State of Stack-----")
for i in range(len(Stack)-1, -1, -1):
	print(Stack[i])

#Extract Data : Pop

print("----- ----- -----")
data = Stack[top] #Stack[top] = 2
Stack[top] = None
top -= 1
print("pop --> ", data)

data = Stack[top] #Stack[top] = 1
Stack[top] = None
top -= 1
print("pop --> ", data)

data = Stack[top] #Stack[top] = 0
Stack[top] = None
top -= 1
print("pop --> ", data)

print("-----State of Stack-----")
for i in range(len(Stack)-1, -1, -1):
	print(Stack[i])
