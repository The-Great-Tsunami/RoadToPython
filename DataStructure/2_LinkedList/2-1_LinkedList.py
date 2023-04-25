#create Class_Node
class Node():                          # Node라는 데이터형을 만드는 것
	def __init__(self):               # 데이터형을 생성할 때 자동으로 실행되는 부분
		self.data = None              # 데이터와 링크가 저장되는 부분
		self.link = None


#create Node1
node1 = Node()
node1.data = 'Pikachu'

#create Node2
node2 = Node()
node2.data = 'Pairi'
node1.link = node2 #Connect the second node to the link of the first node

node3 = Node()
node3.data = 'Ggobogi'
node2.link = node3 #Connect the second node to the link of the first node

node4 = Node()
node4.data = 'Lizamong'
node3.link = node4 #Connect the second node to the link of the first node

node5 = Node()
node5.data = 'Yadoran'
node4.link = node5 #Connect the second node to the link of the first node

currents = node1

print(currents.data, end = ' ')

while currents.link != None:
	currents = currents.link
	print(currents.data, end = ' ')
print()


# inserts Node -> at index2

new_node = Node() #새 노드를 생성
new_node.data = "New_Data" #새 노드의 링크에 정연 노드의 링크를 복사
new_node.link = node2.link
node2.link = new_node


print('---------------')
currents = node1
print(currents.data, end = ' ')

while currents.link != None:
	currents = currents.link
	print(currents.data, end = ' ')
print()


node2.link = new_node.link  #node2의 링크에 새 노드의 링크를 복사
del(new_node)               #새 노드를 삭제

print('---------------')
currents = node1
print(currents.data, end = ' ')

while currents.link != None:
	currents = currents.link
	print(currents.data, end = ' ')