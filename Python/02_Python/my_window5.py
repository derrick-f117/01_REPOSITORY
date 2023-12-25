import tkinter as tk

#Create window
window = tk.Tk()
window.title("I am a Window!🪟")
window.geometry("700x500")  #width x height

#Add content
content1 = tk.Label(window, text="I am the first content of this page!")
#content1.geometry("50x50")
content1.pack(pady="20")

#Run the app
window.mainloop()