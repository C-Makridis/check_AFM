#!/usr/bin/env python
# -*- coding: utf-8 -*-

def checkAFM(AFM):
  """ Check the validity of an AFM number.
      This only checks if it is a valid AFM number, not if it is actually used.
      Input should be given as a string, a check is made, but under certain conditions, an exception whould be thrown with integers. (hint: leading zeros mean an octal system... there is no '8' or '9' in the octal system) """
  if not isinstance(AFM, str):
    raise TypeError( "checkAFM()", "You should apply this function only in strings  to avoid exceptions and errors! Aborting" )
  if len(AFM) == 11 and AFM[:2] == "EL":
    AFM=AFM[2:]
  if AFM.isdigit() == True and len(AFM) == 9: # simple initial check to see if the input has the sorrect length and is consisted by numbers
    i, sums = 256, 0
    for digit in AFM[:-1]:
      sums += int(digit) * i
      i /= 2
    checksum = sums % 11
    if AFM[-1] == str(checksum) or (checksum==10 and AFM[-1]=="0"):
      return True
  return False

#------------------------------------ just to check ------------------------------------
#try:
  #print checkAFM("116448977")
#except ValueError as err:
  #print err.args