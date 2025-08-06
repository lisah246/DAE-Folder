import random
import time

# Game setup
rooms = {
    "Dark Cave": {
        "quiz": {
            "question": "What is 8 x 7?",
            "answer": "56",
            "category": "Math"
        },
        "items": ["flashlight", "broken stick"],
        "correct_item": "flashlight",
        "hazard": {
            "situation": "You face a fire-breathing dragon. What do you do?",
            "choices": {
                "dive into river": True,
                "throw rocks": False
            },
            "category": "Survival"
        },
        "mission_item": "Compass"
    },
    "Misty Pond": {
        "quiz": {
            "question": "Which of these is a strong password? (a) password123 (b) T!m3$Q8zL",
            "answer": "b",
            "category": "Cybersecurity"
        },
        "items": ["life vest", "heavy stone"],
        "correct_item": "life vest",
        "hazard": {
            "situation": "You’re caught in a thick fog. What do you do?",
            "choices": {
                "wait it out": True,
                "run forward blindly": False
            },
            "category": "Survival"
        },
        "mission_item": "Magic Map"
    },
    "Old Cabin": {
        "quiz": {
            "question": "What’s the purpose of version control like Git?",
            "answer": "track code changes",
            "category": "Tech"
        },
        "items": ["matches", "wet blanket"],
        "correct_item": "matches",
        "hazard": {
            "situation": "You hear a ghost approaching. What do you do?",
            "choices": {
                "stay still and silent": True,
                "yell for help": False
            },
            "category": "Survival"
        },
        "mission_item": "Key"
    },
    "Hidden Grove": {
        "quiz": {
            "question": "If you have $500 and spend $123.45, how much do you have left?",
            "answer": "376.55",
            "category": "Budgeting"
        },
        "items": ["rope", "shiny gem"],
        "correct_item": "rope",
        "hazard": {
            "situation": "A giant spider blocks your way. What do you do?",
            "choices": {
                "use rope to swing over": True,
                "try to fight it": False
            },
            "category": "Survival"
        },
        "mission_item": "Exit Token"
    }
}

directions = list(rooms.keys())
visited_rooms = []
mission_items = []
life_points = 3
quiz_scores = {"Math": 0, "Cybersecurity": 0, "Tech": 0, "Budgeting": 0, "Survival": 0}
game_over = False

def safe_input(prompt, valid_options):
    while True:
        try:
            choice = input(prompt).strip().lower()
            if choice not in valid_options:
                raise ValueError("Invalid choice.")
        except ValueError as ve:
            print(f"Error: {ve}")
        else:
            return choice
        finally:
            print()

print("\n🌲 Welcome to the Magical Forest Survival Adventure!")
start = safe_input("Do you want to start the game? (yes/no): ", ["yes", "no"])
if start == "no":
    print("Goodbye!")
    exit()

while life_points >= 0 and len(visited_rooms) < 4:
    print(f"\nYou are in the forest. Rooms to explore: {', '.join([r for r in directions if r not in visited_rooms])}")
    next_room = None
    while next_room not in rooms or next_room in visited_rooms:
        try:
            next_room = input("Enter the name of the room to enter: ").title()
            if next_room not in rooms:
                raise ValueError("That room doesn't exist.")
            if next_room in visited_rooms:
                raise ValueError("You've already been there.")
        except ValueError as ve:
            print(f"Error: {ve}")
            continue
        finally:
            print()
    
    print(f"\n🌟 Entering {next_room}...\n")
    current = rooms[next_room]
    
    # Quiz
    print(f"📘 Quiz: {current['quiz']['question']}")
    try:
        answer = input("Your answer: ").strip().lower()
    except Exception as e:
        print("Something went wrong. -1 point.")
        life_points -= 1
        continue
    else:
        if answer == current['quiz']['answer'].lower():
            print("✅ Correct!")
            life_points += 1
            quiz_scores[current['quiz']['category']] += 1
        else:
            print("❌ Wrong.")
            life_points -= 1
    finally:
        print(f"Current life points: {life_points}")

    if life_points < 0:
        break

    # Item Selection
    print(f"\n🧰 Choose an item from the room: {current['items'][0]} or {current['items'][1]}")
    while True:
        try:
            item_choice = input("Which item do you pick? ").strip().lower()
            if item_choice not in current['items']:
                raise ValueError("That item is not available here.")
        except ValueError as ve:
            print(f"Error: {ve}")
        else:
            if item_choice == current['correct_item']:
                print("🪄 Correct item!")
                life_points += 1
                break
            else:
                print("🪦 Wrong item. Try again.")
                life_points -= 1
                if life_points < 0:
                    break
        finally:
            print(f"Current life points: {life_points}")
    
    if life_points < 0:
        break

    # Hazard
    hazard = current["hazard"]
    print(f"\n⚠️ Hazard: {hazard['situation']}")
    print("Your options:", ', '.join(hazard["choices"].keys()))
    try:
        hazard_choice = input("What do you do? ").strip().lower()
        if hazard_choice not in hazard["choices"]:
            raise ValueError("Not a valid action.")
    except ValueError as ve:
        print(f"Error: {ve}")
        life_points -= 1
    else:
        if hazard["choices"][hazard_choice]:
            print("✅ You survived the hazard!")
            life_points += 1
            quiz_scores["Survival"] += 1
        else:
            print("❌ Wrong move.")
            life_points -= 1
    finally:
        print(f"Current life points: {life_points}\n")

    if life_points < 0:
        break

    visited_rooms.append(next_room)
    mission_items.append(current["mission_item"])
    print(f"🎒 Mission items collected: {', '.join(mission_items)}")

if life_points < 0:
    print("💀 You were captured by the Evil Wizard!")
else:
    print("🎉 You escaped the forest!")

# Game Summary
print("\n📊 Game Summary:")
print(f"Life points: {life_points}")
print(f"Rooms visited: {visited_rooms}")
print(f"Mission items: {mission_items}")
print("\nCategory Scores:")
for cat, score in quiz_scores.items():
    print(f" - {cat}: {score}")

# Leaderboard (fake data)
print("\n🏅 Leaderboard:")
leaderboard = [
    ("Zara", 6),
    ("Leo", 5),
    ("You", life_points),
    ("Mira", 4),
    ("Kai", 3)
]
leaderboard.sort(key=lambda x: x[1], reverse=True)
for name, score in leaderboard:
    print(f"{name}: {score} pts")
