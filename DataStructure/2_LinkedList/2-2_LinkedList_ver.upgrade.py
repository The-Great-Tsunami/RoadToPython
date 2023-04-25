# 전역변수 생성
memory = []
data_array = ["A", "B" ,"C", "D", "E"]

# head - 첫번째 노드
# current - 현재 처리 중인 노드
# pre - 현재 처리 중인 노드의 바로 앞 노드
head, current, pre = None, None, None

#클래스와 함수 선언
class Node():
	def __init__(self):
		self.data = None
		self.link = None

#연결리스트 출력
def print_node(start):

	current = start

	if current == None:
		return
	print(current.data, end = ' ')

	while current.link != None:

		current = current.link
		print(current.data, end=' ')

	print()

#연결리스트 노드 삽입
def insert_node(find_data, insert_data):

	global head, current, pre

	# 첫 번째 노드 삽입
	if head.data == find_data:
		node = Node()
		node.data = insert_data
		node.link = head
		head = node
		return

	# 중간 노드 삽입
	current = head

	while current.link != None:
		pre = current
		current = current.link

		if current.data == find_data:
			node = Node()
			node.data = insert_data
			node.link = current
			pre.link = node
			return

	# 마지막 노드 삽입
	node = Node()
	node.data = insert_data
	current.link = node

#연결리스트 노드 삭제

def delete_node(delete_data):

	global head, current, pre

	# 첫 번째 노드 삭제

	if head.data == delete_data:
		current = head
		head = head.link
		del(current)
		return
	current = head

	# 첫 번째 외 삭제

	while current.data != None:
		pre = current
		current = current.link
		if current.data == delete_data:
			pre.link = current.link
			del(current)
			return

#연결리스트 노드 검색

def find_data(find_data):
	global memory, head, current, pre

	current = head
	if current.data == find_data:
		print(current, '-', current.link)
		return current

	while current.link != None:
		current = current.link
		if current.data == find_data:
			print(pre, "-", current, "-", current.link)
			return current

	print("There is no same data")
	return None


#메인함수

if __name__ == '__main__':

	# 첫번째 노드
	node = Node()
	node.data = data_array[0]
	head = node
	memory.append(node)

	# 두번째 이후 노드
	for data in data_array[1:]:
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	insert_node('A', "INSERT1" )
	print_node(head)

	insert_node('C', "INSERT2")
	print_node(head)

	delete_node("INSERT1")
	print_node(head)

	delete_node("INSERT2")
	print_node(head)

	a = find_data("A")
	print(a)