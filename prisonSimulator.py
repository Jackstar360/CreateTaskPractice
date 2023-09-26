
#The code below is meant to run a rudimentary simulation of a prison, with a small variety of different outcomes leading to a short but sweet experience with much chance for expansion and improvement.
#The game keeps track of days allowing for the illusion of time passing, a currency allowing for more variety in interactions and connectivity between events along with potential for more varied gameplay options. 
#It also combines a list of different events randomly put together and inputs that can even further impact the game based on the decisions.

#these are the imported modules needed for the code to run
import random
import time
import sys

#these are all of the Boolean Variables
play = True
death = False
sick = False
repUpdate = False
pre1 = False

#these are all of the Integer Variables
bank = 5
r = 5
currentTime = 1
bG = 0

#these are all of the lists and String Variables
events = ["requestedMoney", "blowBubbles"]
names = ["Tim", "Bob", "Sir Granferbrableharmfremdabble II", "Miles", "Brooke", "Lucas", "Ari", "Terrance", "Phillip", "Geofrery", "Hecter", "Walter", "Hank", "Jesse", "Jeff", "The Bulkans", "Steve", "Stabbin Mike", "Kenneth Pinyan", "Ted Kaczynski, Destroyer of Industrial Society", "Emmett", "Andrea"]
preEvents = ["overHearRiotPlan", "prisonerDrops$5", "fightCafeteria", "slipPuddle", "bumpGuard", "bumpPrisoner"]
lastEvent = "none"



#this is to create a typing effect
#this Function is called a lot of times because it is used in place of print so I'm not sure whether or not you wanted all of them labeled
def typewriter_effect(phrase):
    # Loop through each character in the sentence
    for char in phrase:

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

#this is for the animation of the title
def type_title_effect(phrase, extention):
    yhep = 0
    
    for char in phrase:

        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(0.8)

    for char in phrase:
        yhep += 1
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(0.08)
        if yhep == 2:
            break
    
    for char in extention:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(1)
    print()

#these are the variables for the typing animations and where the title Function is called
type_delay = 0.05
delete_delay = 0.01
type_title_effect("Cell ", "f Made")
print()
typewriter_effect("Made By: Jack Nelson and Brooke Boring.")
print()


#The first prompts, asks for a name and crime
name = input("What is your name: ")
print("Currently the only crime the game accepts is 'theft'")
crime = input("What is your crime: ").lower()


#The function that plays inbetween events to simulate passing time and updates the currentTime Variable
def dayCycle(timeCycle):
    print()
    print("\033[0;93m")
    typewriter_effect("""
----------------
  A day passes
----------------""")
    print()
    print("\033[0;37m")
    print()
    timeCycle += 1
    statCheck = input("Check your Stats? ").lower()
    if statCheck == "yes":
        print("\033[0;33m" + "Name: " + name)
        print("Crime: " + crime)
        print("Money: $" + str(bank))
        print("Day: " + str(timeCycle))
        print("Reputation: " + str(r) + "\033[0;37m")
        time.sleep(1)
        
    return int(timeCycle)
    
#Plays the random event that does not require input
def preEvent(pEvent):
    ranNumber = str(random.randrange(8, 32))
    global lastEvent
    global pre1
    global r
    global death
    global bank
    global bG
    global play
    if pEvent == "overHearRiotPlan" and lastEvent != pEvent:
        typewriter_effect("You overhear fellow prisoners discussing starting a riot")
        time.sleep(0.5)
        print()
    elif pEvent == "prisonerDrops$5" and lastEvent != pEvent:
        typewriter_effect("You see a fellow prisoner drop "), print("\033[0;32m" + "$5" + "\033[0;37m"), typewriter_effect("You decide to pick it up.")
        time.sleep(0.5)
        bank += 5
        print()
    elif pEvent == "fightCafeteria" and lastEvent != pEvent:
        typewriter_effect("You see a fight involving " + str(ranNumber) + " prisoners")
        ranNumber = str(round(int(ranNumber) / 4))
        ranNumber = (ranNumber)
        print()
        typewriter_effect(str(ranNumber) + " fellow prisoners were hurt")
        ranNumber = int(ranNumber)
        print()
        if ranNumber >= 7:
            ranNumber = round(int(ranNumber) / 1.5)
            ranNumber = str(ranNumber)
            typewriter_effect(str(ranNumber) + " fellow prisoners died")
            print()
        time.sleep(0.5)
    elif pEvent == "slipPuddle" and lastEvent != pEvent:
        typewriter_effect("You slip in a puddle and fall to the ground")
        print()
        time.sleep(0.5)
    elif pEvent == "bumpGuard" and lastEvent != pEvent:
        if bG == 3:
            typewriter_effect("You bump into a guard while walking, he decides enough is enough and attacks you")
            print()
            death = True
        else: 
            typewriter_effect("You bump into a guard while walking, he tells you not to do it again")
            print()
            r += 1
            bG += 1
            time.sleep(0.5)
    elif pEvent == "bumpPrisoner" and lastEvent != pEvent:
        typewriter_effect("You bump into " + random.choice(names) + ". They tell you not to do it again")
        print()
        r -= 1
        time.sleep(0.5)
    else:
        lastEvent = pEvent
        preEvent(random.choice(preEvents))

    
    if death == True:
        print("\033[0;31m")
        typewriter_effect("You Died!")
        print("\033[0;37m")
        play = False 
        
        
    lastEvent = pEvent
    return(bank)
    



#Plays the primary event that require input and displays an image
def randomEvent(event, money):
    eventPass = False
    global r
    global bank
    if death == False:
        preEvent(random.choice(preEvents))
        preEvent(random.choice(preEvents))
        if eventPass == False:
            #Prisoner asks for money
            if event == "requestedMoney":
                print()
                print(""" 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠞⠋⠉⠉⠙⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠈⠲⠤⠤⠔⠋⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠣⣴⣄⠀⠀⡄⠀⣠⣤⣼⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢼⡠⣤⣽⣷⡜⢱⣾⣯⣤⢄⠧⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⠡⡈⠘⠬⠟⠠⢸⠐⠭⠎⢡⠸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⢲⠃⠀⡜⡰⠁⠈⢰⢱⠀⠘⡖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⢠⠁⠈⣑⣒⣉⠀⠇⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠤⣾⡄⠔⠉⠔⠒⠢⠉⠂⣶⡖⠲⢤⡤⠤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣠⡤⢤⠔⠋⠁⠀⢸⣷⣤⣿⢵⡀⠀⠒⠓⡂⠀⢠⢻⡷⠶⣿⠁⠀⠀⠈⢻⡒⠶⢤⣀⠀⠀⠀
⣠⠴⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⢨⣷⣤⣿⢼⠉⠲⠤⠿⠗⠚⠁⣼⡷⠶⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦
⠀⠀⠀⠀⠀⠀⠀⠀⠦⡀⠀⠀⢸⣇⣀⣿⡜⠀⠀⡄⠀⠀⢀⣀⣾⣣⣤⣼⡇⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠢⣄⣀⣀⣀⣀⣀⣠⣽⢆⠀⣾⠉⠉⠉⢿⣍⡐⠀⠐⢈⣥⡾⠋⠉⠉⠈⣿⢠⠞⠒⠶⠦⠤⢤⣤⡤⠞⠀
⠀⠀⢠⠀⠉⠉⠁⠀⠀⠀⢈⣿⠿⠶⠶⢶⣶⣯⣿⣿⣿⣿⣿⡶⠶⠶⠾⠟⠻⣷⣀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⢸⠀⠀⠀⠀⠀⠀⢹⣿⣥⣀⣀⣀⣀⣀⣀⣀⢀⢀⣀⣀⣀⣀⣀⣀⣤⣤⣬⣿⠁⠀⠀⠀⠀⠀⣧⠀⠀
⡄⠀⢸⠀⠀⠀⠀⠀⠀⢸⡈⠉⠉⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⠉⠁⠀⡇⠀⠀⠀⠀⠀⠀⢻⠀⢀
⢱⠀⢸⠀⠀⠀⠀⠀⠀⠀⡷⢶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⡶⠶⠿⡇⠀⠀⠀⠀⠀⠀⢸⠀⣼
⠘⡇⠈⠒⢒⢆⠀⠀⠀⠀⣧⣀⣀⣀⣀⠀⠉⠉⠉⠉⠉⠉⠉⠁⢀⣀⣀⣀⣠⣴⠃⠀⠀⠀⢠⠖⠒⠃⠀⡇
⡼⠁⣀⣀⣤⠈⠳⡄⠀⠀⢹⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⢹⠀⠀⠀⡔⠋⢠⣇⣀⠀⠙
⠑⢦⡈⠙⠿⣤⣾⡁⠀⠀⢸⠶⣶⣦⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣴⣶⠶⠶⡿⠀⠀⠀⣹⡦⠼⠛⠁⣠⢊""")
                typewriter_effect(random.choice(names) + " asks you for "), print("\033[0;32m" + "$5" + "\033[0;37m")
                print()      
                choice = input("Yes or No: ").lower()
                if choice == "yes" and bank >= 5:
                    print("\033[0;92m")
                    typewriter_effect("They appreciate the gesture")
                    print("\033[0;37m")
                    print()
                    bank -= (5)
                    r += 1
                    eventPass = True
                elif choice == "yes":
                    print("\033[0;91m")
                    typewriter_effect("They smack you for lying")
                    print("\033[0;37m")
                    print()
                    r -= 1
                    eventPass = True
                if choice == "no":
                    print ("\033[0;91m")
                    typewriter_effect("They glare at you")
                    print("\033[0;37m")
                    print()
                    r -= 1
                    eventPass = True
            if event == "blowBubbles":
                print("""
⠀⠀⠀⠀⠀⠀⣴⠟⠛⠲⣄⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢸⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣀⠙⠶⠤⠴⠋⠀⠀⠀⠀⠀⠈⢷⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡜⠁⠉⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣈⡓⠢⣄⣀⣀⣠⢾⢡⡽⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⠶⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠞⠛⠛⠛⠛⠛⢿⡅⠀⠘⣎⠻⡎⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣣⣤⣤⣤⣀⣀⡀⢸⡇⠀⠀⠹⢿⡙⣾⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠁⣠⣿⡄⠀⣴⢦⡘⣿⢣⠀⠀⠀⠀⠙⠻⣮⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠉⢉⠁⣤⣃⣘⠃⠘⢮⡇⠀⠀⠀⠀⠀⠈⠳⣝⢦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠘⠛⠁⢈⡇⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠈⢿⢳⣤⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⢸⡛⠛⣻⡿⠁⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣧⡄
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣤⣀⠀⠀⠀⠀⠀⠀⢀⠟⠉⢻⣿⡿⠃
⠀⠀⠀⠀⠀⠀⣠⠞⠋⠙⠛⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣁⣈⣿⣳⣦⡀⠀⠀⢀⡞⠀⠀⡘⠀⠀⠀
⠀⠀⠀⠀⢀⡴⠿⣿⣷⡆⠀⠀⠀⠑⠦⣄⣀⡀⠀⢀⣀⡴⠞⠉⠛⠛⢿⣿⣷⣽⣦⢀⡾⠁⠀⢀⠃⠀⠀⠀
⠀⡰⠚⠉⠉⠛⠷⣶⣬⣧⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⢸⡇⠀⠀⣩⡟⠀⠀⠀⣸⠀⠀⠀⠀
⢸⠁⢀⡀⠀⢠⣄⣀⣹⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⣿⠀⠀⠀⢠⠇⠀⠀⠀⠀
⢸⠀⢾⣉⡇⠿⠬⣭⣿⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⡾⠹⡀⠀⢠⠏⠀⠀⠀⠀⠀
⠈⠳⠤⠟⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⠀⠀⢱⡶⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⢹⠀⡿⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⠀⠘⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
                typewriter_effect(random.choice(names) + " asks if you would like to blow bubbles with them")
                print()
                choice = input("Yes or No? ").lower()
                if choice == "yes":
                    typewriter_effect("You and your new friend blow bubbles until a gaurd tells you to cut it out")
                    r += 1
                print()
                if choice == "no":
                    typewriter_effect("They walk away disapointedly")

    eventPass = False
    
    return (money)





#The if statement that starts the game and prompts the player for their name and crime.
if crime == "theft":
    typewriter_effect("Hello " + name + ". Welcome to the breh Federal Prison")
    print("""
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠉⠁⠀⠀⠈⣉⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠡⠤⠤⠔⠒⠒⢉⣉⣀⣀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠠⠴⠖⠒⠛⠉⠉⠉⢀⣀⢤⣄⡀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⢀⡤⠴⠒⠦⠀⠀⠴⢋⡤⠒⢄⠙⡄⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⢀⡴⢋⡤⠖⢉⣉⣆⠀⢀⣞⣀⣀⣌⣧⠀⠀⣧⠖⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠁⣨⣶⣯⣵⣲⢿⠀⠈⡟⠻⠟⠚⠁⠀⠀⣷⡗⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⢒⡺⠀⠀⠀⠉⣩⠥⠀⢸⠀⠀⢷⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣌⣿⡀⠀⠀⠞⠁⠀⣤⢾⠀⠀⠈⣻⣹⠀⠀⠀⠀⣿⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⡿⡇⠀⠀⠀⠀⠀⠙⠛⠦⣄⡴⠃⠀⠐⠦⡀⠀⣿⠴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠵⣧⠀⠀⢰⢋⡀⠀⠀⠀⠀⢀⣠⡤⠞⠆⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠘⠉⠉⣭⣉⣉⣉⡴⠂⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⡀⠀⠀⠀⠀⡠⠤⠤⠤⣀⠀⢀⡼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠮⣧⡀⣤⡀⠀⠀⠀⣸⢓⡏⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡏⣻⠀⠀⠙⠦⣭⣓⣚⣫⠵⠋⠀⠀⣾⡉⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣎⣡⢿⣯⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⢈⣿⢧⣉⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⡿⠛⢻⣧⠀⢻⣷⡈⢳⣦⣀⠀⠀⠀⠀⢀⣤⣾⠏⣠⣿⠋⢀⣾⠟⠻⣷⣄⠀⠀⠀⠀⠀
⠀⠀⢠⠞⠙⣷⡄⠈⢿⣧⠀⠻⣷⡄⠹⣿⡍⠲⡶⠛⣽⡿⠃⣰⣿⠃⢀⣾⠏⠀⣰⡿⠉⢦⡀⠀⠀⠀
⠀⢠⢿⣆⠀⠘⣿⡄⠈⢿⣧⠀⠹⣿⡀⠘⣿⡀⡇⣸⡟⠀⣰⡿⠁⢀⣿⠏⠀⣼⡿⠁⢀⣾⢷⡀⠀⠀
⢀⡇⠈⢿⣆⠀⠹⣿⡄⠀⢻⣆⠀⢸⣧⠀⠈⠻⡿⠋⠀⢠⣿⠁⢀⣾⠏⠀⣰⡿⠁⢀⣾⡟⢠⠧⣄⡀""")
    typewriter_effect(random.choice(names) + " will be your cellmate")
    print()
    print("\033[0;93m")
    typewriter_effect("""
----------------
  A day passes
----------------""")
    print()
    print("\033[0;37m")
    print()

#The loop that calls events to happen and checks if the players Repuation has run out or if they have Died
while play == True:
    if death == True:
        print("\033[0;31m")
        typewriter_effect("You Died!")
        print("\033[0;37m")
        play = False
    if r <= 0:
        death = True
        typewriter_effect("You were jumped because no one liked you")
        print("\033[0;31m")
        typewriter_effect("You Died!")
        print("\033[0;37m")
        play = False
    if play == True:
        #Calling the events Function and Day Function
        randomEvent(random.choice(events), any)
        currentTime = dayCycle(currentTime)
    