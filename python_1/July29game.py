import tkinter as tk
from tkinter import messagebox
import random
import json

# -----------------------------
# Global Game State
# -----------------------------
rooms = {
    "Clearing": {
        "description": "A small clearing in the spooky forest.",
        "exits": {"north": "Dark Cave", "south": "Old Cabin", "east": "Misty Pond", "west": "Hidden Grove"},
        "items": []
    },
    "Dark Cave": {
        "description": "A damp, pitch-black cave.",
        "exits": {},
        "items": ["flashlight", "broken stick"]
    },
    "Old Cabin": {
        "description": "An abandoned cabin.",
        "exits": {},
        "items": ["map", "old shoe"]
    },
    "Misty Pond": {
        "description": "A foggy pond.",
        "exits": {},
        "items": ["compass", "strange feather"]
    },
    "Hidden Grove": {
        "description": "A glowing grove.",
        "exits": {},
        "items": ["fire kit", "rusty can"]
    }
}

quizzes = [
    {"category": "Math", "question": "What is 15% of $200?", "choices": ["$20", "$30", "$25"], "answer": "$30"},
    {"category": "Budgeting", "question": "You save $15/week for 4 weeks. How much?", "choices": ["$45", "$60", "$75"], "answer": "$60"}
    # Add more if needed
]

hazards = [
    {"scenario": "Dragon blocks path!", "choices": ["Dive into river", "Throw rocks"], "answer": "Dive into river"},
    {"scenario": "Swarm of bees!", "choices": ["Cover in mud", "Wave arms"], "answer": "Cover in mud"}
]

mission_items = {"flashlight", "map", "compass", "fire kit"}

current_room = "Clearing"
inventory = []
life_points = 0
score_breakdown = {"Quiz": 0, "Hazards": 0, "Items": 0}

# -----------------------------
# GUI App
# -----------------------------
class SpookyForestGame:
    def __init__(self, master):
        self.master = master
        master.title("Spooky Forest Adventure")

        self.text = tk.Label(master, text="Welcome to the Spooky Forest Adventure!", font=("Arial", 14), wraplength=400)
        self.text.pack(pady=10)

        self.info = tk.Label(master, text="", font=("Arial", 10))
        self.info.pack()

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Button(self.buttons_frame, text="", width=30, command=lambda i=_: self.option_click(i))
            btn.grid(row=_, column=0, pady=2)
            self.option_buttons.append(btn)

        self.state = "start"
        self.next()

    def set_options(self, options):
        for i, text in enumerate(options):
            self.option_buttons[i].config(text=text, state="normal")
        for j in range(len(options), 4):
            self.option_buttons[j].config(text="", state="disabled")

    def option_click(self, i):
        self.choice = self.option_buttons[i].cget("text")
        self.next()

    def next(self):
        global current_room, inventory, life_points
        if self.state == "start":
            self.text.config(text="Do you want to start your adventure?")
            self.set_options(["Yes", "No"])
            self.state = "intro"

        elif self.state == "intro":
            if self.choice == "No":
                self.text.config(text="You chose not to proceed. Game over.")
                self.set_options([])
                return
            self.state = "move"
            self.next()

        elif self.state == "move":
            self.text.config(text=f"You are in the {current_room}. Choose a direction:")
            self.set_options(["north", "south", "east", "west"])
            self.state = "quiz"

        elif self.state == "quiz":
            self.direction = self.choice
            self.quiz = random.choice(quizzes)
            self.text.config(text=f"Quiz: {self.quiz['question']}")
            self.set_options(self.quiz["choices"])
            self.state = "quiz_result"

        elif self.state == "quiz_result":
            if self.choice == self.quiz["answer"]:
                life_points += 1
                score_breakdown["Quiz"] += 1
            else:
                life_points -= 1
            if life_points < 0:
                self.game_over()
                return
            room_map = {"north": "Dark Cave", "south": "Old Cabin", "east": "Misty Pond", "west": "Hidden Grove"}
            current_room = room_map[self.direction]
            self.state = "item"
            self.next()

        elif self.state == "item":
            items = rooms[current_room]["items"]
            if not items:
                self.text.config(text="No more items here. Going back.")
                self.state = "hazard"
                self.set_options(["OK"])
                return
            self.text.config(text=f"Choose an item: {', '.join(items)}")
            self.set_options(items + ["Leave"])
            self.state = "item_result"

        elif self.state == "item_result":
            if self.choice == "Leave":
                self.state = "hazard"
                self.next()
                return
            if self.choice in rooms[current_room]["items"]:
                item = self.choice
                if item in mission_items:
                    inventory.append(item)
                    life_points += 1
                    score_breakdown["Items"] += 1
                    self.text.config(text=f"You picked {item}. +1 life point.")
                else:
                    life_points -= 1
                    self.text.config(text=f"{item} is cursed! -1 life point.")
                rooms[current_room]["items"].remove(item)
                if life_points < 0:
                    self.game_over()
                    return
                if mission_items.issubset(set(inventory)):
                    self.win()
                    return
                self.state = "hazard"
                self.set_options(["Continue"])

        elif self.state == "hazard":
            hazard = random.choice(hazards)
            self.hazard = hazard
            self.text.config(text=f"Hazard! {hazard['scenario']}")
            self.set_options(hazard["choices"])
            self.state = "hazard_result"

        elif self.state == "hazard_result":
            if self.choice == self.hazard["answer"]:
                life_points += 1
                score_breakdown["Hazards"] += 1
                self.text.config(text=f"Safe choice! +1 life point.")
            else:
                life_points -= 1
                self.text.config(text=f"Bad choice! -1 life point.")
            if life_points < 0:
                self.game_over()
                return
            self.state = "move"
            self.set_options(["Continue"])

        self.info.config(text=f"Room: {current_room} | Inventory: {', '.join(inventory)} | ❤️ {life_points}")

    def game_over(self):
        self.text.config(text="Game over. The forest swallows you whole.")
        self.set_options([])

    def win(self):
        self.text.config(text=f"🎉 You collected all items and escaped! Final life points: {life_points}")
        self.set_options([])

# -----------------------------
# Launch GUI
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SpookyForestGame(root)
    root.mainloop()
