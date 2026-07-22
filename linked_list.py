#linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(25)
node4 = Node(50)

# Connecting nodes
node1.next = node2
node2.next = node3
node3.next = node4

# Head of linked list
head = node1

# Traversing linked list
current = head

while current is not None:
    print(current.data, end="->")
    current = current.next

print("None")

#add new node at beginning
new_node= Node(60)
new_node.next = head
head = new_node

#adding new node at last
new_node1 = Node(70)
current = head
while current is not None:
    current = current.next
    current.next = new_node1
