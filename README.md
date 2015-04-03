# check AFM
Simple python script with Tkinter interface to check the validity of an AFM (Greek VAT Identification Number), based on its check digit.

Not very usefull, it is just my first attempt with Python, Tkinter and github.

It does work, but I do not think someome will find it useful. Maybe just the fuction checkAFM() so as not to re invent the wheel.

I have not yet confirmed compatibility with Python 3.X

#USAGE
##Command line
simply run tk_checkAFM.py from command line followed by any number of AFM's you want to check, one after the other, space seperated.

e.g.: 
```./tk_checkAFM.py 012345678 123456789 234567890```
or
```python tk_checkAFM.py 012345678 123456789 234567890```

Returns a tab seperated list of AFM's, followed by either "True" (=valid AFM) or "False".

##GUI
Just double click.... I think it's quite self-explanatory
You could also launch from console without any arguments.
