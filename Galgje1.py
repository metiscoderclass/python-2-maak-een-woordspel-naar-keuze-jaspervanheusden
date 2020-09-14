import random
import time  
randnumber = random.randint(1, 3)

word = "kaas"
if randnumber == 1:
    word = "bord"

if randnumber == 2:
    word = "pein"

if randnumber == 3:
    word = "zout"
#er is hier ruimte om meer woorden toe te voegen
letterscore = len(word)
turns = 8
fouten = 5
dupletter = 0
letteramt = len(word)
win = 0
letter1 = "*"
letter2 = "*"
letter3 = "*"
letter4 = "*"

print("Dit spel is gemaakt als cadeau voor GERARD GEFELICITEERT")
name = input("Hoe heet jij? ")
print("Hallo, " + name + " Welkom bij Galgje, je doel is om de letters in het woord te raden, je hebt 8 beurten om de juiste letter te raden.")

time.sleep(1)




print("elk stipje is 1 letter")
for _ in range(8):
    
    print(letter1 + letter2 + letter3 + letter4)
    letter = input("welke leter(s) kies je? ")
    if letter == word:
        print("Wow! dat is het hele woord!")
        time.sleep(5)
        win = 2
        while win == 2:
            exit
    if letter == letter1:
            print("Je kan niet 2 keer dezelfde letter kiezen") 
            letterscore += 1
            fouten -= 1
            dupletter += 1
    if letter == letter2:
            print("Je kan niet 2 keer dezelfde letter")
            letterscore += 1
            fouten -= 1
            dupletter += 1
    if letter == letter3:
            print("Je kan niet 2 keer dezelfde letter") 
            letterscore += 1
            fouten -= 1
            dupletter += 1
    if letter == letter4:
            print("Je kan niet 2 keer dezelfde letter") 
            letterscore += 1
            fouten -= 1
            dupletter += 1
    if letter in word:
        if dupletter == 0:
            print("De letter " + letter + " zit in het woord!")
            letterscore -= 1
            letternumber = word.index(letter)
            letternumber = letternumber + 1
            if letternumber == 1:
                letter1 = letter
            if letternumber == 2:
                letter2 = letter
            if letternumber == 3:
                letter3 = letter
            if letternumber == 4:
                letter4 = letter

        

        
    elif letter not in word:
        if dupletter == 0:
            print("Oops! die letter zit niet in het woord!")
            fouten -= 1
    if letterscore == 0:
       print("je hebt gewonnen! het woord was " + word)
       win = 1
       
    while win == 1:
        exit
    time.sleep(1)
    
    dupletter == 0
    turns -= 1
    if turns == 0:
        print("Helaas! Je hebt verloren, het woord was " + word)
        time.sleep(10)
        exit
    




