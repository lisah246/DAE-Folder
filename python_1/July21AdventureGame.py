import random
import sys

# -----------------------------
# Global Variables
# -----------------------------

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

current_room = "Clearing"
inventory = []
life_points = 0
mission_items = {"flashlight", "map", "compass", "fire kit"}

# -----------------------------
# Quiz Data (by categories)
# -----------------------------

quizzes = [
    # Math
    {"category": "Math", "question": "What is 15% of $200?", "choices": ["$20", "$30", "$25"], "answer": "$30"},
    {"category": "Math", "question": "What is half of 18?", "choices": ["7", "8", "9"], "answer": "9"},
    # Budgeting
    {"category": "Budgeting", "question": "You buy software for $120 and get a $20 discount. What do you pay?", "choices": ["$100", "$110", "$120"], "answer": "$100"},
    {"category": "Budgeting", "question": "If you save $15 per week, how much after 4 weeks?", "choices": ["$45", "$60", "$75"], "answer": "$60"},
    # Project Management
    {"category": "Project Management", "question": "A project has 10 tasks, 7 done. What percent complete?", "choices": ["70%", "50%", "80%"], "answer": "70%"},
    {"category": "Project Management", "question": "Estimate: 5 hours, working 2/day. How many days?", "choices": ["2.5", "3", "5"], "answer": "3"},
    # Tech
    {"category": "Tech", "question": "What does CPU stand for?", "choices": ["Central Processing Unit", "Computer Power Unit", "Central Power Utility"], "answer": "Central Processing Unit"},
    {"category": "Tech", "question": "Which is a strong password?", "choices": ["password123", "Qx!7&zLw", "john2022"], "answer": "Qx!7&zLw"},
    # Cybersecurity
    {"category": "Cybersecurity", "question": "What is phishing?", "choices": ["Fishing online", "A scam to steal data", "A virus"], "answer": "A scam to steal data"},
    {"category": "Cybersecurity", "question": "Safest for two-factor authentication?", "choices": ["SMS", "Authenticator app", "Email"], "answer": "Authenticator app"},
]

# -----------------------------
# Hazards
# -----------------------------

hazards = [
    {"scenario": "Dragon blocks path! What do you do?", "choices": ["Dive into river", "Throw rocks"], "answer": "Dive into river"},
    {"scenario": "Swarm of bees! What do you do?", "choices": ["Cover in mud", "Wave arms"], "answer": "Cover in mud"},
    {"scenario": "Landslide starts! What do you do?", "choices": ["Climb up", "Stay put"], "answer": "Climb up"},
    {"scenario": "Deep fog surrounds you. What do you do?", "choices": ["Stay still", "Run blindly"], "answer": "Stay still"},
]

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
    print("\n🧚‍♀️ Fairy: Welcome, brave child! You must collect four items to survive and escape.")
    print("The right items give +1 life point, the wrong ones lose -1 point.")
    print("Your skills in math, tech, budgeting, project management, and cybersecurity will be tested.")
    choice = input("Do you wish to proceed? (yes/no): ").strip().lower()
    if choice != "yes":
        print("👋 You choose not to proceed. Game over.")
        sys.exit()
    else:
        print("✨ Be brave and choose your path!")

def ask_quiz():
    global life_points
    if not quizzes:
        print("🎓 No more quizzes left!")
        return
    quiz = random.choice(quizzes)
    quizzes.remove(quiz)
    print(f"\n🧚‍♀️ Quiz ({quiz['category']}): {quiz['question']}")
    for i, choice in enumerate(quiz["choices"], 1):
        print(f"{i}. {choice}")
    answer = input("Choose the number: ").strip()
    try:
        selected = quiz["choices"][int(answer)-1]
        if selected == quiz["answer"]:
            life_points += 1
            score_breakdown[quiz["category"]] += 1
            print("✅ Correct! +1 life point.")
        else:
            life_points -= 1
            print("❌ Wrong! -1 life point.")
    except:
        life_points -= 1
        print("❌ Invalid! -1 life point.")
    if life_points < 0:
        game_over()

def handle_hazard():
    global life_points
    if not hazards:
        print("✨ No hazards left.")
        return
    hazard = random.choice(hazards)
    hazards.remove(hazard)
    print(f"\n⚠️ Hazard: {hazard['scenario']}")
    for i, choice in enumerate(hazard["choices"], 1):
        print(f"{i}. {choice}")
    answer = input("Choose the number: ").strip()
    try:
        selected = hazard["choices"][int(answer)-1]
        if selected == hazard["answer"]:
            life_points += 1
            score_breakdown["Hazards"] += 1
            print("✅ Safe choice! +1 life point.")
        else:
            life_points -= 1
            print("❌ Bad choice! -1 life point.")
    except:
        life_points -= 1
        print("❌ Invalid! -1 life point.")
    if life_points < 0:
        game_over()

def take_item(item):
    global life_points
    if item.lower() in [i.lower() for i in rooms[current_room]["items"]]:
        real_item = next(i for i in rooms[current_room]["items"] if i.lower() == item.lower())
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
        check_end()
    else:
        print("❌ That item isn't here.")

def check_end():
    collected = set(i.lower() for i in inventory)
    if mission_items.issubset(collected):
        print("\n🎉 You collected all correct items and escape the forest!")
        print(f"❤️ Final life points: {life_points}")
        show_summary()
        show_leaderboard()
        sys.exit()

def game_over():
    print("\n💀 Your life points fell below zero. The wizard captures you forever!")
    print(f"❤️ Final life points: {life_points}")
    show_summary()
    show_leaderboard()
    sys.exit()

def show_summary():
    print("\n📊 Score Breakdown 📊")
    for category, score in score_breakdown.items():
        bar = "█" * score
        print(f"{category:18}: {bar} ({score})")

def show_leaderboard():
    print("\n🏅 Leaderboard 🏅")
    fake_data = [
        {"name": "Aria", "points": 10},
        {"name": "Zane", "points": 8},
        {"name": "Liam", "points": 7},
        {"name": "You", "points": life_points},
        {"name": "Maya", "points": 3}
    ]
    sorted_data = sorted(fake_data, key=lambda x: x["points"], reverse=True)
    medals = ["🥇", "🥈", "🥉"]
    for idx, entry in enumerate(sorted_data, 1):
        medal = medals[idx-1] if idx <= 3 else "🎖️"
        print(f"{idx}. {medal} {entry['name']} - {entry['points']} points")

# -----------------------------
# Main Game Loop
# -----------------------------

def main():
    global current_room

    intro()

    while True:
        print(f"\nYou are in the {current_room}.")
        print(f"Inventory: {', '.join(inventory) if inventory else 'Empty'} | ❤️ Life points: {life_points}")
        print("Options: north, south, east, west, inventory, points, quit")
        command = input("> ").strip().lower()

        if command == "quit":
            print("👋 You chose to rest forever...")
            show_summary()
            show_leaderboard()
            break
        elif command == "inventory":
            print(f"🎒 Inventory: {', '.join(inventory) if inventory else 'Empty'}")
        elif command == "points":
            print(f"❤️ Life points: {life_points}")
        elif command in ["north", "south", "east", "west"]:
            if command == "north":
                target = "Dark Cave"
            elif command == "south":
                target = "Old Cabin"
            elif command == "east":
                target = "Misty Pond"
            elif command == "west":
                target = "Hidden Grove"

            ask_quiz()

            if life_points < 0:
                game_over()

            current_room = target

            while True:
                if not rooms[current_room]["items"]:
                    print("No more items here. Go elsewhere.")
                    break
                print(f"Items in this room: {', '.join(rooms[current_room]['items'])}")
                print("Pick an item or type 'leave' to exit.")
                choice = input("> ").strip().lower()
                if choice == "leave":
                    handle_hazard()
                    print("✨ You return to the clearing.")
                    current_room = "Clearing"
                    break
                else:
                    take_item(choice)
                    if life_points < 0:
                        game_over()
                    if choice in [i.lower() for i in inventory]:
                        handle_hazard()
                        print("✨ You return to the clearing.")
                        current_room = "Clearing"
                        break
        else:
            print("❓ Invalid command.")

# -----------------------------
# Run
# -----------------------------

if __name__ == "__main__":
    main()
