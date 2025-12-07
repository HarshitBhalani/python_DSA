stack = []

stack.append(1)
stack.append(2) 
stack.append(3)
print(f"stack after push {stack}") # The stack  [1,2,3]

topElement= stack[-1]
print(f"top element is {topElement}") #return top(last) element of the stack

popElement= stack.pop()
print(f"element popped from stack is {popElement}") #popped the last element 3
print(f"stack after pop operation {stack}") # The stack after pop [1,2]

isEmpty = not bool(stack)
print(isEmpty) # False because stack is not empty

print(len(stack))

print("*** Implementation of Stack using class ***")

# stack in linked list implementation
# Node for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack Class
class Stack:
    def __init__(self):
        self.top = None  # Initially stack is empty

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    # Pop operation
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty! Nothing to pop.")
            return None
        
        popped_value = self.top.data
        self.top = self.top.next
        print(f"Popped: {popped_value}")
        return popped_value

    # Peek operation
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty!")
            return None
        return self.top.data

    # Check empty
    def isEmpty(self):
        return self.top is None

    # Display Stack
    def display(self):
        current = self.top
        print("Stack:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Testing the Stack
stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

stack.display()

print("Top element:", stack.peek())
stack.pop()
stack.display()
print("Is Empty?", stack.isEmpty())

print(" *** Stacks using Linked List implemented successfully! ***")
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverseAndPrint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())