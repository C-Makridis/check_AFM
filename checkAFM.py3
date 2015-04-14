#!/usr/bin/env python3
import sys
if sys.version_info[0] < 3:
  sys.exit("This script depends on Python 3. Aborting!")

def checkAFM(afm):
  """ Check the validity of an AFM number.
      This only checks if it is a valid AFM number, not if it is actually used.
      Input should be given as a string, a check is made, but under certain conditions, an exception whould be thrown with integers. (hint: leading zeros mean an octal system... there is no '8' or '9' in the octal system) """
  if not isinstance(afm, str):
    raise TypeError( "checkAFM()", "You should feed to this function only strings to avoid exceptions and errors! Aborting." )
  if len(afm) == 11 and afm[:2].upper() == "EL":
    afm=afm[2:]
  if afm.isdigit() == True and len(afm) == 9: # simple initial check to see if the input has the sorrect length and is consisted by numbers
    i, sums = 256, 0
    for digit in afm[:-1]:
      sums += int(digit) * i
      i /= 2
    checksum = sums % 11
    if int(afm[-1]) == int(checksum) or (checksum==10 and afm[-1]=="0"):
      return True
  return False
#========================================================================

def tui():
  #If executed from console, with arguments
  
  counter={"True":0, "False":0} #just to show some statistics at the end
  
  def filter_output(afm, applied_filter):
    result = checkAFM(afm)
    counter[str(result)] += 1
    if applied_filter == None:
      return afm + "\t" + result + "\n"
    elif applied_filter == True and result == True:
      return afm + "\n"
    elif applied_filter == False and result == False:
      return afm + "\n"
  
  import argparse
  arg_parser = argparse.ArgumentParser(description = "Utility to check if input is a valid AFM (Greek VAT number). Input file should have one entry per line",
				       epilog="Note that -t and -f are mutually exclusive.")
  arg_parser.add_argument("-t", "--true_only", dest="results", action="store_const", const=True, default=None,
			  help="Return only a list of valid AFM's. Breaks -f!")
  arg_parser.add_argument("-f", "--false_only", dest="results", action="store_const", const=False, default=None,
			  help="Return only a list of invalid AFM's. Breaks -t!")
  arg_parser.add_argument("-i", "--input_file", nargs=1, help="File to read AFM's from. It should have one entry per line.")
  arg_parser.add_argument("-o", "--output_file", nargs=1, help="File to save results to.")
  arg_parser.add_argument("-s", "--stats", action="store_const", const=True, help="Show number of valid and invalid AFM's at the end.")
  arg_parser.add_argument("-v", "--version", action="version", version="P3x / 1.0")
  arg_parser.add_argument("AFM", nargs="*")
  args = arg_parser.parse_args()

  if args.output_file:
    try:
      output_file = open(args.output_file[0], "w")
    except:
      sys.exit("Unable to create file '"+ args.output_file[0]+"'. Aborting")

  if args.input_file:
    try:
      input_file = open(args.input_file[0], "r")
    except:
      sys.exit("Unable to open file '"+ args.input_file[0]+"'. Aborting")
    for line in input_file:
      a = filter_output(line.strip(), args.results)
      if a != None:
        if args.output_file:
          output_file.write(a)
        else:
          print(a.strip())

  if args.AFM:
    for afm in args.AFM:
      a = filter_output(afm, args.results)
      if a != None:
        if args.output_file:
          output_file.write(a) 
        else:
          print(a.strip())
  if args.stats:
    if args.output_file:
      output_file.write("---------\n" + str(counter["True"]) + " valid and " + str(counter["False"]) + 
	" invalid AFM's where found in a total of " + str( counter["True"] + counter["False"] ) + " entries.")
    else:
      print("---------\n" + str(counter["True"]) + " valid and " + str(counter["False"]) + 
	" invalid AFM's where found in a total of " + str( counter["True"] + counter["False"] ) + " entries.")
#========================================================================
def gui():
  try:
    from tkinter import Tk, ttk
    from tkinter.ttk import Button, Entry, Label, Style
  except:
    sys.exit("tkinter does not seem to be available at your system. Aborting.")
  
  def checkme(): #check the input and accordingly give the output...
    if txt_f_single_entry.get()=="":
      lbl_f_single_result.config(text="", style="TLabel")
    elif checkAFM(txt_f_single_entry.get()):
      lbl_f_single_result.config(text="Έγκυρο ΑΦΜ.", style="valid.TLabel")
    else:
      lbl_f_single_result.config(text="Άκυρο ΑΦΜ.", style="invalid.TLabel")

  #create the window
  main_window = Tk()
  main_window.title("Έλεγχος εγκυρότητας Α.Φ.Μ.")
  main_window.geometry("400x150")
  main_window.minsize(400,150)

  #fool arround with styling
  style = ttk.Style()
  style.configure("valid.TLabel", background="green")
  style.configure("empty.TLabel", background="white")
  style.configure("invalid.TLabel", background="red")
  style.configure("TNotebook", padding = 10)
  
  #create the Notebook
  tabs = ttk.Notebook(main_window)
  f_single = ttk.Frame(tabs)
  f_file = ttk.Frame(tabs)
  tabs.add(f_single, text="Μεμονομένα Α.Φ.Μ.")
  tabs.add(f_file, text="Λίστα από αρχείο")
  tabs.pack()
  
  #add some widgets in f_single tab
  lbl_f_single_instructions = Label(f_single, text="Εισάγετε έναν ΑΦΜ για έλεγχο")
  lbl_f_single_instructions.grid(column=0, row=0)

  lbl_f_single_result = Label(f_single, text="", width=10, justify="center")
  lbl_f_single_result.grid(column=1, row=0, rowspan=3, sticky="ewns")

  txt_f_single_entry = Entry(f_single)
  txt_f_single_entry.focus()
  txt_f_single_entry.bind("<Return>", lambda event: checkme() )
  txt_f_single_entry.bind("<KP_Enter>", lambda event: checkme() )
  txt_f_single_entry.grid(column=0,row=1)

  Button_f_single_submit = Button(f_single, text="Έλεγχος", command=checkme)
  Button_f_single_submit.grid(column=0,row=2)

  main_window.mainloop()
#========================================================================
if __name__ == "__main__":
  if len( sys.argv ) > 1: tui()
  else: gui()