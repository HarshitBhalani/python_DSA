#linked list implementation with various operations - insertion, deletion, traversal, search, count

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Traverse Linked List
def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")


# Insert at Beginning
def insertBeginning(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode


# Insert at End
def insertEnd(head, data):
    newNode = Node(data)
    if head is None:
        return newNode
    current = head
    while current.next:
        current = current.next
    current.next = newNode
    return head


# Insert at Any Position (1-based)
def insertAtPosition(head, data, position):
    newNode = Node(data)
    if position == 1:
        newNode.next = head
        return newNode

    current = head
    for _ in range(position - 2):
        if current is None:
            break
        current = current.next

    newNode.next = current.next
    current.next = newNode
    return head


# Delete from Beginning
def deleteBeginning(head):
    if head is None:
        print("List is empty")
        return None
    return head.next


# Delete from End
def deleteEnd(head):
    if head is None:
        print("List is empty")
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


# Delete from Any Position
def deleteAtPosition(head, position):
    if head is None:
        return None
    if position == 1:
        return head.next

    current = head
    for _ in range(position - 2):
        if current.next is None:
            return head
        current = current.next

    if current.next is not None:
        current.next = current.next.next

    return head


# Search Node
def search(head, key):
    current = head
    position = 1
    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1
    return -1

# Count Nodes
def countNodes(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original List:")
traverse(node1)

node1 = insertBeginning(node1, 100)
print("\nAfter inserting 100 at beginning:")
traverse(node1)

node1 = insertEnd(node1, 50)
print("\nAfter inserting 50 at end:")
traverse(node1)

node1 = insertAtPosition(node1, 97, 3)
print("\nAfter inserting 97 at position 3:")
traverse(node1)

node1 = deleteBeginning(node1)
print("\nAfter deleting beginning:")
traverse(node1)

node1 = deleteEnd(node1)
print("\nAfter deleting end:")
traverse(node1)

node1 = deleteAtPosition(node1, 2)
print("\nAfter deleting position 2:")
traverse(node1)

pos = search(node1, 2)
print(f"\nSearch 2 found at position: {pos}")

print("\nTotal nodes:", countNodes(node1))
