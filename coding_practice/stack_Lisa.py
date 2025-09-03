# stack.py
# -----------------------------------------------------------------------------
# Your task: implement a simple Stack using a Python list.
#
# Functions to implement:
#   1. push(value)    -> put value on top of the stack
#   2. pop()          -> remove and return the top value, or None if empty
#   3. peek()         -> return the top value without removing it, or None if empty
#   4. is_empty()     -> return True if the stack has no items
#   5. size()         -> return how many items are in the stack
# -----------------------------------------------------------------------------

# The stack should be stored in a list called "stack"
stack = []

def push(value):
    # TODO: add value to the top of the stack
    # Write your code here
    stack.append(value)

     
def pop():
    # TODO: remove and return the top value, or None if empty
    # Write your code here
    if len(stack) == 0:
        return None
    return stack.pop()
     
def peek():
    # TODO: return the top value without removing it, or None if empty
    # Write your code here
    if len(stack) == 0:
        return None
    return stack[-1]
     
def is_empty():
    # TODO: return True if stack is empty, else False
    # Write your code here
    return len(stack) == 0
     
def size():
    # TODO: return how many items are in the stack
    # Write your code here
    return len(stack)

def check(test_name, got, expected):
    if got == expected:
        print(f"[PASS] {test_name}: got {got}")
    else:
        print(f"[FAIL] {test_name}: got {got}, expected {expected}")

# Start fresh
stack.clear()

# Quick simple tests for our stack functions

# Push 'A' and 'B' onto the stack
push("A")   # stack = ['A']
push("B")   # stack = ['A', 'B']
print("Stack now:", stack)          # should print ['A', 'B']

# Peek at the top of the stack without removing it
print("Peek:", peek())              # should print 'B'

# Check how many items are currently in the stack
print("Size:", size())              # should print 2

# Pop items off the stack (remove + return the top item)
print("Pop:", pop())                # should print 'B', stack = ['A']
print("Pop:", pop())                # should print 'A', stack = []
print("Pop empty:", pop())          # should print None (stack is empty)

# Check if the stack is empty now
print("Is empty?", is_empty())      # should print True
