import tkinter
from tkinter import ttk

root= tkinter.Tk()
root.geometry("1000x500")

frame1 = tkinter.Frame(root, padx=20, pady=20, bg="#ff0000")
frame2 = tkinter.Frame(root, padx=20, pady=20, bg="#00ff00")

frame1.grid()
frame2.grid()

button = tkinter.Button(frame1, text="Cliquez ici !")
button2 = tkinter.Button(frame2, text="Cliquez ici !")

button.grid()
button2.grid()

root.mainloop()