# Ελληνικά
(scroll down for English)

## check AFM
Είναι ένα απλό script με γραφικό περιβάλλον (tkinter) που ελέγχει την εγκυρότητα ενός Α.Φ.Μ. βάση του ψηφίου ελέγχου.

Μπορείτε να κάνετε import το checkAFM και να χρησιμοποιήσετε την συνάρτηση check_afm() στο δικό σας script, τόσο σε Python 2 (δοκιμάσθηκε με την έκδοση 2.7.6), όσο και σε Python 3 (δοκιμάσθηκε με την έκδοση 3.4.0). Για να το εκτελέσετε ωστόσο, από κονσόλα ή γραφικό περιβάλλον, απαιτείτε Python 3.

Αναγνωρίζει την διεθνή απόδοση των Α.Φ.Μ. (με το πρόθεμα `EL`).

Στην παρούσα φάση, ειδικά το γραφικό περιβάλλον είναι μόνο στα Ελληνικά.

Το αρχείο checkAFM.py μπορείτε:

1. Να το τρέξετε σε γραφικό περιβάλλον (διπλό κλικ ή από κονσόλα χωρίς καμία παράμετρο) (απαιτείται Python 3)
  * Για να ελέγξετε μεμονομένα Α.Φ.Μ. πληκτρολογώντας τα.
  * Για να υποβάλετε ένα αρχείο κειμένου με Α.Φ.Μ. (ένα ανά γραμμή) που θέλετε να ελέγξετε.

2. Να το τρέξετε από κονσόλα (απαιτείται Python 3)
  * Για να ελέγξετε ένα σχετικά περιορισμένο αριθμό Α.Φ.Μ.
  * Για να ελέγξετε οποιοδήποτε όγκο δεδομένων από αρχείο κειμένου.
  * Το αποτέλεσμα μπορείτε να το πάρετε είτε στην κονσόλα, είτε σε αρχείο κειμένου.

3. Να το εισάγετε στο δικό σας script και να χρησιμοποιήσετε την συνάρτηση check_afm()
  * Σε Python 2
    ```from checkAFM import check_afm
    print check_afm("123456789")```
  * Σε Python 3
    ```from checkAFM import check_afm
    print( check_afm("123456789") )```

  Παρακαλώ σημειώστε πως τα δεδομένα στην συνάρτηση θα πρέπει να βεβαιωθείτε πως τα δίνετε ως string και όχι ως integers!

Έχει δοκιμασθεί με αρχείο που περιείχε περισσότερα από 8000 Α.Φ.Μ., χωρίς να παρουσιασθεί οποιοδήποτε πρόβλημα.

## Οδηγίες χρήσης

### Από κονσόλα

* `checkAFM.py` ακολουθούμενο από οσαδήποτε Α.Φ.Μ. θέλετε να ελέγξετε, χωρισμένα απλά με ένα κενό χαρακτήρα (space)
* `checkAFM.py -i ΑΡΧΕΙΟ` για να διαβάσει τα δεδομένα από ένα από αρχείο κειμένου. Ελέγχει ολόκληρες τις γραμμές του αρχείου, οπότε βεβαιωθείτε πως περιέχει ένα Α.Φ.Μ. ανά γραμμή.
* `checkAFM.py -o ΑΡΧΕΙΟ` για να ανακατευθύνετε τα αποτελέσματα σε αρχείο κειμένου.
* με την παράμετρο `-t` μπορείτε να περιορίσετε τις επιστρεφόμενες τιμές μόνο στα έγκυρα Α.Φ.Μ.
* με την παράμετρο `-f` μπορείτε να περιορίσετε τις επιστρεφόμενες τιμές μόνο στα άκυρα Α.Φ.Μ.
* με την παράμετρο `-s` μπορείτε να δείτε τους αριθμούς έγκυρων και άκυρων Α.Φ.Μ. που βρέθηκαν στα δεδομένα σας.

Σημειώστε πως οι παράμετροι `-t` και `-f` ακυρώνουν η μία την άλλη. Αν συμπεριλάβετε και τις δύο, μόνο η τελευταία θα εφαρμοσθεί.
Αν δεν συμπεριλάβετε καμία από τις δύο παραμέτρους, θα εξαχθεί μία λίστα των δεδομένων σας, ακολουθούμενη από τις τιμές `True` (για έγκυρα Α.Φ.Μ.) ή `False`.

* με την παράμετρο `-h` θα επιστραφεί μήνυμα με οδηγίες χρήσης και περιγραφή των παραμέτρων, ενώ με την παράμετρο `-v` θα επιστραφεί η έκδοση του script.

#### Παραδείγματα:
```
./checkAFM.py 012345678 123456789 234567890
```
ή
```
python3 checkAFM.py 012345678 123456789 234567890
```
επιστρέφουν στην οθόνη σας μία λίστα από τα δεδομένα ακολουθούμενα από την ένδειξη "True" ή "False".

```checkAFM.py -f -o results.txt 012345678 123456789```
δημιουργεί το αρχείο κειμένου results.txt που περιέχει μόνον όσες τιμές βρέθηκε πως ΔΕΝ είναι έγκυρα Α.Φ.Μ.

### Γραφικό περιβάλλον
Μπορείτε να το εκτελέσετε είτε με διπλό κλικ, είτε από κονσόλα χωρίς καμία παράμετρο.
Εκτός από την δαχτυλογράφηση κάθε Α.Φ.Μ. ξεχωριστά είναι δυνατή η ανάγνωση δεδομένων από αρχείο κειμένου (ένα Α.Φ.Μ. ανά γραμμή) και η εξαγωγή των αποτελεσμάτων σε αρχείο κειμένου επίσης.
Εφόσον σας εξυπηρετεί, μπορείτε να περιορίσετε τα εξαγώμενα δεδομένα είτε στις έγκυρες, είτε στις άκυρες τιμές.


# English
## check AFM
Simple python script with Tkinter interface to check the validity of an AFM (Greek VAT Identification Number), based on its check digit.

You can import this as a module and use check_afm() funtion in both Python 2 (tested with 2.7.6) and Python 3 (tested with 3.4.0), but you can only run it with Python 3, both in console and GUI.

It does recognise the international form of an AFM (prefixed with `EL`)

Unfortunately, the GUI at this point is in Greek language only.

It is one single file, that you can:

1. launch from your graphic enviroment (clickety-click) and use its Graphical User Interface (only with Python 3)
  * to check singularly afm's
  * to submit a text file with values (one per line) you want to check.

2. execute from terminal: (only with Python 3)
  * to check a small number of inputs
  * to check any number of data from a txt file
  * output can be either a file or the standar output (aka your screen)

3. import to use check_afm() function on your own script (works both with Python 2 and Python 3)
  * For Python 2
    ```from checkAFM import check_afm
    print check_afm("123456789")```
  * For Python 3
    ```from checkAFM import check_afm
    print ( check_afm("123456789") )```

  Please note that you should make sure to input the data as a string. NOT as an integer!


It has been tested against 8.000 valid AFM's without any hiccups.

##USAGE

###Command line
* `checkAFM.py` from command line followed by any number of AFM's you want to check, one after the other, space seperated.
* `checkAFM.py -i YOUR_FILE` to read data from a plain text file. It validates the whole line, so make sure the file has one AFM per line.
* `checkAFM.py -o FILE` to redirect output to a file.
* add `-t` to force the program return only data that are found to be valid AFM's.
* add `-f` to force the program return only data that are found to by invalid AFM's.
* add `-s` to include the number of valid and invalid AFM's at the end of the output.

Note that `-t` and `-f` are mutually exclusive. If you include both of them, only the last one will be applied.
If you ommit both of them, instead of a list of data, you'll get a tab seperated set of AFM's with either `True` or `False` next to it.

* `checkAFM.py -h` will return instructions for the syntax, while `checkAFM.py -v` will return it's version.


e.g.: 
```
./checkAFM.py 012345678 123456789 234567890
```
or
```
python3 checkAFM.py 012345678 123456789 234567890
```

Returns a tab seperated list of AFM's, followed by either "True" (=valid AFM) or "False".

```checkAFM.py -f -o results.txt 012345678```
creates the file `results.txt` which includes only the invalid data passed to the program.

###GUI
Just double click to launch (you could also launch from console without any arguments).
You can either type a single AFM to check, or select a text file with data you want to check (one per line) and where your results should be saved. You can limit the results to either valid or invalid ones if it suites you.


##TODO:
More like a list of thinks that come to my mind that could be done, not that will be done necessarily.
* yeah.... the GUI is quite ugly, I know...
* multilingual support for GUI (probably only bilingual, English and Greek)...
* maybe give an option to pass valid AFM's to web services like http://ec.europa.eu/taxation_customs/vies/vatRequest.html
* test in other platforms (Windows / MacOS), even though it should work as is. (please if you happen to do so, give me some feedback)