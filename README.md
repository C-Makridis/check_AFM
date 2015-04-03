# check AFM
Simple python script with Tkinter interface to check the validity of an AFM (Greek VAT Identification Number), based on its check digit.

Not very usefull, it is just my first attempt with Python, Tkinter and github.

It does work, but I do not think someome will find it useful. Maybe just the fuction checkAFM() so as not to re invent the wheel.

I have not yet confirmed compatibility with Python 3.X

It does recognise the international form of an AFM (prefixed with EL)

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

#TODO:
More like a list of thinks that come to my mind that could be done, not that will be done necessarily.
* alter the GUI to accept a list of values
* maybe give an option to pass valid AFM's to web services like http://ec.europa.eu/taxation_customs/vies/vatRequest.html
* test in other platforms (Windows / MacOS) and python versions
* make it possible to execute without arguments from console, for computers without a desktop environment
* add support for other countries