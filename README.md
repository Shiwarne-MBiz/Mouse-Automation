# Mouse-Automation

This code is a Python script that uses the Tkinter library to create a graphical user interface (GUI) for a cursor movement automation program. The program moves the cursor randomly on the screen at regular intervals.



> The code begins by importing the necessary libraries: tkinter for creating the GUI, pyautogui for controlling the cursor, and other standard libraries such as random, time, threading, ctypes, and sys.

> It defines a global variable running which will be used to control the cursor movement.

> The move_cursor function is responsible for generating random coordinates and moving the cursor to those coordinates using pyautogui.moveTo().

> The start_movement function is triggered when the user clicks the "Start" button in the GUI. It sets running to True, disables the "Start" button, enables the "Stop" button, and starts a separate thread to execute the move_cursor_thread function.

> The move_cursor_thread function continuously moves the cursor randomly every 3 seconds and waits for 5 seconds before the next movement. This loop runs as long as the running flag is True.

> The stop_movement function is triggered when the user clicks the "Stop" button. It sets running to False, disables the "Stop" button, enables the "Start" button, and stops the cursor movement.

> The code then creates the main Tkinter window and sets its attributes such as title, size, and background color.

> Various Tkinter widgets such as labels and buttons are created and placed inside a container frame using layout managers like pack() and place().

> The start_movement and stop_movement functions are assigned as commands to the "Start" and "Stop" buttons, respectively.

> Finally, the Tkinter event loop is started using window.mainloop(), which handles user interactions with the GUI.

This code can be used as a simple example of how to create a GUI in Tkinter and control cursor movement using pyautogui.
