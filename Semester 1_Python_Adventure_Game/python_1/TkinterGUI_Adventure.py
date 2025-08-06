# Spooky Forest Adventure Game with Full GUI and Pictures

# ---------- CONSTANTS ----------
MAX_LIFE_POINTS = 5
SAVE_FILE = "save_file.txt"
LEADERBOARD_FILE = "leaderboard.txt"

# ---------- IMPORTS ----------
import random
import tkinter as tk
from tkinter import messagebox, PhotoImage
import os
from collections import namedtuple

# ---------- VARIABLES ----------
life_points = MAX_LIFE_POINTS
mission_items = []
wrong_items = []
visited_rooms = []

# ---------- ROOM DATA USING NAMED TUPLES ----------
Room = namedtuple("Room", ["name", "question", "answer", "items", "image"])

room_data = [
    Room("Dark Cave", "What color do you get when you mix red and blue?", "purple", ["magic stone", "stick"], "images/dark_cave.png"),
    Room("Misty Pond", "What gas do plants breathe in?", "carbon dioxide", ["magic water", "mud"], "images/misty_pond.png"),
    Room("Old Cabin", "How many legs does a spider have?", "8", ["magic lantern", "old boot"], "images/old_cabin.png"),
    Room("Hidden Grove", "What planet do we live on?", "earth", ["magic compass", "leaf"], "images/hidden_grove.png")
]

room_dict = {room.name: room for room in room_data}
rooms = [room.name for room in room_data]

# ---------- LOAD AND SAVE ----------
def save_game():
    with open(SAVE_FILE, "w") as f:
        f.write(f"{life_points}\n")
        f.write(",".join(mission_items) + "\n")
        f.write(",".join(visited_rooms) + "\n")

def load_game():
    global life_points, mission_items, visited_rooms
    try:
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()
            life_points = int(lines[0].strip())
            mission_items = lines[1].strip().split(",") if lines[1].strip() else []
            visited_rooms = lines[2].strip().split(",") if lines[2].strip() else []
    except:
        pass

def update_leaderboard(name):
    with open(LEADERBOARD_FILE, "a") as f:
        f.write(f"{name} - Items: {len(mission_items)} - Life Points: {life_points}\n")

# ---------- GUI FUNCTIONS ----------
def start_gui():
    def start_game():
        window.destroy()
        load_game()
        game_window()

    def view_leaderboard():
        try:
            with open(LEADERBOARD_FILE, "r") as f:
                leaderboard_text = f.read()
        except FileNotFoundError:
            leaderboard_text = "No leaderboard data yet."

        leaderboard_window = tk.Toplevel(window)
        leaderboard_window.title("Leaderboard")
        tk.Label(leaderboard_window, text="Leaderboard", font=("Arial", 14)).pack(pady=5)
        tk.Message(leaderboard_window, text=leaderboard_text, width=400).pack(padx=10, pady=10)

    window = tk.Tk()
    window.title("Spooky Forest Adventure")
    tk.Label(window, text="Welcome to the Spooky Forest Adventure!", font=("Arial", 16)).pack(pady=20)
    tk.Button(window, text="Start Game", command=start_game, width=20).pack(pady=5)
    tk.Button(window, text="View Leaderboard", command=view_leaderboard, width=20).pack(pady=5)
    tk.Button(window, text="Exit", command=window.destroy, width=20).pack(pady=5)
    window.mainloop()

# ---------- GAME GUI LOGIC ----------
def game_window():
    root = tk.Tk()
    root.title("Game in Progress")

    question_label = tk.Label(root, text="", font=("Arial", 14))
    question_label.pack(pady=10)

    image_label = tk.Label(root)
    image_label.pack()

    item_buttons = []

    def show_room(room_name):
        room = room_dict[room_name]
        visited_rooms.append(room_name)

        question_label.config(text=f"{room.name}: {room.question}")

        try:
            img = PhotoImage(file=room.image)
            image_label.config(image=img)
            image_label.image = img
        except:
            image_label.config(image="", text="[Image not found]", font=("Arial", 12))

        for btn in item_buttons:
            btn.destroy()
        item_buttons.clear()

        def handle_answer(is_correct):
            nonlocal room
            global life_points

            if is_correct:
                messagebox.showinfo("Correct", "You gain a life point!")
                life_points += 1
            else:
                messagebox.showerror("Wrong", "You lose a life point!")
                life_points -= 1

            question_label.config(text=f"Pick an item:")

            for item in room.items:
                def make_handler(item=item):
                    def choose():
                        if item.startswith("magic"):
                            mission_items.append(item)
                            messagebox.showinfo("Item", f"You found a mission item: {item}!")
                        else:
                            wrong_items.append(item)
                            messagebox.showwarning("Wrong Item", f"That was the wrong item! -1 Life")
                            global life_points
                            life_points -= 1
                        next_turn()
                    return choose

                btn = tk.Button(root, text=item, command=make_handler(item))
                btn.pack(pady=2)
                item_buttons.append(btn)

        # Answer buttons
        tk.Button(root, text="Answer: " + room.answer, command=lambda: handle_answer(True)).pack()
        tk.Button(root, text="Wrong Answer", command=lambda: handle_answer(False)).pack()

    def next_turn():
        if life_points <= 0:
            messagebox.showinfo("Game Over", "You ran out of life points. The wizard captures you forever!")
            root.destroy()
        elif len(mission_items) == 4:
            name = tk.simpledialog.askstring("Victory!", "You escaped! Enter your name for the leaderboard:")
            if name:
                update_leaderboard(name)
            root.destroy()
        else:
            for widget in root.winfo_children():
                widget.destroy()
            available = [r for r in rooms if r not in visited_rooms]
            tk.Label(root, text="Choose a room:", font=("Arial", 14)).pack(pady=10)
            for r in available:
                tk.Button(root, text=r, command=lambda r=r: show_room(r)).pack(pady=2)

    next_turn()
    root.mainloop()

# ---------- RUN GAME ----------
if __name__ == "__main__":
    start_gui()
