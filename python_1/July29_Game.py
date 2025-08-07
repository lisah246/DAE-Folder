# Spooky Forest Adventure Game - GUI Version (Tkinter)

# ---------- CONSTANTS ----------
MAX_LIFE_POINTS = 5  # Maximum life points a player can have
SAVE_FILE = "save_file.txt"  # File to save game progress
LEADERBOARD_FILE = "leaderboard.txt"  # File to store leaderboard entries

# ---------- IMPORTS ----------
import tkinter as tk
from tkinter import messagebox
import random
import os
from collections import namedtuple  # Named tuple for room structure

# ---------- VARIABLES ----------
life_points = MAX_LIFE_POINTS  # Tracks the current life points
mission_items = []  # Correct magical items collected by player
wrong_items = []  # Wrong items collected (subtracts points)
visited_rooms = []  # Tracks rooms already visited

# ---------- ROOM DATA USING NAMED TUPLES ----------
Room = namedtuple("Room", ["name", "question", "answer", "items"])

# Room data
room_data = [
    Room("Dark Cave", "What color do you get when you mix red and blue?", "purple", ["magic stone", "stick"]),
    Room("Misty Pond", "What gas do plants breathe in?", "carbon dioxide", ["magic water", "mud"]),
    Room("Old Cabin", "How many legs does a spider have?", "8", ["magic lantern", "old boot"]),
    Room("Hidden Grove", "What planet do we live on?", "earth", ["magic compass", "leaf"])
]

room_dict = {room.name: room for room in room_data}  # For quick lookup

# ---------- SAVE/LOAD FUNCTIONS ----------
def save_game():
    """
    Save current game state to SAVE_FILE
    """
    with open(SAVE_FILE, "w") as f:
        f.write(f"{life_points}\n")
        f.write(",".join(mission_items) + "\n")
        f.write(",".join(visited_rooms) + "\n")

def load_game():
    """
    Load saved game state from SAVE_FILE
    """
    global life_points, mission_items, visited_rooms
    try:
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()
            life_points = int(lines[0].strip())
            mission_items = lines[1].strip().split(",") if lines[1].strip() else []
            visited_rooms = lines[2].strip().split(",") if lines[2].strip() else []
    except:
        pass  # Skip if loading fails

def update_leaderboard(name):
    """
    Write player's result to leaderboard file
    """
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name} - Items: {len(mission_items)} - Life Points: {life_points}\n")

# ---------- GUI FUNCTIONS ----------
def start_game_window():
    """
    Initialize the main GUI game window
    """
    game_window = tk.Tk()
    game_window.title("Spooky Forest Adventure")

    status_label = tk.Label(game_window, text=f"Life Points: {life_points}", font=("Arial", 12))
    status_label.pack(pady=10)

    instruction_label = tk.Label(game_window, text="Choose a room to explore:", font=("Arial", 14))
    instruction_label.pack(pady=10)

    for room in room_data:
        if room.name not in visited_rooms:
            btn = tk.Button(game_window, text=room.name, command=lambda r=room: enter_room(game_window, r))
            btn.pack(pady=5)

    game_window.mainloop()

def enter_room(game_window, room):
    """
    Handle entering a room: ask quiz, choose item
    """
    global life_points

    visited_rooms.append(room.name)

    # Ask quiz question
    def check_answer():
        global life_points
        player_answer = answer_entry.get().strip().lower()
        if player_answer == room.answer:
            life_points = min(MAX_LIFE_POINTS, life_points + 1)
            messagebox.showinfo("Correct", "You got it right! +1 Life Point")
        else:
            life_points -= 1
            messagebox.showwarning("Incorrect", f"Wrong! The correct answer was '{room.answer}'. -1 Life Point")

        quiz_window.destroy()
        if life_points <= 0:
            end_game("lose")
        else:
            choose_item(room)

    quiz_window = tk.Toplevel(game_window)
    quiz_window.title(room.name)

    tk.Label(quiz_window, text=room.question, font=("Arial", 12)).pack(pady=10)
    answer_entry = tk.Entry(quiz_window)
    answer_entry.pack(pady=5)
    tk.Button(quiz_window, text="Submit", command=check_answer).pack(pady=5)

def choose_item(room):
    """
    Handle item selection after quiz
    """
    global life_points

    def item_choice(picked):
        if "magic" in picked:
            mission_items.append(picked)
            messagebox.showinfo("Item", f"You picked {picked}, it's magical!")
        else:
            wrong_items.append(picked)
            life_points -= 1
            messagebox.showwarning("Item", f"{picked} is useless! -1 Life Point")

        item_window.destroy()

        if life_points <= 0:
            end_game("lose")
        elif len(mission_items) == 4:
            end_game("win")
        else:
            start_game_window()

    item_window = tk.Toplevel()
    item_window.title("Pick an Item")

    tk.Label(item_window, text=f"Choose one item from: {room.items}", font=("Arial", 12)).pack(pady=10)

    for item in room.items:
        tk.Button(item_window, text=item, command=lambda i=item: item_choice(i)).pack(pady=5)

def end_game(outcome):
    """
    End game with message and ask for leaderboard name
    """
    result_window = tk.Tk()
    result_window.title("Game Over")

    if outcome == "win":
        msg = "You escaped the forest with all magical items!"
    else:
        msg = "You lost all life points! The forest has captured you..."

    tk.Label(result_window, text=msg, font=("Arial", 14)).pack(pady=10)
    tk.Label(result_window, text="Enter your name for the leaderboard:").pack(pady=5)

    name_entry = tk.Entry(result_window)
    name_entry.pack(pady=5)

    def save_and_exit():
        name = name_entry.get().strip()
        if name:
            update_leaderboard(name)
        result_window.destroy()

    tk.Button(result_window, text="Save and Exit", command=save_and_exit).pack(pady=10)

def start_gui():
    """
    Initial GUI welcome screen with start and leaderboard buttons
    """
    welcome = tk.Tk()
    welcome.title("Spooky Forest Adventure")

    tk.Label(welcome, text="Welcome to the Spooky Forest Adventure!", font=("Arial", 14)).pack(pady=20)
    tk.Button(welcome, text="Start Game", command=lambda: [welcome.destroy(), start_game_window()]).pack(pady=10)
    tk.Button(welcome, text="View Leaderboard", command=show_leaderboard).pack(pady=5)
    tk.Button(welcome, text="Quit", command=welcome.destroy).pack(pady=10)

    welcome.mainloop()

def show_leaderboard():
    """
    Display leaderboard from file in new window
    """
    lb_win = tk.Toplevel()
    lb_win.title("Leaderboard")

    tk.Label(lb_win, text="Leaderboard", font=("Arial", 14)).pack(pady=10)

    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as f:
            content = f.read()
    else:
        content = "No entries yet."

    text_box = tk.Text(lb_win, height=15, width=50)
    text_box.insert(tk.END, content)
    text_box.config(state=tk.DISABLED)
    text_box.pack(pady=10)

# ---------- RUN GAME ----------
if __name__ == "__main__":
    start_gui()
