from tkinter import *

w = Canvas(Tk(), width=900, height=400)
w.pack()

for i in range(300):
  x = i * 8

  if (i % 2) == 0:
    f = "#FFCC33"
  else:
    f = "#CC33FF"

  w.create_line(x, 0, x, 400, fill=f)

mainloop()