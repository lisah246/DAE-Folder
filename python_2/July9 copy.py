import time
import threading
import sys
from datetime import timedelta

# Global flags
stop_timer = False
pause_timer = False

def format_duration(seconds):
    return str(timedelta(seconds=int(seconds)))

def show_timer(start_time, pause_durations):
    while not stop_timer:
        if not pause_timer:
            current_time = time.time()
            total_pause = sum(pause_durations)
            elapsed = int(current_time - start_time - total_pause)
            sys.stdout.write(f"\rElapsed Time: {format_duration(elapsed)}")
            sys.stdout.flush()
        time.sleep(1)

def save_to_file(tasks):
    with open("task_log.txt", "a") as f:
        for task in tasks:
            f.write(f"Task: {task['name']}\n")
            f.write(f"Started: {task['start']}\n")
            f.write(f"Ended:   {task['end']}\n")
            f.write(f"Duration: {format_duration(task['duration'])}\n")
            f.write("-" * 40 + "\n")
        total_time = sum(task['duration'] for task in tasks)
        f.write(f"\n🧮 Total Time Tracked: {format_duration(total_time)}\n")
        f.write("=" * 40 + "\n")
    print("📝 Task log saved to 'task_log.txt'.")

def show_summary(tasks):
    print("\n📋 Task Summary:")
    for idx, task in enumerate(tasks, 1):
        print(f"\nTask {idx}: {task['name']}")
        print(f"  Started:  {task['start']}")
        print(f"  Ended:    {task['end']}")
        print(f"  Duration: {format_duration(task['duration'])}")
    total_time = sum(task['duration'] for task in tasks)
    print(f"\n🧮 Total Time Tracked: {format_duration(total_time)}")

def main():
    global stop_timer, pause_timer
    tasks = []

    print("\n🎯 Welcome to the Python Task Tracker!\n")

    while True:
        task_name = input("Enter the task name: ")

        # Initial instructions
        print("Press ENTER to START the task...")
        print("Press ENTER again to END the task...")
        print("Other Commands: [p] Pause | [r] Resume")

        input()  # Wait for ENTER to start
        start_time = time.time()
        pause_durations = []
        current_pause_start = None

        print("Task Started.")

        stop_timer = False
        pause_timer = False

        # Start the timer in a thread
        timer_thread = threading.Thread(target=show_timer, args=(start_time, pause_durations))
        timer_thread.start()

        while True:
            cmd = input("\nCommand (ENTER to end, p, r): ").strip().lower()

            if cmd == 'p':
                if not pause_timer:
                    pause_timer = True
                    current_pause_start = time.time()
                    print("⏸️  Task paused.")
                else:
                    print("Already paused.")
            elif cmd == 'r':
                if pause_timer:
                    pause_timer = False
                    pause_durations.append(time.time() - current_pause_start)
                    print("▶️  Task resumed.")
                else:
                    print("Task is not paused.")
            elif cmd == '':
                if pause_timer:
                    pause_durations.append(time.time() - current_pause_start)
                stop_timer = True
                timer_thread.join()
                break
            else:
                print("Invalid input. Use ENTER, 'p' to pause, or 'r' to resume.")

        end_time = time.time()
        total_pause = sum(pause_durations)
        duration = round(end_time - start_time - total_pause, 2)

        print(f"\n⏹️ Task '{task_name}' ended at {time.ctime(end_time)}.")
        print(f"🕒 Total Duration (excluding pauses): {format_duration(duration)}\n")

        task_info = {
            "name": task_name,
            "start": time.ctime(start_time),
            "end": time.ctime(end_time),
            "duration": duration
        }

        tasks.append(task_info)

        print("What would you like to do next?")
        print("  1. Track another task")
        print("  2. Show summary and exit")
        print("  3. Show summary, save to file, and exit")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            continue
        elif choice == "2":
            show_summary(tasks)
            print("\n🎉 Congratulations! You have completed your task(s)!")
            break
        elif choice == "3":
            show_summary(tasks)
            save_to_file(tasks)
            print("\n🎉 Congratulations! You have completed your task(s)!")
            break
        else:
            print("Invalid input. Exiting the program.")
            break

if __name__ == "__main__":
    main()
