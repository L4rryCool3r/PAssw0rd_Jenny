#!/usr/bin/python


''
    NAME : 2nd  PYTHON
    DATE : 11 - 08 - 2019
    AUTHOR : SinBad
'''   
import string
from random import *
print("****   My first Python Code   ****\n\n\n")
print("     -- Generate password --\n")
chars = string.ascii_letters + string.digits + string.punctuation

def createPassword():
    lenght = randint(10, 20)
    while True:
        password =  ""
        nbrLettersLower = 0
        nbrLettersUpper = 0
        nbrDigits = 0
        nbrPunc = 0
        for x in range(lenght) :
            newChar = choice(chars)
            password += newChar
            if newChar in string.ascii_letters :
                if newChar == newChar.lower() :
                    nbrLettersLower+=1
                elif newChar == newChar.upper() :
                    nbrLettersUpper+=1   
            if newChar in string.digits :
                nbrDigits+=1
            if newChar in string.punctuation :
                nbrPunc+=1
        if nbrLettersLower>0 and nbrLettersUpper>0 and nbrDigits>0 and nbrPunc>0 :
            break
    if  nbrLettersLower<10: nbrLettersLower="0"+str(nbrLettersLower)
    if  nbrLettersUpper<10: nbrLettersUpper="0"+str(nbrLettersUpper)
    if  nbrDigits<10: nbrDigits="0"+str(nbrDigits)
    if  nbrPunc<10: nbrPunc="0"+str(nbrPunc)
    print("       -Lenght:       " ,len(password))
    print("       -Letters lower:" ,nbrLettersLower )
    print("       -Letters upper:" ,nbrLettersUpper )
    print("       -Digits:       " ,nbrDigits)
    print("       -Punctuation:  " ,nbrPunc,"\n")
    print("Your Password -->  " ,password)
   
createPassword()


print "give me a bottle of rum!"
