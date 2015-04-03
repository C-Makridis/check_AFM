#!/usr/bin/env python
# -*- coding: utf-8 -*-

from my_functions import checkAFM
import Tkinter
from Tkinter import *

def checkme(): #check the input and accordingly give the output...
  if txt.get()=="":
    txt.config(bg="WHITE")
    lbl.config(text="Παρακαλώ εισάγετε έναν ΑΦΜ για έλεγχο")
  elif checkAFM(txt.get()):
    #print "OK"
    txt.config(bg="GREEN")
    lbl.config(text="Έγκυρο ΑΦΜ. Εισάγετε επόμενο")
  else:
    #print "Not OK"
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


#submit_btn = Button(main_window, text="Έλεγχος", command=checkme)
#submit_btn.pack()
#.pack() can be done in one step!
Button(main_window, text="Έλεγχος", command=checkme).pack()

# Go, Go, Go!!!!
main_window.mainloop()