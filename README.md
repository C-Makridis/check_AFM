
# check AFM
Simple python script with Tkinter interface to check the validity of an AFM (Greek VAT Identification Number), based on its check digit.

Not very usefull, it is just an exercise for me with Python, Tkinter and github.

It does work (it has been tested against 8.000 valid AFM's), but I do not think someome will find it useful. Maybe just the fuction checkAFM() so as not to re-invent the wheel.

It is at this point compatible only with Python 3.x.

It does recognise the international form of an AFM (prefixed with EL)

It is one single file, that you could:
1. import to use checkAFM() function
2. execute from terminal:
..* to check a small number of inputs
..* to check any number of data from a txt file
..* output can be either a file or the standar output (aka your screen)
3. launch from your graphic enviroment and use its Graphical User Interface



#USAGE
##Command line
* `checkAFM.py` from command line followed by any number of AFM's you want to check, one after the other, space seperated.
* `checkAFM.py -i YOUR_FILE` to read data from a plain text file. It validates the whole line, so make sure the file has one AFM per line.
* `checkAFM.py -o FILE` to redirect output to a file.
* add `-t` to force the program return only data that are found to be valid AFM's.
* add `-f` to force the program return only data that are found to by invalid AFM's.

Note that `-t` and `-f` are mutually exclusive.
If you ommit both of them, instead of a list of data, you would get a tab seperated set of AFM's with either `True` or `False` next to it.

* `checkAFM.py -h` would return instructions for the syntax, while `checkAFM.py -v` would return it's version.


e.g.: 
```./checkAFM.py 012345678 123456789 234567890```
or
```python checkAFM.py 012345678 123456789 234567890```

Returns a tab seperated list of AFM's, followed by either "True" (=valid AFM) or "False".

```checkAFM.py -f -o results.txt 012345678```
creates the file `results.txt` which includes only the invalid data passed to the program.

##GUI
Just double click.... I think it's quite self-explanatory
You could also launch from console without any arguments.

At this point the GUI lacks of the various options the script has at console.

#TODO:
More like a list of thinks that come to my mind that could be done, not that will be done necessarily.
* alter the GUI to accept a list of values, accept files of data, export to files etc.
* maybe give an option to pass valid AFM's to web services like http://ec.europa.eu/taxation_customs/vies/vatRequest.html
* test in other platforms (Windows / MacOS)
* add support for other countries (longshot but I thought I should mention it)
