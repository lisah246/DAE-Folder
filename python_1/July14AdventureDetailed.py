import json

# -----------------------------
# Global Variables
# -----------------------------

rooms = {
    "Clearing": {
        "description": "A small clearing in the spooky forest. You feel a cold breeze, and eerie whispers echo among the trees. There is a narrow path to the east.",
        "exits": {"east": "Dark Cave"},
        "items": []
    },
    "Dark Cave": {
        "description": "A damp, pitch-black cave. You hear dripping water and the scurry of unseen creatures. Exits: west and north.",
        "exits": {"west": "Clearing", "north": "Old Cabin"},
        "items": ["flashlight", "broken stick"]
    },
    "Old Cabin": {
        "description": "An abandoned cabin with creaky floorboards and dusty furniture. Spider webs hang from every corner. Exits: south and east.",
        "exits": {"south": "Dark Cave", "east": "Misty Pond"},
        "items": ["map", "old shoe"]
    },
    "Misty Pond": {
        "description": "A foggy pond reflecting moonlight. The water ripples even though there is no wind. Exit: west.",
        "exits": {"west": "Old Cabin", "north": "Hidden Grove"},
        "items": ["compass", "strange feather"]
    },
    "Hidden Grove": {
        "description": "A hidden grove glowing faintly in the dark. The air feels charged with energy. Exit: south.",
        "exits": {"south": "Misty Pond"},
        "items": ["magic stone", "rusty can"]
    }
}

current_room = "Clearing"
inventory = []

mission_items = {"flashlight", "map", "compass", "magic stone"}

# -----------------------------
# Functions
# -----------------------------

def show_instructions():
    print("\n=== 🧒 Escape the Spooky Forest ===")
    print("You are a kid lost in a spooky, haunted forest!")
    print("To escape, you must collect these 4 magical survival items, each hidden:")
    print("  - flashlight")
    print("  - map")
    print("  - compass")
    print("  - magic stone")
    print("But beware! Each room also has a useless or cursed item. Choose wisely!")
    print("If you pick up the wrong set of items, you will be captured and imprisoned by a mysterious forest wizard forever! 🌑")
    print("\nAvailable commands:")
    print("  go [direction]    : Move to another place (e.g., go east)")
    print("  take [item]       : Pick up an item (type its name)")
    print("  look              : Re-describe the current place")
    print("  inventory         : Check your collected items")
    print("  save              : Save your progress")
    print("  load              : Load your saved progress")
    print("  quit              : Quit the game\n")
    print("Be brave and careful... You can do it! 🌲🌙")

def show_status():
    print("\n------------------------")
    print(f"You are in the {current_room}.")
    print(rooms[current_room]["description"])
    if rooms[current_room]["items"]:
        print(f"You see: {', '.join(rooms[current_room]['items'])}")
    print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'}")
    print("------------------------")

def move_player(direction):
    if direction in rooms[current_room]["exits"]:
        return rooms[current_room]["exits"][direction]
    else:
        print("❌ You can't go that way! The trees block your path.")
        return current_room

def take_item(item):
    lower_items = [i.lower() for i in rooms[current_room]["items"]]
    if item.lower() in lower_items:
        actual_item = next(i for i in rooms[current_room]["items"] if i.lower() == item.lower())
        inventory.append(actual_item)
        rooms[current_room]["items"].remove(actual_item)
        print(f"✅ You picked up the {actual_item}.")
        check_end()
    else:
        print("❌ That item isn't here! Check the spelling carefully.")

def check_end():
    if len(inventory) == 4:
        collected = set(i.lower() for i in inventory)
        if mission_items.issubset(collected):
            print("\n🎉 Congratulations! You chose the correct magical items!")
            print("Guided by your compass and map, lit by your flashlight, and protected by the magic stone, you escape the spooky forest safely!")
            print("You run home as the morning light rises. You are free! 🌅")
            print("👋 Thanks for playing!")
            exit()
        else:
            print("\n💀 Oh no! You picked the wrong set of items...")
            print("A mysterious wizard emerges from the shadows and traps you in an endless dream among the forest trees.")
            print("Your screams echo through the dark as you vanish forever...")
            print("👻 Game over. Thanks for playing!")
            exit()

def save_game():
    try:
        game_data = {
            "current_room": current_room,
            "inventory": inventory
        }
        with open("savegame.json", "w") as f:
            json.dump(game_data, f)
        print("💾 Game saved successfully!")
    except Exception as e:
        print("⚠️ Error saving game:", e)

def load_game():
    global current_room, inventory
    try:
        with open("savegame.json", "r") as f:
            game_data = json.load(f)
            current_room = game_data["current_room"]
            inventory = game_data["inventory"]
        print("📂 Game loaded successfully!")
    except FileNotFoundError:
        print("⚠️ Save file not found.")
    except Exception as e:
        print("⚠️ Error loading game:", e)

# -----------------------------
# Main Game Loop
# -----------------------------

def main():
    global current_room
    show_instructions()

    while True:
        show_status()
        command = input("> ").strip().lower()

        try:
            if command == "quit":
                print("👋 You give up and curl up under a tree. The forest slowly swallows you...")
                break
            elif command.startswith("go "):
                direction = command[3:].strip()
                current_room = move_player(direction)
            elif command.startswith("take "):
                item = command[5:].strip()
                take_item(item)
            elif command == "look":
                print(rooms[current_room]["description"])
            elif command == "inventory":
                print(f"🎒 Inventory: {', '.join(inventory) if inventory else 'Empty'}")
            elif command == "save":
                save_game()
            elif command == "load":
                load_game()
            else:
                print("❓ Invalid command. The forest didn't understand you...")
        except Exception as e:
            print("⚠️ Error processing command:", e)

# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    main()
