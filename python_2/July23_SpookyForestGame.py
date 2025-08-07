# Final Version of the Spooky Forest Adventure Game
# Includes: File operations (save/load game, leaderboard), Exception handling

import random
import time
import os

# ------------------- Constants & Game Setup -------------------
rooms = ["Dark Cave", "Misty Pond", "Old Cabin", "Hidden Grove"]
mission_items = {"Dark Cave": "Flashlight", "Misty Pond": "Life Jacket", "Old Cabin": "Map", "Hidden Grove": "Magic Key"}
quiz_bank = {
    "Dark Cave": ("What is the opposite of light?", "dark"),
    "Misty Pond": ("What is H2O more commonly known as?", "water"),
    "Old Cabin": ("What do you use to find direction?", "compass"),
    "Hidden Grove": ("What season comes after summer?", "fall")
}

hazards = {
    "Dark Cave": ("A bat swarm rushes at you! Do you duck or run?", "duck"),
    "Misty Pond": ("You slip into the water! Do you swim or scream?", "swim"),
    "Old Cabin": ("A ghost appears! Do you talk or hide?", "hide"),
    "Hidden Grove": ("A shadow blocks your path. Do you fight or sneak?", "sneak")
}

# ------------------- Save/Load Functions -------------------
def save_game(player):
    with open("save_file.txt", "w") as f:
        f.write(f"{player['name']},{player['life_points']},{'|'.join(player['inventory'])}\n")

def load_game():
    if not os.path.exists("save_file.txt"):
        return None
    with open("save_file.txt", "r") as f:
        line = f.readline().strip().split(',')
        return {"name": line[0], "life_points": int(line[1]), "inventory": line[2].split('|')}

def save_leaderboard(player):
    with open("leaderboard.txt", "a") as f:
        f.write(f"{player['name']} - Score: {player['life_points']} - Inventory: {player['inventory']}\n")

# ------------------- Core Game Functions -------------------
def ask_question(room, player):
    question, correct_answer = quiz_bank[room]
    try:
        answer = input(f"Quiz: {question} ").strip().lower()
        if answer == correct_answer:
            print("Correct! +1 Life Point")
            player['life_points'] += 1
        else:
            print("Incorrect. -1 Life Point")
            player['life_points'] -= 1
    except Exception as e:
        print("Something went wrong. Skipping question without life point change.")


def choose_item(room, player):
    correct_item = mission_items[room]
    items = [correct_item, "Broken Stick", "Old Sock"]
    random.shuffle(items)
    while True:
        print("Choose an item:")
        for i, item in enumerate(items):
            print(f"{i+1}. {item}")
        try:
            choice = int(input("Enter item number: "))
            if choice < 1 or choice > len(items):
                raise ValueError
            selected = items[choice - 1]
            if selected == correct_item:
                print(f"You picked the correct item! +1 Life Point")
                player['life_points'] += 1
                player['inventory'].append(correct_item)
                break
            else:
                print("Wrong item. -1 Life Point")
                player['life_points'] -= 1
                if player['life_points'] < 0:
                    break
        except ValueError:
            print("Invalid input. Try again.")
        except Exception:
            print("Something went wrong. Try again.")


def face_hazard(room, player):
    prompt, correct_response = hazards[room]
    try:
        answer = input(f"Hazard: {prompt} ").strip().lower()
        if answer == correct_response:
            print("Well done! +1 Life Point")
            player['life_points'] += 1
        else:
            print("Not quite. -1 Life Point")
            player['life_points'] -= 1
    except Exception:
        print("Error occurred. Skipping hazard without penalty.")

# ------------------- Game Loop -------------------
def play_game():
    print("Welcome to the Spooky Forest Adventure!")
    try:
        name = input("Enter your name: ")
    except Exception:
        name = "Player"

    player = {"name": name, "life_points": 3, "inventory": []}

    for room in rooms:
        print(f"\nYou enter the {room}...\n")

        ask_question(room, player)
        if player['life_points'] < 0:
            print("Game Over! You were captured by the evil wizard!")
            break

        choose_item(room, player)
        if player['life_points'] < 0:
            print("Game Over! You were captured by the evil wizard!")
            break

        face_hazard(room, player)
        if player['life_points'] < 0:
            print("Game Over! You were captured by the evil wizard!")
            break

        save_game(player)  # Save after each room

    # Final check
    if all(item in player['inventory'] for item in mission_items.values()):
        print(f"\nCongratulations {player['name']}! You escaped the spooky forest!")
    else:
        print(f"\nYou didn’t collect all the needed items. You’re lost forever in the forest!")

    print(f"Final Life Points: {player['life_points']}")
    save_leaderboard(player)

# ------------------- Entry Point -------------------
if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted.")
    finally:
        print("Thanks for playing!")
