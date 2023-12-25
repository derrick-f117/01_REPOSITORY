import tkinter as tk

#Create window and set dimensions
window = tk.Tk()
window.title("Hello World!")
window.geometry("600x500")

#CONTENT
label = tk.Label(window, text="I am contented")
label.pack(pady="20")

label2 = tk.Label(window, text="I am a second label🙂")
label2.pack(pady="20")

window.mainloop()