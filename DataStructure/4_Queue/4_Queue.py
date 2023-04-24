Queue = [None, None, None, None, None]
front = rear = -1

rear += 1
Queue[rear] = "화사"

rear += 1
Queue[rear] = "솔라"

rear += 1
Queue[rear] = "문별"

print("----- Queue State -----")
print("front = ", front," | rear = ", rear)
print('[Exit] <--', end = ' ')

for i in range(0, len(Queue), 1):
	print(Queue[i], end = ' ')
print('<-- [Start]')
print("----- ----- ----- -----")

front += 1
data = Queue[front]
Queue[front] = None
print('deQueue -->', data)

front += 1
data = Queue[front]
Queue[front] = None
print('deQueue -->', data)

front += 1
data = Queue[front]
Queue[front] = None
print('deQueue -->', data)

print("----- Queue State -----")
print("front = ", front," | rear = ", rear)
print('[Exit] <--', end = ' ')

for i in range(0, len(Queue), 1):
	print(Queue[i], end = ' ')
print('<-- [Start]')
print("----- ----- ----- -----")
