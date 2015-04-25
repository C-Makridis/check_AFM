#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Check the validity of an AFM number (Greek VAT code).

Only this modules check_afm() funtion is usable by importing it.
Please review check_afm.__doc__
"""
def check_afm(afm):
  """Check the validity of an AFM number (Greek VAT code).

  Check if input is a valid AFM number via its check digit (not if it is actually used).
  Return either True of False.
  Input should be given as a string. An integer, under certain conditions, could through an exception.
  """
  
  if not isinstance(afm, str):
    raise TypeError( "check_afm()", "You should feed to this function only strings to avoid exceptions and errors! Aborting." )
  if len(afm) == 11 and afm[:2].upper() == "EL":
    afm=afm[2:]
  if afm.isdigit() == True and len(afm) == 9:
    i, sums = 256, 0
    for digit in afm[:-1]:
      sums += int(digit) * i
      i /= 2
    checksum = sums % 11
    if int(afm[-1]) == int(checksum) or (checksum==10 and afm[-1]=="0"):
      return True
  return False
#========================================================================

def _tui():
  #If executed from console, with arguments
  
  counter={True:0, False:0} #just to show some statistics at the end
  
  def _filter_output(afm, applied_filter):
    result = check_afm(afm)
    counter[result] += 1
    if applied_filter == None:
      return afm + "\t" + str(result) + "\n"
    elif applied_filter == True and result == True:
      return afm + "\n"
    elif applied_filter == False and result == False:
      return afm + "\n"
  
  import argparse
  arg_parser = argparse.ArgumentParser(description = "Utility to check if input is a valid AFM (Greek VAT number). Input file should have one entry per line", epilog="Note that -t and -f are mutually exclusive.")
  arg_parser.add_argument("-t", "--true_only", dest="results", action="store_const", const=True, default=None,
			  help="Return only a list of valid AFM's. Breaks -f!")
  arg_parser.add_argument("-f", "--false_only", dest="results", action="store_const", const=False, default=None,
			  help="Return only a list of invalid AFM's. Breaks -t!")
  arg_parser.add_argument("-i", "--input_file", nargs=1, help="File to read AFM's from. It should have one entry per line.")
  arg_parser.add_argument("-o", "--output_file", nargs=1, help="File to save results to.")
  arg_parser.add_argument("-s", "--stats", action="store_const", const=True, help="Show number of valid and invalid AFM's at the end.")
  arg_parser.add_argument("-v", "--version", action="version", version="P3x / 2.0")
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
      a = _filter_output(line.strip(), args.results)
      if a != None:
        if args.output_file:
          output_file.write(a)
        else:
          print(a.strip())

  if args.AFM:
    for afm in args.AFM:
      a = _filter_output(afm, args.results)
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
      print("---------\n" + str(counter[True]) + " valid and " + str(counter[False]) + 
	" invalid AFM's where found in a total of " + str( counter[True] + counter[False] ) + " entries.")
#========================================================================
def _gui():
  try:
    from tkinter import Tk, ttk, filedialog, messagebox, StringVar, IntVar
    from tkinter.ttk import Button, Entry, Frame, Label, LabelFrame, Notebook, Radiobutton, Style
  except:
    sys.exit("Unable to load tkinter. Aborting.")
  
  def _check_single(): #check the input and accordingly give the output... for the f_single tab
    if txt_f_single_entry.get()=="":
      lbl_f_single_result.config(text="", style="TLabel")
    elif check_afm(txt_f_single_entry.get()):
      lbl_f_single_result.config(text="Έγκυρο ΑΦΜ.", style="valid.TLabel")
    else:
      lbl_f_single_result.config(text="Άκυρο ΑΦΜ.", style="invalid.TLabel")
  
  def _select_input_file():
    strv_f_file_input.set(filedialog.askopenfilename(title="Άνοιγμα αρχείου"))
    if strv_f_file_input.get() != "" and strv_f_file_output.get() != "":
      btn_f_file_submit.config(state="normal")
    else: btn_f_file_submit.config(state="disabled")
#TODO a much better mechanism to enable / disable btn_f_file_submit is needed.
  def _select_output_file():
    strv_f_file_output.set(filedialog.asksaveasfilename(title="Αποθήκευση ως..."))
    if strv_f_file_input.get() != "" and strv_f_file_output.get() != "":
      btn_f_file_submit.config(state="normal")
    else: btn_f_file_submit.config(state="disabled")
  
  def _check_file():#TODO this could / should be merged with the TUI version...
    input_filepath = strv_f_file_input.get()
    output_filepath = strv_f_file_output.get()
    filter_output = intvar_filter_sel.get()
    try:
      input_file = open(input_filepath, "r")
      output_file = open(output_filepath, "w")
    except:
      messagebox.showerror(title="Σφάλμα", message="Αδυναμία διαχείρησης των αρχείων που ορίσατε.\n\nΠαρακαλώ επιβεβαιώστε πως το αρχείο με τα δεδομένα υπάρχει, πως έχετε δικαιώματα ανάγνωσης, και πως έχετε δικαιώματα εγγραφής στον κατάλογο εξαγωγής των αποτελεσμάτων.")
      return
    counter = {True:0, False:0}
    for entry in input_file:
      validation = check_afm(entry.strip())
      counter[validation]+=1
      if filter_output == 3 and validation == False:
        output_file.write(entry)
      elif filter_output == 2 and validation == True:
        output_file.write(entry)
      elif filter_output == 1:
        output_file.write(entry.strip() + "\t" + str(validation) + "\n\r")
    lbl_f_file_result.config(text="Σύνολο: "+str(counter[True]+counter[False])+"\nΈγκυρα: "+str(counter[True])+"\nΆκυρα: "+str(counter[False]))

  #create the window
  main_window = Tk()
  main_window.title("Έλεγχος εγκυρότητας Α.Φ.Μ. (v 2.0)")
  main_window.geometry("600x180")
  main_window.minsize(600,180)

  #fool arround with styling
  style = ttk.Style()
  style.configure("valid.TLabel", background="green")
  style.configure("empty.TLabel", background="white")
  style.configure("invalid.TLabel", background="red")
  style.configure("TNotebook", padding = 10)
  
  #create the Notebook
  tabs = Notebook(main_window)
  f_single = Frame(tabs)
  f_file = Frame(tabs)
  tabs.add(f_single, text="Μεμονομένα Α.Φ.Μ.")
  tabs.add(f_file, text="Λίστα από αρχείο")#add state="disabled" prior to git push until ready
  tabs.pack(anchor="nw")
  
  #add some widgets in f_single tab
  lbl_f_single_instructions = Label(f_single, text="Εισάγετε έναν ΑΦΜ για έλεγχο")
  lbl_f_single_instructions.grid(column=0, row=0)

  lbl_f_single_result = Label(f_single, text="", width=10, justify="center")
  lbl_f_single_result.grid(column=1, row=0, rowspan=2, sticky="ewns")

  txt_f_single_entry = Entry(f_single, width=11)
  txt_f_single_entry.focus()
  txt_f_single_entry.bind("<KeyRelease>", lambda e: _check_single() )
  txt_f_single_entry.grid(column=0,row=1)

  #btn_f_single_submit = Button(f_single, text="Έλεγχος", command=_check_single)
  #btn_f_single_submit.grid(column=0,row=2)
    
  #add some widgets in f_file tab
  lbl_f_file_finput = Label(f_file, text="Άνοιγμα...")
  lbl_f_file_finput.grid(column=0, row=0)
  strv_f_file_input = StringVar()
  txt_f_file_finput = Entry(f_file, textvariable = strv_f_file_input)
  txt_f_file_finput.grid(column=1, row=0)
  btn_f_file_finput = Button(f_file, text="...", width=3, command=_select_input_file)
  btn_f_file_finput.grid(column=2, row=0, sticky="W")
  
  lbl_f_file_foutput = Label(f_file, text="Αποθήκευση ως...")
  lbl_f_file_foutput.grid(column=0, row=1)
  strv_f_file_output = StringVar()
  txt_f_file_foutput = Entry(f_file, textvariable = strv_f_file_output)
  txt_f_file_foutput.grid(column=1, row=1)
  btn_f_file_foutput = Button(f_file, text="...", width=3, command=_select_output_file)
  btn_f_file_foutput.grid(column=2, row=1, sticky="W")
  
  lf_filter = LabelFrame(f_file, text="Επιστροφή")
  lf_filter.grid(column=3, row=0, rowspan=2, sticky="ewns")
  intvar_filter_sel = IntVar()
  rb_filter_all = Radiobutton(lf_filter, text="Όλων", variable=intvar_filter_sel, value=1) #TODO maybe add command
  rb_filter_all.pack(anchor="w")
  rb_filter_all.invoke()
  rb_filter_true = Radiobutton(lf_filter, text="Έγκυρων", variable=intvar_filter_sel, value=2)
  rb_filter_true.pack(anchor="w")
  rb_filter_false = Radiobutton(lf_filter, text="Άκυρων", variable=intvar_filter_sel, value=3)
  rb_filter_false.pack(anchor="w")
  
  lf_result = LabelFrame(f_file, text="Σύνοψη")
  lf_result.grid(column=4, row=0, rowspan=2, sticky="ewns")
  lbl_f_file_result = Label(lf_result, text="", width=12)#TODO bring results
  lbl_f_file_result.pack()
  
  btn_f_file_submit = Button(f_file, text="Επεξεργασία", state="disabled", command=_check_file)
  btn_f_file_submit.grid(column=0, row=2, columnspan=3)
  
  btn_main_exit = Button(main_window, text="Έξοδος", command=sys.exit)
  btn_main_exit.pack(anchor="se")

  main_window.mainloop()
#========================================================================
if __name__ == "__main__":
  import sys
  if sys.version_info[0] < 3:
    sys.exit("This script depends on Python 3. You can not run it with Python 2, but you can import and use its main funtion check_afm().")
  if len( sys.argv ) > 1: _tui()
  else: _gui()