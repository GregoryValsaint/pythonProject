import tkinter
window = tkinter.Tk()

canvas = tkinter.Canvas(window, bg="#ffffff")
canvas.pack(fill="both", expand=True)

#faire un diagonale
#canvas.create_line(0, 0, 500, 500)

#faire un cercle
canvas.create_oval(0, 0, 200, 200)
#canvas.grid(fill="both", expand=True)

window.mainloop()