import tkinter as tk
import pyautogui as screen
import random
import time
import threading
import ctypes
import sys

# Global variables
running = True

# Function to move the cursor randomly
def move_cursor():
    x, y = screen.size()
    x1 = random.randint(0, x)
    y1 = random.randint(0, y)
    screen.moveTo(x1, y1)

# Function to start the cursor movement
def start_movement():
    global running
    running = True

    # Disable the start button once it's clicked
    start_button.config(state=tk.DISABLED)

    # Enable the stop and close buttons
    stop_button.config(state=tk.NORMAL)
    close_button.config(state=tk.NORMAL)

    # Print the start message
    print("Program Executes...")

    # Start moving the cursor in a separate thread
    def move_cursor_thread():
        while running:
            time.sleep(3)
            move_cursor()
            time.sleep(5)

    # Create and start the cursor movement thread
    movement_thread = threading.Thread(target=move_cursor_thread)
    movement_thread.start()

# Function to stop the cursor movement
def stop_movement():
    global running
    running = False

    # Disable the stop button
    stop_button.config(state=tk.DISABLED)

    # Enable the start button
    start_button.config(state=tk.NORMAL)

    # Print the termination message
    print("The code has been terminated by the user...")

# Function to close the application
def close_application():
    print("Application Closed")
    window.destroy()
    sys.exit()

# Create the main Tkinter window
window = tk.Tk()

# Set the title bar color for Windows
if sys.platform.startswith('win'):
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    window.attributes('-toolwindow', True)

window.title("Cursor Movement Automation")
window.geometry("800x600")  # Set the window size
window.configure(bg="black")  # Set the background color

# Create a large-sized container
container = tk.Frame(window, bg="black", width=700, height=500)
container.pack(pady=50)

# Create a label for the title
title_label = tk.Label(container, text="Cursor Movement Automation", font=("Arial", 24), fg="white", bg="black")
title_label.pack(pady=20)

# Create a start button
start_button = tk.Button(container, text="Start", font=("Arial", 14), fg="white", bg="green", command=start_movement, width=10)
start_button.pack(pady=10)

# Create a stop button
stop_button = tk.Button(container, text="Stop", font=("Arial", 14), fg="white", bg="red", command=stop_movement, state=tk.DISABLED, width=10)
stop_button.pack(pady=10)

# Create a close button
close_button = tk.Button(container, text="Close", font=("Arial", 8), fg="white", bg="gray", command=close_application, width=10)
close_button.pack(pady=10)

# Center align the widgets
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# label for the code editor
creator_label = tk.Label(window, text="Shiwarne Silva\nTrainee HelpDesk Executive", font=("Arial", 10), fg="white", bg="black")
creator_label.place(relx=1, rely=1, anchor=tk.SE, x=-10, y=-10)

# Start the Tkinter event loop
window.mainloop()
