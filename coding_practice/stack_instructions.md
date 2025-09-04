# What is a “stack”?

A stack in programming is just a way to organize data using the rule called “Last In, First Out” (LIFO) — the last thing you put on is the first thing you take off like a stack of plates.

To implement a stack is to create a working data structure that adheres to the Last-In, First-Out (LIFO) principle. 

# Why do we care?

Programs often need a temporary place to keep track of things:

Example: A web browser uses a stack for the Back button (the last page you visited is the first you go back to).

# What do the terms mean?

push(value)
👉 Means “put something on top of the stack.”
Example: Add a pancake.

pop()
👉 Means “take the top thing off and give it back.”
If stack is empty, return None.
Example: Take the top pancake off the stack.

peek()
👉 Means “look at the top thing without taking it.”
Example: You peek to see if the top pancake is blueberry, but you don’t eat it yet.

is_empty()
👉 Checks if there are no items.
Example: Is the pancake stack empty? True/False.

size()
👉 Counts how many items are in the stack.
Example: “We have 3 pancakes in the stack.”

# The big picture

Your instructor gave you this exercise because:

It’s a classic beginner data structure.

It makes you practice using Python lists (append, pop, len, etc.).

It teaches you how to build tools (functions) that match real-world ideas (like Back button, undo, etc.).


# What does “implement” mean?

Fill in the TODOs with real Python code so the functions actually work.

The tiny bits of Python you need

Add to the end: stack.append(value)

Remove from the end and return it: stack.pop()

Look at the last item without removing: stack[-1]

Length of list: len(stack)

Check if empty: len(stack) == 0 (or simply if stack:/if not stack:)

TEST Commands

push('A')
print(stack)          # should show ['A']

push('B')
print(stack)          # should show ['A', 'B']

print(peek())         # should print 'B'

print(size())         # should print 2

print(pop())          # should print 'B'
print(stack)          # now ['A']

print(pop())          # should print 'A'
print(stack)          # now []

print(pop())          # should print None (empty)

print(is_empty())     # should print True
