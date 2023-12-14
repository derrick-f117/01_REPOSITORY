import tkinter as tk

def submit():
    # Retrieve answers from entry widgets
    answer1 = entry1.get()
    answer2 = entry2.get()

    # Print or process the answers as needed
    print("Answer 1:", answer1)
    print("Answer 2:", answer2)

# Create the main window
window = tk.Tk()
window.title("Questionnaire")

# Create and place question labels
label1 = tk.Label(window, text="What is your name?")
label1.pack()

# Create and place entry widget for answer 1
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="How old are you?")
label2.pack()

# Create and place entry widget for answer 2
entry2 = tk.Entry(window)
entry2.pack()

# Create and place submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Run the application
window.mainloop()
