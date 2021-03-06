from tkinter import *

abc = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K',
    'l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w', 'W',
    'x','X','y', 'Y','z', 'Z']
ciph = "Here will be the output"

    ###########################
    # Functions for ciphering #
    ###########################

#Uses the Caesar cipher. It shifts the letters the times given.
def caesar ():
    result = Toplevel()
    result.title("Caesar")
    input = toCip.get()
    num = int(caesarN.get())
    ciphered = ""
    for letter in input:
        if letter in abc:
            ind = abc.index(letter)
            ciphered = ciphered + abc[(ind+(num*2) )%52]
        else:
            ciphered = ciphered + letter
    output = Label(result, text = ciphered)
    output.grid()

#The same function as Caesar but taking arguments, so it can be called from Vigenere
def caeHelp(input, num):
    ciphered = ""
    for letter in input:
        if letter in abc:
            ind = abc.index(letter)
            ciphered = ciphered + abc[(ind+(num*2) )%52]
        else:
            ciphered = ciphered + letter
    return ciphered

#Uses the Vigenere cipher. It uses a square table, which in essence is just applying Caesar a different number of times
#depending on the letter of the keyword being used at the moment.
def vigenere ():
    result = Toplevel()
    result.title("Vigenere")
    input = toCip.get()
    keyword = vigKey.get()
    ciphered = ""
    i = 0
    while i <len(input):
        for letter in input:
            if letter in abc:
                ciphered = ciphered + caeHelp(letter, round((abc.index(keyword[i%len(keyword)])/2)))
            else:
                ciphered = ciphered + letter
            i = i+1
    output = Label(result, text = ciphered)
    output.grid()

#Uses the frquencies of letters in English. Depending on it, it gives it a number. This uses Lewand's ordering.
def frequency():
    result = Toplevel()
    result.title("By frequency")
    input = toCip.get()
    #Order of the alphabet from most frequent to least frequent

    abcFreq = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z'
               'E','T','A','O','I','N','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z']
    ciphered = ""
    for letter in input:
        if letter in abcFreq:
            ciphered = ciphered + str((abcFreq.index(letter) %26)+1 + " ")
        else:
            ciphered = ciphered + letter
    output = Label(result, text = ciphered)
    output.grid()


#Uses the polialphabetical ordering. There are three alphabets (there could be more) and alternates them
def polialphabetical():
    result = Toplevel()
    result.title("Polialphabetical")
    input = toCip.get()
    ciphered = ""
    output = Label(result, text = ciphered)
    output.grid()



    ############################
    # Settings for the display #
    ############################

window = Tk()
window.title("Cipher")
window.geometry("500x300")

#Introductory message.
mPrinc = Message(window, text = "Hi! Fill in the necessary data and then choose the kind of ciphering you want! \n")
mPrinc.config(width = 200)
mPrinc.grid()

#Text to be ciphered
msg = Message(window, text = "Text to cipher ")
msg.config(width = 100)
msg.grid(sticky = "w")
toCip = Entry(window)
toCip.grid(sticky = "w", row = 1, column = 1)

#Necessary inputs for Caesar
msgC = Message(window, text = "Number (only Caesar) ")
msgC.grid(sticky = "w", row = 2, column = 0)
caesarN = Entry(window)
caesarN.grid(row = 2, column = 1)

#Necessary inputs for Vigenere
msgV = Message(window, text = "Key (only Vigenere) ")
msgV.grid(row = 3, sticky = "w")
vigKey = Entry(window)
vigKey.grid(row = 3, column = 1)

#Necessary inputs for polialphabetical
msgP = Message(window, text = "Order of alphabets (Polialphabetical only)")
msgP.grid(row = 4, sticky = "w")
order = Entry(window)
order.grid(row = 4, column = 1)

#Buttons for getting the ciphered text.
Button(window, text = "Caesar", command = caesar).grid(row = 7)
Button(window, text = "Vigenere", command = vigenere).grid(row = 7, column = 1)
Button(window, text = "Frequency", command = frequency).grid(row = 7, column = 2)
Button(window, text = "Polialphabetical", command = polialphabetical).grid(row = 8, column = 1)



window.mainloop()
