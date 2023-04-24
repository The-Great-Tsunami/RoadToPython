#create Class_Node
class Node():
	def __init__(self):
		self.data = None
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

print(node1.data, end = ' - ')
print(node1.link.data, end = ' - ')
print(node1.link.link.data, end = ' - ')
print(node1.link.link.link.data, end = ' - ')
print(node1.link.link.link.link.data)