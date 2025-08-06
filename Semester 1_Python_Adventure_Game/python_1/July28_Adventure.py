# Spooky Forest Adventure Game

# ---------- CONSTANTS ----------
MAX_LIFE_POINTS = 5
SAVE_FILE = "save_file.txt"
LEADERBOARD_FILE = "leaderboard.txt"

# ---------- IMPORTS ----------
import random
import time
from collections import namedtuple

# ---------- VARIABLES ----------
life_points = MAX_LIFE_POINTS
mission_items = []
wrong_items = []  # <-- This is a list to store incorrect item choices
visited_rooms = []  # <-- This is a list to track which rooms have been visited

# ---------- ROOM DATA USING NAMED TUPLES ----------
Room = namedtuple("Room", ["name", "question", "answer", "items"])

room_data = [
    Room("Dark Cave", "What color do you get when you mix red and blue?", "purple", ["magic stone", "stick"]),
    Room("Misty Pond", "What gas do plants breathe in?", "carbon dioxide", ["magic water", "mud"]),
    Room("Old Cabin", "How many legs does a spider have?", "8", ["magic lantern", "old boot"]),
    Room("Hidden Grove", "What planet do we live on?", "earth", ["magic compass", "leaf"])
]

room_dict = {room.name: room for room in room_data}
rooms = [room.name for room in room_data]  # <-- This is a list of room names for selection

# ---------- FUNCTIONS ----------
def intro():
    """
    Displays the introduction to the game.
    Explains the story and the player's mission.
    """
    print("""
    Welcome to the Spooky Forest Adventure!
    You're a kid trapped in a mysterious forest.
    You must find 4 magical items to escape.
    Choose wisely — danger lurks in every corner.
    """)

def save_game():
    """
    Saves the current game state to a text file.
    Stores life points, mission items, and visited rooms.
    """
    with open(SAVE_FILE, "w") as f:
        f.write(f"{life_points}\n")
        f.write(",".join(mission_items) + "\n")
        f.write(",".join(visited_rooms) + "\n")
    print("Game state saved!")

# Updated load_game with exception handling and comments
def load_game():
    """
    Loads the saved game state from a file.
    Restores life points, mission items, and visited rooms.
    If the file is missing or invalid, starts a new game.
    """
    global life_points, mission_items, visited_rooms
    try:
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()

            # Ensure the save file has at least 3 lines
            if len(lines) >= 3:
                life_points = int(lines[0].strip())
                mission_items = lines[1].strip().split(",") if lines[1].strip() else []
                visited_rooms = lines[2].strip().split(",") if lines[2].strip() else []
                print("Game loaded successfully!")
            else:
                raise ValueError("Save file is incomplete. Starting new game.")

    except FileNotFoundError:
        print("No saved game found. Starting new game.")
    except ValueError as ve:
        print(f"Save file error: {ve}")
        print("Starting a new game instead.")
    except Exception as e:
        print(f"Unexpected error loading game: {e}")
        print("Starting a new game instead.")

def update_leaderboard(name):
    """
    Appends the player's name, number of items collected, and remaining life points to the leaderboard file.
    """
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name} - Items: {len(mission_items)} - Life Points: {life_points}\n")

def ask_question(question, correct_answer):
    """
    Asks the player a quiz question.
    Adjusts life points based on whether the answer is correct.
    """
    global life_points
    try:
        answer = input(question + " ").strip().lower()
        if answer == correct_answer:
            print("Correct! You gain a life point.")
            life_points += 1
        else:
            print("Wrong! You lose a life point.")
            life_points -= 1
    except Exception as e:
        print("Oops! Something went wrong. Please try again.")
        print(f"Error: {e}")
    finally:
        print(f"Life Points: {life_points}")

def pick_item(room_items):
    """
    Lets the player choose an item from the room.
    Adds correct items to mission_items and wrong items to wrong_items.
    Adjusts life points for wrong choices.
    """
    global life_points
    try:
        print("Available items:", room_items)
        choice = input("Pick an item: ").strip().lower()
        if choice in room_items:
            if choice.startswith("magic"):
                print("You found a mission item!")
                mission_items.append(choice)
            else:
                print("Oops! Wrong item.")
                wrong_items.append(choice)
                life_points -= 1
        else:
            raise ValueError("Invalid item choice")
    except ValueError as ve:
        print(ve)
        print("Please try again. No points lost.")
    finally:
        print(f"Life Points: {life_points}")

def room_challenge(room_name):
    """
    Executes the challenge for a given room.
    Includes asking a quiz question and selecting an item.
    """
    print(f"\nEntering the {room_name}...")
    visited_rooms.append(room_name)

    room = room_dict[room_name]
    ask_question(room.question, room.answer)
    pick_item(room.items)

def play_game():
    """
    Main game loop.
    Loads or starts the game, handles room selection and checks win/lose conditions.
    Saves progress after each round.
    """
    global life_points
    intro()
    load_game()

    # ---- Main Game Loop ----
    while life_points > 0 and len(mission_items) < 4:
        print("\nAvailable rooms:", [r for r in rooms if r not in visited_rooms])
        try:
            choice = input("Choose a room: ").strip().title()
            if choice in rooms and choice not in visited_rooms:
                room_challenge(choice)
            elif choice in visited_rooms:
                print("You already visited that room!")
            else:
                raise ValueError("Invalid room choice")
        except ValueError as ve:
            print(ve)
            print("Try again. No points lost.")

        if life_points <= 0:
            print("\nYou ran out of life points. The wizard captures you forever!")
            break
        elif len(mission_items) == 4:
            print("\nCongratulations! You collected all magical items and escaped the spooky forest!")
            name = input("Enter your name for the leaderboard: ")
            update_leaderboard(name)
            break

        save_game()  # Save game state at the end of each loop

# ---------- RUN GAME ----------
if __name__ == "__main__":
    play_game()
