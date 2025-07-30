# Lisa's Python Project: Adventure Game
# Background: Introductory game for kids to learn math, technology, and basic reasoning skills.

import random
import sys
import json

"""Import (bring into your program) three Python standard libraries so you can use their built-in functions:

random

Provides functions to generate random numbers or randomly choose items.

In your game, it’s used to pick random quiz questions and hazards to keep the gameplay unpredictable.

sys

Gives access to system-specific parameters and functions.

In your code, it’s mainly used for sys.exit(), which cleanly ends the game program when needed (like quitting or game over).

json

Lets you work with JSON data (JavaScript Object Notation), a common format to store and exchange data.

Your game uses it to save and load the game state from a file (savegame.json), so players can continue where they left off.

So basically, these imports give your code handy tools to run the game smoothly, handle randomness, quit properly, and save/load data."""

# -----------------------------
# Global Variables
# -----------------------------

# Rooms with descriptions, exits, and items available in each room
rooms = {
    "Clearing": {
        "description": "A small clearing in the spooky forest. You feel a cold breeze, and eerie whispers echo among the trees.",
        "exits": {"north": "Dark Cave", "south": "Old Cabin", "east": "Misty Pond", "west": "Hidden Grove"},
        "items": []
    },
    "Dark Cave": {
        "description": "A damp, pitch-black cave. You hear dripping water and the scurry of unseen creatures.",
        "exits": {},
        "items": ["flashlight", "broken stick"]
    },
    "Old Cabin": {
        "description": "An abandoned cabin with creaky floorboards and dusty furniture.",
        "exits": {},
        "items": ["map", "old shoe"]
    },
    "Misty Pond": {
        "description": "A foggy pond reflecting moonlight. The water ripples even though there is no wind.",
        "exits": {},
        "items": ["compass", "strange feather"]
    },
    "Hidden Grove": {
        "description": "A hidden grove glowing faintly in the dark. The air feels charged with energy.",
        "exits": {},
        "items": ["fire kit", "rusty can"]
    }
}

# Starting variables
current_room = "Clearing"   # Player's current location
inventory = []              # Items player has collected
life_points = 0             # Player's life points
max_life_points = 12        # Maximum possible life points
mission_items = {"flashlight", "map", "compass", "fire kit"}  # Correct items to find

# Completed rooms variables
completed_rooms = set()  # Tracks rooms player has fully completed

player_name = "You"  # Default name if none entered

# -----------------------------
# Quiz Data (by categories)
# -----------------------------

# List of quizzes with category, question, multiple choices, and correct answer
quizzes = [
    {"category": "Math", "question": "What is 15% of $200?", "choices": ["$20", "$30", "$25"], "answer": "$30"},
    {"category": "Math", "question": "What is half of 18?", "choices": ["7", "8", "9"], "answer": "9"},
    {"category": "Budgeting", "question": "You buy software for $120 and get a $20 discount. What do you pay?", "choices": ["$100", "$110", "$120"], "answer": "$100"},
    {"category": "Budgeting", "question": "If you save $15 per week, how much after 4 weeks?", "choices": ["$45", "$60", "$75"], "answer": "$60"},
    {"category": "Project Management", "question": "A project has 10 tasks, 7 done. What percent complete?", "choices": ["70%", "50%", "80%"], "answer": "70%"},
    {"category": "Project Management", "question": "You're managing a small project task that will take 5 hours total. You plan to work 2 hours per day on it. How many days will it take you to finish?", "choices": ["2.5", "3", "5"], "answer": "3"},
    {"category": "Tech", "question": "What does CPU stand for?", "choices": ["Central Processing Unit", "Computer Power Unit", "Central Power Utility"], "answer": "Central Processing Unit"},
    {"category": "Tech", "question": "Which is a strong password?", "choices": ["password123", "Qx!7&zLw", "john2022"], "answer": "Qx!7&zLw"},
    {"category": "Cybersecurity", "question": "What is phishing?", "choices": ["Fishing online", "A scam to steal data", "A virus"], "answer": "A scam to steal data"},
    {"category": "Cybersecurity", "question": "Safest for two-factor authentication?", "choices": ["SMS", "Authenticator app", "Email"], "answer": "Authenticator app"},
]

# -----------------------------
# Hazards
# -----------------------------

# List of hazards the player must respond to, with choices and correct answers
hazards = [
    {"scenario": "Dragon blocks path! What do you do?", "choices": ["Dive into river", "Throw rocks"], "answer": "Dive into river"},
    {"scenario": "Swarm of bees! What do you do?", "choices": ["Cover in mud", "Wave arms"], "answer": "Cover in mud"},
    {"scenario": "Landslide starts! What do you do?", "choices": ["Climb up", "Stay put"], "answer": "Climb up"},
    {"scenario": "Deep fog surrounds you. What do you do?", "choices": ["Stay still", "Run blindly"], "answer": "Stay still"},
]

# Score tracker by category
score_breakdown = {
    "Math": 0,
    "Budgeting": 0,
    "Project Management": 0,
    "Tech": 0,
    "Cybersecurity": 0,
    "Items": 0,
    "Hazards": 0
}

# -----------------------------
# Functions
# -----------------------------

def intro():
    """
    Displays the game introduction and prompts the player to start or quit.
    Exits the game if the player does not want to proceed.
    """
    global player_name
    player_name = input("Enter your name, brave adventurer: ").strip()
    if not player_name:
        player_name = "You"  # fallback if empty

    print("\n🧚‍♀️ Fairy: Welcome, brave child! You must collect 4 key items to survive and escape.")
    print("The right items give +1 life point, the wrong ones lose -1 point.")
    print("Your skills in math, tech, budgeting, project management, and cybersecurity will be tested.")
    choice = input("Do you wish to proceed? (yes/no): ").strip().lower()
    if choice != "yes":
        print("👋 You choose not to proceed. Game over.")
        sys.exit()
    else:
        print("✨ Be brave and choose your path!")

def ask_quiz():
    """
    Presents a random quiz question to the player.
    Increases or decreases life points based on correctness.
    Ends the game if life points drop below zero.
    """
    global life_points
    if not quizzes:
        print("🎓 No more quizzes left!")
        return
    quiz = random.choice(quizzes)
    quizzes.remove(quiz)  # Remove to avoid repeats

    print(f"\n🧚‍♀️ Quiz ({quiz['category']}): {quiz['question']}")
    for i, choice in enumerate(quiz["choices"], 1):
        print(f"{i}. {choice}")

    while True:
        answer = input("Choose the number: ").strip()
        # Validate input is a valid option number
        if not answer.isdigit() or int(answer) < 1 or int(answer) > len(quiz["choices"]):
            print("❌ That is not an option, try again.")
            continue
        selected = quiz["choices"][int(answer) - 1]
        if selected == quiz["answer"]:
            life_points += 1
            score_breakdown[quiz["category"]] += 1
            print("✅ Correct! +1 life point.")
        else:
            life_points -= 1
            print("❌ Wrong! -1 life point.")
        break

    if life_points < 0:
        game_over()

def handle_hazard():
    """
    Presents a random hazard scenario to the player.
    Adjusts life points based on player's choice.
    Ends the game if life points drop below zero.
    """
    global life_points
    if not hazards:
        print("✨ No hazards left.")
        return
    hazard = random.choice(hazards)
    hazards.remove(hazard)  # Remove to avoid repeats

    print(f"\n⚠️ Hazard: {hazard['scenario']}")
    for i, choice in enumerate(hazard["choices"], 1):
        print(f"{i}. {choice}")

    while True:
        answer = input("Choose the number: ").strip()
        # Validate input is a valid option number
        if not answer.isdigit() or int(answer) < 1 or int(answer) > len(hazard["choices"]):
            print("❌ That is not an option, try again.")
            continue
        selected = hazard["choices"][int(answer) - 1]
        if selected == hazard["answer"]:
            life_points += 1
            score_breakdown["Hazards"] += 1
            print("✅ Safe choice! +1 life point.")
        else:
            life_points -= 1
            print("❌ Bad choice! -1 life point.")
        break

    if life_points < 0:
        game_over()

def take_item(item):
    """
    Attempts to take an item from the current room.
    Updates inventory and life points based on whether the item is a mission item.
    Ends game if life points drop below zero.
    Returns True if item was valid (regardless of success), else False.
    """
    global life_points
    lowered_items = [i.lower() for i in rooms[current_room]["items"]]

    if item.lower() not in lowered_items:
        print("❌ That is not an option, try again.")
        return False

    real_item = rooms[current_room]["items"][lowered_items.index(item.lower())]

    if real_item.lower() in mission_items:
        inventory.append(real_item)
        rooms[current_room]["items"].remove(real_item)
        life_points += 1
        score_breakdown["Items"] += 1
        print(f"✅ You took the {real_item}! +1 life point.")
    else:
        life_points -= 1
        print(f"❌ The {real_item} is cursed! -1 life point. Try again.")

    if life_points < 0:
        game_over()

    return True

def check_end():
    """
    Checks if player has collected all mission items.
    If yes, ends the game with a victory message and shows summary and leaderboard.
    """
    collected = set(i.lower() for i in inventory)
    if mission_items.issubset(collected):
        print("\n🎉 You collected all correct items and escape the forest!")
        print(f"❤️ Final life points: {life_points}/{max_life_points}")
        show_summary()
        show_leaderboard()
        save_results_to_file()
        sys.exit()

def game_over():
    """
    Ends the game with a failure message when life points drop below zero.
    Shows final score summary, leaderboard, and saves results to file.
    """
    print("\n💀 Your life points fell below zero. The wizard captures you forever!")
    print(f"❤️ Final life points: {life_points}/{max_life_points}")
    show_summary()
    show_leaderboard()
    save_results_to_file()
    sys.exit()

def show_summary():
    """
    Displays a textual bar chart summary of the player's score breakdown by category.
    """
    print("\n📊 Score Breakdown 📊")
    for category, score in score_breakdown.items():
        bar = "█" * score
        print(f"{category:18}: {bar} ({score})")

def show_leaderboard():
    """
    Displays a simple leaderboard with preset player data including the current player.
    """
    print("\n🏅 Leaderboard 🏅")
    fake_data = [
        {"name": "Aria", "points": 10},
        {"name": "Zane", "points": 8},
        {"name": "Liam", "points": 7},
        {"name": player_name, "points": life_points},
        {"name": "Maya", "points": 3}
    ]
    sorted_data = sorted(fake_data, key=lambda x: x["points"], reverse=True)
    medals = ["🥇", "🥈", "🥉"]

    for idx, entry in enumerate(sorted_data, 1):
        medal = medals[idx-1] if idx <= 3 else "🎖️"
        print(f"{idx}. {medal} {entry['name']} - {entry['points']} points")

def save_results_to_file():
    """
    Saves the game results, including final life points, score breakdown, and leaderboard, to a text file.
    Handles exceptions and notifies the player if saving fails.
    """
    try:
        with open("game_results.txt", "w") as f:
            f.write("🎉 Game Results 🎉\n")
            f.write(f"Final life points: {life_points}\n\n")
            f.write("📊 Score Breakdown 📊\n")
            for category, score in score_breakdown.items():
                bar = "█" * score
                f.write(f"{category:18}: {bar} ({score})\n")
            f.write("\n🏅 Leaderboard 🏅\n")
            fake_data = [
                {"name": "Aria", "points": 10},
                {"name": "Zane", "points": 8},
                {"name": "Liam", "points": 7},
                {"name": player_name, "points": life_points},
                {"name": "Maya", "points": 3}
            ]
            sorted_data = sorted(fake_data, key=lambda x: x["points"], reverse=True)
            medals = ["🥇", "🥈", "🥉"]

            for idx, entry in enumerate(sorted_data, 1):
                medal = medals[idx-1] if idx <= 3 else "🎖️"
                f.write(f"{idx}. {medal} {entry['name']} - {entry['points']} points\n")
        print("💾 Game results saved to game_results.txt")
    except Exception as e:
        print(f"❌ Failed to save game results: {e}")

def save_game():
    """
    Saves the current game state (room, inventory, life points, quizzes, hazards, score) to a JSON file.
    """
    save_data = {
        "current_room": current_room,
        "inventory": inventory,
        "life_points": life_points,
        "quizzes": quizzes,
        "hazards": hazards,
        "score_breakdown": score_breakdown
    }
    try:
        with open("savegame.json", "w") as f:
            json.dump(save_data, f)
        print("💾 Game saved successfully!")
    except Exception as e:
        print(f"❌ Error saving game: {e}")

def load_game():
    """
    Loads game state from a JSON file and updates global variables accordingly.
    Handles errors if file not found or corrupt.
    """
    global current_room, inventory, life_points, quizzes, hazards, score_breakdown
    try:
        with open("savegame.json", "r") as f:
            save_data = json.load(f)
        current_room = save_data["current_room"]
        inventory.clear()
        inventory.extend(save_data["inventory"])
        life_points = save_data["life_points"]
        quizzes.clear()
        quizzes.extend(save_data["quizzes"])
        hazards.clear()
        hazards.extend(save_data["hazards"])
        score_breakdown.clear()
        score_breakdown.update(save_data["score_breakdown"])
        print("📂 Game loaded successfully!")
    except FileNotFoundError:
        print("❌ No saved game found.")
    except Exception as e:
        print(f"❌ Error loading game: {e}")

# -----------------------------
# Main Game Loop
# -----------------------------

def main():
    """
    Runs the main game loop, handling player input for movement, inventory, points, saving/loading, and quitting.
    Coordinates quizzes, item collection, hazards, and room transitions.
    """
    global current_room

    intro()

    while True:
        # Show current location and player stats
        print(f"\nYou are in the {current_room}.")
        print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'} | ❤️ Life points: {life_points}/{max_life_points}")
        print("Game Options: north, south, east, west, inventory, points, save, load, quit")

        command = input("> ").strip().lower()

        # Player chooses to quit the game
        if command == "quit":
            print("👋 You chose to rest forever...")
            show_summary()
            show_leaderboard()
            save_results_to_file()
            break

        # Display player's inventory
        elif command == "inventory":
            print(f"🎒 Inventory: {', '.join(inventory) if inventory else 'Empty'}")

        # Display player's life points
        elif command == "points":
            print(f"❤️ Life points: {life_points}")

        # Save the game state
        elif command == "save":
            save_game()

        # Load a saved game state
        elif command == "load":
            load_game()

        # Move in a direction
        elif command in ["north", "south", "east", "west"]:
            # Map commands to rooms
            if command == "north":
                target = "Dark Cave"
            elif command == "south":
                target = "Old Cabin"
            elif command == "east":
                target = "Misty Pond"
            elif command == "west":
                target = "Hidden Grove"

            # Check if this room is already completed
            if target in completed_rooms:
                print("⚠️ You've already successfully completed this location. Choose another location.")
                continue  # Skip rest, ask for input again

            current_room = target
            print(f"🌲 You are now in the {current_room}.")

            # Ask a quiz question before moving
            ask_quiz()

            # Check if player lost all life points
            if life_points < 0:
                game_over()

            # Allow player to pick up items or leave room
            while True:
                if not rooms[current_room]["items"]:
                    print("No more items here. Go elsewhere.")
                    break

                items = rooms[current_room]["items"]
                if not items:
                    print("No more items here. Go elsewhere.")
                    break

                print("Items in this room:")
                for i, item in enumerate(items, 1):
                    print(f"{i}. {item}")
                print("Choose an item number or type 'leave' to exit.")

                choice = input("> ").strip().lower()

                if choice == "leave":
                    handle_hazard()
                    print("✨ You return to the clearing.")
                    current_room = "Clearing"
                    break
                elif choice.isdigit() and 1 <= int(choice) <= len(items):
                    selected_item = items[int(choice) - 1]
                    if take_item(selected_item):
                        handle_hazard()
                        check_end() 
                        completed_rooms.add(current_room)
                        print("✨ You return to the clearing.")
                        current_room = "Clearing"
                        break
                else:
                    print("❌ That is not an option, try again.")

        else:
            print("❓ Invalid command.")

# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    main()
