# -*- coding: utf-8 -*-

import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("My Python Window")

# Set the window size
window.geometry("400x300")  # width x height

# Add content to the window (optional)
label = tk.Label(window, text="Hello, this is a window!")
label.pack(pady=20)  # Add padding to the label

# Run the Tkinter event loop
window.mainloop()
