from collections import deque

stack = deque()
stack.append("https:\\cnn.com")
stack.append("https:\\cnn.com\\india")
stack.append("https:\\cnn.com\\us")
stack.append("https:\\cnn.com\\uk")
stack.append("https:\\cnn.com\\netherlands")
stack.append("https:\\cnn.com\\germany")
print(type(stack))
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
