#BY ROHAN SHIRKHEDKAR
import string
import random
from random import randrange
print("=========================")
print("     Cipher/Decipher")
print("=========================")
def isInt(s):
    #finds if number is an integer
    try: 
        int(s)
        return True
    except ValueError:
        return False
def parseKey(key):
    #Converts key to numbers, whatever it is
    try:
        key1 = []
        if not isInt(key):
            str(key)
            keyNum = 0
            for character in key:
                number = ord(character)
                key1.append(number)
                keyNum = keyNum + 1
            key1 = str(key1)
            key = key1.replace("[","").replace("]","").replace(", ","")
            key = int(key)/(keyNum*1000)
            return key
        else:
            key = int(key)
            return key
    except:
        print("Not Trying to Break the System now are we?")
def cypher():
    try:
        #Gets String to be ciphered and key
        rinput = input('Write Text to be Cyphered: ')
        key = parseKey(input("Key: ").lower())
        #Generates Random Number
        rnd = randrange(1, 100)
        output = []
        #loops as many times as they are characteres in the string
        for character in rinput:
            #converts letter to number and multiplies it by the random number
            number = ord(character) * rnd
            #adds the output to a list
            output.append(number)
        #At the end, adds the random number to the list after multiplying it by the key
        output.append(rnd*key)
        #prints the list
        print(output)
    except:
        print("Not Trying to Break the System now are we?")
def decypher():
    try:
        #Gets list and evaluates what type of string it is (Lets python recognise it as a list)
        dlist = eval(input('Text to be Decyphered:'))
        key = parseKey(input("Key: ").lower())
        #Gets random number and divides it by the key
        rnd = dlist[-1]
        rnd = rnd / key
        #Removes random number from list
        dlist.pop()
        #Declares Variable in which deciphered message will be stored in
        out = ""
        #Loops as many times as they are numbers in the list
        for number in dlist:
            #divides number by random number and gets rid of the decimal point
            vnum = number/rnd
            vnum = int(vnum)
            #Converts left over number to a letter (or symbol) and adds it to variable 'out'
            valf = chr(vnum)
            out = out + valf
        #Prints deciphered message
        print(out)
    except:
        print("Not Trying to Break the System now are we?")
def getMode():
    #This function figures out if the user wants to use the cipher or decipher or quit
    try:
        while True:
            query = input('Cipher or Decipher? ')
            Fl = query[0].lower()
            if query == '' or not Fl in ['c','d','q']:
                q = input('Do you want to quit? ')
                fu = q[0].lower()
                if q == '' or not fu in ['y','n','q']:
                    print("Go Die in a Hole")
                else:
                    if fu == 'y':
                        break
                    if fu == 'n':
                        print("Well then answer with 'cipher' or 'decipher'")
                    if fu == 'q':
                        break
            else:
                if Fl == 'c':
                    cypher()
                if Fl == 'd':
                    decypher()
                if Fl == 'q':
                    break
    except:
        print("Not Trying to Break the System now are we?")
        getMode()
#Now to actual code that runs on start
getMode() #runs the function that figures out what the user wants to do
