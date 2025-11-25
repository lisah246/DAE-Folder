# 📚 SIMPLE STACK - Like a Stack of Books!
# Rule: Last book you put on top is the first one you take off

# Step 1: Create an empty stack (just an empty list)
stack = []
print("📚 Started with empty stack:", stack)

# Step 2: PUSH function - Add items to the stack
def push(item):
    """Put an item on TOP of the stack"""
    stack.append(item)  # append puts item at the END (which is the TOP)
    print(f"✅ Added '{item}' to the stack")
    print(f"📚 Stack now: {stack}")
    print(f"🔝 Last item added (TOP): {stack[-1]}")  # [-1] gets the LAST item
    print()

# Step 3: POP function - Remove items from the stack  
def pop():
    """Take the TOP item off the stack"""
    if len(stack) == 0:
        print("❌ Stack is empty! Nothing to remove")
        return None
    else:
        # The last item added is the first one we remove (LIFO!)
        removed_item = stack.pop()  # pop() removes the LAST item
        print(f"✅ Removed '{removed_item}' from the stack")
        print(f"📚 Stack now: {stack}")
        if len(stack) > 0:
            print(f"🔝 New top item: {stack[-1]}")  # Show what's on top now
        else:
            print("🔝 Stack is now empty!")
        print()
        return removed_item

# Step 4: PEEK function - Look at the top without removing
def peek():
    """Look at the TOP item without taking it off"""
    if len(stack) == 0:
        print("❌ Stack is empty! Nothing to peek at")
        return None
    else:
        # The LAST item in the list is the TOP of the stack
        top_item = stack[-1]  # [-1] always gets the LAST item
        print(f"👀 Top item is: '{top_item}'")
        print(f"📚 Full stack: {stack}")
        print()
        return top_item

# 🎯 LET'S TEST IT! Watch how "Last In, First Out" works:

print("=" * 60)
print("🎯 TESTING OUR STACK - Last In, First Out!")
print("=" * 60)

print("🔢 Let's add some books one by one:")
push("Book 1")     # First book goes in
push("Book 2")     # Second book goes on top of Book 1  
push("Book 3")     # Third book goes on top of everything

print("👀 Let's peek at what's on top:")
peek()  # Should show "Book 3" because it was the LAST one we added

print("🗑️ Now let's remove books one by one:")
pop()   # Should remove "Book 3" (last one added)
pop()   # Should remove "Book 2" (second to last added)
pop()   # Should remove "Book 1" (first one added, last one removed)

print("🗑️ Try to remove from empty stack:")
pop()   # Should show error message

print("=" * 60)
print("✨ SIMPLE EXPLANATION:")
print("• stack = [] is just a list")
print("• push() uses append() to add to the END")
print("• pop() removes from the END") 
print("• peek() looks at the END with [-1]")
print("• The END of the list = the TOP of the stack")
print("• Last thing you put in = First thing that comes out")
print("=" * 60)