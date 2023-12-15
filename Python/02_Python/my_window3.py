import tkinter as tk

def submit():
    answer1 = entry1.get()
    answer2 = entry2.get()

    print("Answer 1:" +str(answer1))
    print("Answer 2:" +str(answer2))

    if str(answer1) == "Derrick Abuga" and str(answer2) == "17":
        print("Welcome, Derrick@17")


window = tk.Tk()
window.title("Math Quiz")

label1 = tk.Label(window, text="What is your name?")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="How old are you?")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

window.mainloop()