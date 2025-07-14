# Example basic structure

def show_instructions():
    print("Commands: go [direction], look, take [item], inventory, quit")

def show_status():
    print(f"You are in {current_room}")
    print("Inventory:", inventory)
    print(rooms[current_room]["description"])

def move(direction):
    if direction in rooms[current_room]["exits"]:
        return rooms[current_room]["exits"][direction]
    else:
        print("You can't go that way!")
        return current_room

# Define rooms
rooms = {
    "Forest": {
        "description": "A dark, spooky forest. There is a path to the north.",
        "exits": {"north": "Cave"},
        "items": ["stick"]
    },
    "Cave": {
        "description": "A damp cave. You see light to the south.",
        "exits": {"south": "Forest"}
    }
}

current_room = "Forest"
inventory = []

show_instructions()

while True:
    show_status()
    command = input("> ").strip().lower()

    try:
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command.startswith("go "):
            direction = command[3:]
            current_room = move(direction)
        elif command == "look":
            print(rooms[current_room]["description"])
        elif command.startswith("take "):
            item = command[5:]
            if "items" in rooms[current_room] and item in rooms[current_room]["items"]:
                inventory.append(item)
                rooms[current_room]["items"].remove(item)
                print(f"You picked up the {item}.")
            else:
                print("That item isn't here!")
        elif command == "inventory":
            print("Inventory:", inventory)
        else:
            print("Invalid command.")
    except Exception as e:
        print("Something went wrong:", e)
