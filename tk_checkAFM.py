#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_functions import checkAFM
import Tkinter
from Tkinter import *
import sys

#If executed from console, with arguments
if len(sys.argv) > 1:
  for i in sys.argv[1:]:
    print i + "\t" + str(checkAFM(i))
  sys.exit(0)

#Or go for GUI
def checkme(): #check the input and accordingly give the output...
  if txt.get()=="":
    txt.config(bg="WHITE")
    lbl.config(text="Παρακαλώ εισάγετε έναν ΑΦΜ για έλεγχο")
  elif checkAFM(txt.get()):
    txt.config(bg="GREEN")
    lbl.config(text="Έγκυρο ΑΦΜ. Εισάγετε επόμενο")
  else:
    txt.config(bg = "RED" )
    lbl.config(text="Λάθος ΑΦΜ. Εισάγετε επόμενο")

#create the window
main_window = Tk()
main_window.title("Έλεγχος εγκυρότητας Α.Φ.Μ.")
main_window.geometry("300x70")
main_window.minsize(300,70)

#add some widgets in it
lbl = Label(main_window, text="Παρακαλώ εισάγετε έναν ΑΦΜ για έλεγχο")
lbl.pack()

txt = Entry(main_window)
txt.focus()
txt.bind("<Return>", lambda event: checkme() )
txt.bind("<KP_Enter>", lambda event: checkme() )
txt.pack()

Button(main_window, text="Έλεγχος", command=checkme).pack()

# Go, Go, Go!!!!
main_window.mainloop()