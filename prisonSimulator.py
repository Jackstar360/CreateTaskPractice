
#The code below is meant to run a rudimentary simulation of a prison, with a small variety of different outcomes leading to a short but sweet experience with much chance for expansion and improvement.
#The game keeps track of days allowing for the illusion of time passing, a currency allowing for more variety in interactions and connectivity between events along with potential for more varied gameplay options. 
#It also combines a list of different events randomly put together and inputs that can even further impact the game based on the decisions.

#these are the imported modules needed for the code to run
import random
import time
import sys
import keyboard
import curses


#Text colors
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"
reset = "\033[0m"


#these are all of the Boolean Variables
play = True
death = False
sick = False
repUpdate = False
pre1 = False
specialWalk = False
gang = False
learnedMagic = True

#these are all of the Integer Variables
bank = 5
r = 3
currentTime = 1
bG = 0
karma = 5
health = 20


menu = ["Melee", "Items", "Magic", "Run"]
current_row = 0

def print_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠛⠉⠀⠀⠀⠀⠀⠈⠉⠓⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⢁⣤⣶⣾⣶⣿⣄⣴⣿⣮⣢⣢⡀⡈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢃⡤⠚⠉⠙⠛⠿⠿⠿⠿⠿⠛⠋⠉⠉⠙⢦⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡞⠀⡼⡂⠀⠴⠤⠤⠤⠤⠤⠔⠒⠂⣠⠢⠀⡷⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢣⠀⡊⠿⡄⣀⣚⣢⡄⡄⣒⣓⢈⡯⠈⠐⠄⣧⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡾⢊⣴⣶⣬⣂⠄⡆⠃⡏⢌⣐⣮⣶⣿⢿⣮⡸⣹⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣸⡇⠿⣯⣾⠹⡿⠿⣿⣧⣜⣿⣿⣟⢿⡹⡳⡟⠁⢷⢏⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢻⣻⡁⠀⠻⣽⢿⣿⣿⠽⠃⠀⢛⠻⢿⣭⣭⠖⠀⡀⣸⡾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⢷⡸⣦⣤⡶⠊⠀⣎⡃⠀⢘⣱⡀⠉⠳⣶⠿⢃⡟⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⢼⣷⡈⢏⡄⢀⡞⣩⣿⣿⣿⣅⡹⡄⢰⣠⢣⣾⡟⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣾⡧⣸⣿⣿⣿⣿⠿⠿⣿⣿⡀⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣽⣿⣿⣷⡟⠩⠬⢶⡶⢶⠲⠤⢹⣧⣿⡿⡧⡢⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣤⡔⡘⠹⡉⢹⠘⢿⣿⣿⠦⠴⠋⢰⡄⠙⠒⢚⣿⡿⠀⡇⠇⢸⢹⡉⠒⢄⠀⠀⠀⠀⠀⠀
⠀⣀⠴⠋⠀⣡⠎⠀⢱⡀⠱⡜⢰⠈⠻⣿⣷⣶⣶⣾⣿⣾⣾⡿⠋⠀⠀⡟⠀⡌⠀⢣⠀⠀⠙⢔⠂⢄⠀⠀
⠊⢀⠀⢀⠔⠁⠀⠀⠀⠱⡀⠘⢦⡆⠐⡾⣿⣿⣏⠉⣙⡿⣿⡡⡎⢀⠜⠀⡜⠀⠀⠀⢆⠀⠀⠈⠳⡀⠑⢦
⢀⢆⠔⠁⠀⠀⠀⠀⠀⠀⠈⠢⡀⠙⠢⣸⣌⠻⣒⠐⠐⡺⢋⣼⡴⠋⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠀
⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠄⡀⠉⠓⠾⠵⠮⠶⠛⠁⢀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠀⠤⠤⠄⠐⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
    
    for i, item in enumerate(menu):
        x = 10
        y = i + 1
        arrow = " 🡄" if i == current_row else ""
        stdscr.addstr(y, x, f"{item}{arrow}")
        

    stdscr.refresh()

def main(stdscr):
    global current_row  # Declare current_row as a global variable

    curses.curs_set(0)
    # Remove background color initialization.
    
    while True:
        print_menu(stdscr)

        key = stdscr.getch()
        

        if key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == 10:  # Enter key
            stdscr.clear()
            stdscr.addstr(10, 10, f"Selected: {menu[current_row]}")
            stdscr.refresh()
            #stdscr.getch()  # Wait for a key press to continue
            time.sleep(1)
            curses.endwin()

#these are all of the lists and String Variables
events = ["requestedMoney", "blowBubbles", "phoneCall", "sonMail", "spoonEscape", "yardBored", "medical"]
names = ["Tim", "Bob", "Sir Granferbrableharmfremdabble II", "Miles", "Brooke", "Lucas", "Ari", "Terrance", "Phillip", "Geofrery", "Hecter", "Walter", "Hank", "Jesse", "Jeff", "The Bulkans", "Steve", "Stabbin Mike", "Kenneth Pinyan", "Ted Kaczynski, Destroyer of Industrial Society", "Emmett", "Andrea"]
preEvents = ["overHearRiotPlan", "prisonerDrops$5", "fightCafeteria", "slipPuddle", "bumpGuard", "bumpPrisoner", "nap", "sneeze"]
colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]
gangs = ["theGenerallyMeanSpiritedCoagulationOfPals", "crochetClub", "angryFellas", "theDeathGang", "isis", "theMickeyMouseClubHouse", "teddyBearTerrors", "spookyPumpkinGang", "theCult"]
items = {
    "Stick":0,
    "Spoon":0,
    "Keycard":0,
    "Baton":0,
    "Hand Gun":0,
    "Flower":0,
    "Small Rock":0
}
magic = {
    "Unholy Spark":0,
    "Hellfire":0,
    "Eldritch Manus":0
}
lastPEvent = "none"
lastEvent = "none"
siblingTalked = 0
cellMate = (random.choice(names))


def randomColor(output):
    output = random.choice(colors)
    if output == "red":
        output = red
    elif output == "green":
        output = green
    elif output == "blue":
        output = blue
    elif output == "yellow":
        output = blue
    elif output == "magenta":
        output = magenta
    elif output == "cyan":
        output = cyan
    return(output)


def name_effect(phrase1, name, phrase2):
    for char in phrase1:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    for char in name:
        
        print(f"{randomColor(any)}{char}{reset}", end='', flush=True)
        time.sleep(0.05)

    for char in phrase2:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()



#this is to create a typing effect
#this Function is called a lot of times because it is used in place of print so I'm not sure whether or not you wanted all of them labeled
def typewriter_effect(phrase, color):
    # Loop through each character in the sentence
    for char in phrase:
        
        print(f"{color}{char}", end='', flush=True)
        time.sleep(0.05)
    print(reset)


def typewriter_effect2(phrase1, phrase2, color):
    for char in phrase1:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    for char in phrase2:
        print(f"{color}{char}{reset}", end='', flush=True)
        time.sleep(0.05)
    

#Makes the middle of a sentence colored
def typewriter_effect3(phrase1, phrase2, phrase3, color):
    for char in phrase1:
        print(char, end='', flush=True)
        time.sleep(0.05)
    
    for char in phrase2:
        print(f"{color}{char}", end='', flush=True)
        time.sleep(0.05)
    
    for char in phrase3:
        print(f"{reset}{char}", end='', flush=True)
        time.sleep(0.05)
        
#sys.stdout.write(char)
#sys.stdout.flush()
#time.sleep(0.05)

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
typewriter_effect("Made By: Jack Nelson and Brooke Boring.", white)
print()


#The first prompts, asks for a name and crime
while True:
    name = input("What is your name: ")
    name_effect("So your name is ", name, "?")
    first = input("Yes or No? ").lower()
    if first == "yes":
        break
print("Currently the only crime the game accepts is 'theft'")
crime = input("What is your crime: ").lower()

motherConversations = ["You and your mother talk about your day and she wishes you well", "You and your mother argue over your incarceration until you run out of time", "She doesnt pick up"]
fatherConversations = ["You and your father discuss the time you committed " + crime, "Your father argues with you about having got caught", "He doesnt pick up"]
siblingConversation = ["You and your sibling laugh about " + crime, "You and your sibling fight about you being in prison", "They dont pick up"]


#The function that plays inbetween events to simulate passing time and updates the currentTime Variable
def dayCycle(timeCycle):
    global health
    if health >= 20:
        health = 20
    print()
    typewriter_effect("""
----------------
  A day passes
----------------""", bright_yellow)
    print()
    timeCycle += 1
    statCheck = input("Check your Stats? ").lower()
    if statCheck == "yes":
        print(yellow + "Name: " + name)
        print("Crime: " + crime)
        print("Health: " + str(health))
        print("Money: $" + str(bank))
        print("Day: " + str(timeCycle))
        print("Reputation: " + str(r))
        if sick == False:
            print("You are not sick" + reset)
        else:
            print("You are sick" + reset)
        time.sleep(1)
        
    return int(timeCycle)


def on_key_event(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'space':
        print("""
Melee
Items🡄
Magic
Run
""")



    
#Plays the random event that does not require input
def preEvent(pEvent):
    ranNumber = str(random.randrange(8, 32))
    global lastPEvent
    global pre1
    global r
    global death
    global bank
    global bG
    global play
    global currentTime
    global health

    if health <= 0:
        death = True

    if pEvent == "overHearRiotPlan" and lastPEvent != pEvent and death == False:
        typewriter_effect("You overhear fellow prisoners discussing starting a riot", reset)

        print()
    elif pEvent == "prisonerDrops$5" and lastPEvent != pEvent and death == False:
        typewriter_effect3("You see a fellow prisoner drop ", "$5. ", "You decide to pick it up.", green)

        bank += 5
        print()
    elif pEvent == "fightCafeteria" and lastPEvent != pEvent and death == False:
        typewriter_effect("You see a fight involving " + str(ranNumber) + " prisoners", reset)
        ranNumber = str(round(int(ranNumber) / 4))
        ranNumber = (ranNumber)
        print()
        typewriter_effect(str(ranNumber) + " fellow prisoners were hurt", reset)
        ranNumber = int(ranNumber)
        print()
        if ranNumber >= 7:
            ranNumber = round(int(ranNumber) / 1.5)
            ranNumber = str(ranNumber)
            typewriter_effect(str(ranNumber) + " fellow prisoners died", red)
            print()
    elif pEvent == "slipPuddle" and lastPEvent != pEvent and death == False:
        typewriter_effect("You slip in a puddle and fall to the ground", reset)
        health -= 1
        print()
    elif pEvent == "bumpGuard" and lastPEvent != pEvent and death == False:
        if bG >= 3 and r < 8:
            typewriter_effect("You bump into a guard while walking, he decides enough is enough and attacks you", red)
            print()
            death = True
        else: 
            typewriter_effect("You bump into a guard while walking, he tells you not to do it again", reset)
            print()
            r += 1
            bG += 1
    elif pEvent == "bumpPrisoner" and lastPEvent != pEvent and death == False:
        typewriter_effect("You bump into " + random.choice(names) + ". They tell you not to do it again", reset)
        print()
        r -= 1
    elif pEvent == "nap" and lastPEvent != pEvent and death == False:
        typewriter_effect("You get tired and decide to take a nap", reset)
        print()
    elif pEvent == "sneeze" and lastPEvent != pEvent and death == False:
        if karma <= 4:
            typewriter_effect(random.choice(names) + " sneezes on you", reset)
            typewriter_effect2("You feel a bit ", "ill", cyan)
            sick = True
        else:
            typewriter_effect(random.choice(names) + " sneezes on you", reset)
    else:
        lastPEvent = pEvent
        preEvent(random.choice(preEvents))

    
    if death == True:
        typewriter_effect("You Died!", red)
        play = False 
        
    time.sleep(0.5)
    lastPEvent = pEvent
    return(bank)
    



#Plays the primary event that require input and displays an image
def randomEvent(event, money):
    eventPass = False
    
    global lastEvent
    global r
    global bank
    global siblingTalked
    global cellMate
    global death
    global health
    global karma
    global specialWalk
    global currentTime
    global sick

    #testing thing
    event = "shoved"

    if health <= 0:
        death = True

    if event == lastEvent:
        randomEvent(random.choice(events), any)

    if death == False:
        preEvent(random.choice(preEvents))
        preEvent(random.choice(preEvents))
    if death == False:
        while eventPass == False:
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
                typewriter_effect2(random.choice(names) + " asks you for ", "$5", green)
                print()      
                print("Money: " + str(bank))
                choice = input("Yes or No: ").lower()
                if choice == "yes" and bank >= 5:
                    typewriter_effect("They appreciate the gesture", bright_green)
                    print()
                    bank -= (5)
                    r += 1
                    eventPass = True
                elif choice == "yes":
                    typewriter_effect("They smack you for lying", bright_red)
                    print()
                    r -= 1
                    health -= 4
                    eventPass = True
                elif choice == "no":
                    typewriter_effect("They glare at you", reset)
                    print()
                    r -= 1
                    eventPass = True
                else:
                    print("error")
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
                typewriter_effect(random.choice(names) + " asks if you would like to blow bubbles with them", reset)
                print()
                choice = input("Yes or No? ").lower()
                if choice == "yes":
                    typewriter_effect("You and your new friend blow bubbles until a gaurd tells you to cut it out", bright_green)
                    karma += 1
                    print()
                    eventPass = True
                elif choice == "no" and karma >= 4:
                    typewriter_effect("They walk away disapointedly", reset)
                    karma -= 1
                    eventPass = True
                elif choice == "no" and karma < 4:
                    typewriter_effect("They didn't like your tone when you said that and slammed your head against a pole", bright_red)
                    health -= 5
                    r -= 1
                    eventPass = True
                else:
                    print("error")
            if event == "phoneCall":
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⢲⡞⠛⠛⠒⠒⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠿⣟⣂⣀⣤⣤⣀⣀⣉⡢⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣠⡶⠚⣿⣿⣿⣤⣤⣤⣾⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢱⣶⣿⣿⣿⣿⣿⡟⢻⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⡿⣿⠿⠛⠛⠛⠛⠀⠿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠸⣄⠀⠀⠀⠀⢠⡷⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⢉⠠⠀⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⣈⢀⣀⣤⡾⢻⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣺⡟⠛⠛⠋⠁⡸⠃⣷⣲⣤⣄⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡾⠟⡟⠁⢸⡗⠤⠤⡴⠊⠀⠀⡇⠉⠙⠻⣿⣷⢄⠀⠀
⢀⡀⠀⢀⡀⠀⠀⠀⠀⡼⢃⡄⠘⠛⣟⡁⢣⢨⠋⠀⣻⡟⠲⠃⠀⡀⣰⢝⣡⣈⠇⠀
⠘⢿⣿⣿⣮⣦⡀⠀⡼⣮⣜⣀⣀⠀⠈⠙⣾⡷⠚⢋⣍⠀⠀⢢⡀⣿⠏⢛⣿⣿⡿⠀
⠀⠀⡻⣻⣿⣿⣟⣦⠁⡿⠛⠙⠛⠒⠀⢠⠃⡁⢀⠚⠻⠶⠠⠤⣿⣏⡜⢿⣿⣿⢷⠀
⠀⠀⢳⡫⢵⣺⣿⣷⣳⠷⣖⡺⢖⣺⠀⢸⢠⡇⠸⢶⠶⣶⣦⢤⣿⡏⠀⠀⠉⠉⠸⡇
⠀⠀⠈⢶⣫⣿⣿⣿⣿⣫⡽⢀⡂⠈⠁⠚⠦⣧⠀⣨⠀⠀⢸⢀⣿⣀⣠⣤⣄⣀⠀⣇
⠀⠀⠀⠀⢳⠴⣿⠿⣿⣷⣻⣅⡂⠀⠀⠀⠸⢸⠀⠈⡎⢓⠒⠚⠛⠛⠿⣿⣿⣿⣿⡟
⠀⠀⠀⠀⠀⢦⣀⣠⣿⣿⡏⠉⠉⠛⠉⢱⣧⣼⠀⠀⡇⢸⠀⠀⠀⠀⠀⠈⠉⡟⠉⠀
⠀⠀⠀⠀⠀⠀⠙⠻⠿⠿⠃⠀⠀⠀⠀⢸⣿⣇⣀⣰⢁⣾⣶⣤⣤⣤⣤⣴⣾⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⢸⡌⠏⠙⠛⠻⠿⠿⠿⠿⠟⠛⠁⠀⠀⠀⠀
""")
                typewriter_effect("A gaurd offers to let you have a phone call", reset)
                print()
                choice = input("Yes or No? ").lower()
                if choice == "yes":
                    while play == True:
                        caller = input("Would you like to call Your Mother, Father, or Sibling? ").lower()
                        if caller == "mother":
                            motherSaid = (random.choice(motherConversations))
                            typewriter_effect(motherSaid, reset)
                            print()
                            if motherSaid == "You and your mother talk about your day and she wishes you well":
                                karma += 1
                            eventPass = True
                            break
                        elif caller == "father":
                            typewriter_effect(random.choice(fatherConversations), reset)
                            print()
                            eventPass = True
                            break
                        elif caller == "sibling":
                            if siblingTalked == 2:
                                typewriter_effect("You yell at your sibling for not pulling their weight again", reset)
                                print()
                                eventPass = True
                                siblingTalked += 1
                                break
                            else:
                                typewriter_effect(random.choice(siblingConversation), reset)
                                print()
                                eventPass = True
                                siblingTalked += 1
                                break
                        else:
                            print("error")
                elif choice == "no":
                    typewriter_effect("The guard shrugs and walks away", reset)
                else:
                    print("error")
            if event == ("sonMail"):
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠐⠚⣹⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠔⠒⠉⠁⠀⠀⠀⣠⠃⠈⢧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡠⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀
⢀⣀⡤⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀
⠈⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀
⠀⠘⡿⠶⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⢱⡀⠀⠀⠀
⠀⠀⣱⡀⠈⠉⠛⠛⢶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀
⠀⠈⡈⣗⠀⠀⠀⠀⠀⠀⠉⠻⠿⣶⣤⣄⣀⠀⠀⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀
⠀⠀⠀⢸⣆⠀⡀⠀⡀⣤⢦⠴⢄⠀⠈⢙⠿⣷⣶⣾⡿⠀⠉⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀
⠀⠀⠀⠁⢻⣱⡎⠶⠑⠉⠀⠀⠀⠁⠀⠎⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠑⠢⢄⠀⠀⠀⠀⠀⠈⢆⠀
⠀⠀⠀⠀⠌⣇⠀⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠄⡀⠀⠀⠸⡄
⠀⠀⠀⠀⠠⠸⡄⠄⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠤⡀⣳
⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⠤⣤⠶⠋
⠀⠀⠀⠀⠀⠈⠈⡏⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠴⠒⠚⠋⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⡄⠫⢠⠁⠀⠀⠀⠀⠀⢀⣠⣤⠶⠟⠋⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⢫⢠⠃⠀⣀⣠⡴⠶⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠼⣯⠾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
                typewriter_effect("You receive a letter from someone claiming to be your son, read it?", reset)
                print()
                choice = input("Yes or No? ").lower()
                if choice == "yes":
                    typewriter_effect("You read the letter: ", reset)
                    print()
                    eventPass = True
                    typewriter_effect(""" It's been a year daddy, I really really miss you. 
Mommy says you went to the store to get some milk. 
Anyways I'm failing all my classes and mommy hits me very frequently,
and she changed my name to tickle tipson.
Anyways daddy I forgive you for abusing me,
Please come back.
""", reset)
                    print()
                elif choice == "no":
                    typewriter_effect("You toss the letter into the trash and move on with your day.", reset)
                    print()
                    eventPass = True
                else:
                    print("error")
            if event == ("spoonEscape"):
                print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠔⠋⠉⠀⠈⡟⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠊⢉⠉⠀⠀⠀⠀⠀⢀⠇⠀⢸⣦⣠⣴⣮⣉⠉⠉⠙⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⡄⢠⠘⡆⠀⠀⠀⢀⣠⠚⠀⠀⢸⡇⢀⠾⢋⠻⢣⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠸⣨⣇⡧⠴⠒⠉⠉⠉⠀⠀⠀⣿⢸⣁⣾⠁⣠⢰⢷⠀⢠⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡾⠻⢭⡒⣄⢀⣏⡔⠁⠀⠀⠀⠀⠀⠀⠀⣸⣽⣿⢻⣯⢤⢙⣿⠞⡷⠋⠀⠀⠀⠀
⠐⣖⠤⣄⣀⣼⠃⠤⣠⣿⠞⢋⠎⠀⠀⠀⠀⠀⠀⠀⠀⣰⠘⣹⠈⠉⠉⠛⠁⠈⠓⠃⠀⠀⠀⠀⠀
⠀⠈⠳⣄⠙⡆⠀⠀⡿⠁⢠⠃⠀⠰⡄⠀⠀⠀⠀⠀⡔⢹⠟⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣯⢾⡰⣣⡇⢀⠃⠀⠤⣀⠘⢄⠀⠀⠀⡸⣰⣇⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠓⣷⢧⣹⢾⠤⢤⣀⣈⠑⢮⣳⡀⢸⡽⠋⢀⡤⠛⢢⣤⠤⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠇⡎⠀⢸⠀⠐⠒⠻⣝⢲⠭⠿⢾⣷⣄⣾⣀⣀⡼⢼⣀⢳⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡾⠀⡁⠀⠀⢧⢤⣔⠯⠒⠓⠋⠤⠤⠮⠄⠒⠒⠋⣉⠅⠉⠉⠉⠛⡟⠛⠒⠦⣄⡀⠀
⠀⠀⠀⠀⢠⠃⠀⠁⠀⠀⣀⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠓⠂⠉⠁⠀⣰⠃⠀⠀⠀⠈⠙⠂
⠀⠀⠀⠀⠈⠓⠦⣤⣴⡛⠫⢭⡒⠦⣄⢀⣀⣀⣤⠤⠔⡾⠟⠒⠚⠉⠁⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣾⢻⡷⡈⠉⠉⠈⠉⠙⣽⠀⠀⠀⠀⣠⠇⠀⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡏⡏⣿⣏⣰⡇⠀⣀⣀⡤⠖⠁⠀⠀⠀⢸⣷⣠⠤⣀⣀⣀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡇⡇⠈⣿⡟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠉⠙⢿⣯⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣰⢗⣃⡀⠳⠁⠀⠤⠤⣤⡤⠤⠤⠤⠤⠤⠼⠶⠒⣶⣤⠄⢼⣿⣿⣭⡽⣆⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠄⠉⠁⠀⠀⢠⣂⠭⠅⠀⠀⠠⠦⠤⠤⠤⠴⠶⣤⣤⡄⠈⠭⠄⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀
""")
                typewriter_effect("Your cellmate " + cellMate + " decides to start digging an escape tunnel under their bed with a plastic spoon", reset)
                print()
                choice = input("Help them, ignore them, or tell a guard? ").lower()
                if choice == ("help them"):
                    typewriter_effect("You and " + cellMate + " dig all day and night until you run out of spoons and give up", bright_green)
                    r += 1
                    eventPass = True
                elif choice == ("ignore them"):
                    typewriter_effect(cellMate + " digs all day until they give up from exhaustion", reset)
                    print()
                    eventPass = True
                elif choice == ("tell a guard"):
                    typewriter_effect("The guard beats " + cellMate + " senseless and drags them away", bright_red)
                    print()
                    r -= 2
                    cellMate = random.choice(names)
                    typewriter_effect(cellMate + " is your new cellMate", reset)
                    print()
                    eventPass = True
                else:
                    print("error")
            if event == "yardBored":
                print("""
⡀⣠⠤⠴⢶                                       ⢀
⣿⣧⣄⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿
⣿⣿⣿⣷⣄⡀⠀⠑⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣻⣿
⠙⢿⣿⣹⣿⣿⣦⣄⠀⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣻⣿⣿⠞
⠀⢸⡇⠉⠻⢿⣿⣿⣷⢾⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⠿⠛⠉⠀⠀
⠀⢸⡇⠀⠀⠀⠉⣿⠿⣿⣷⣾⣦⣀⣀⣀⣄⣄⣤⣤⣇⣤⣤⣤⣤⣤⣤⣼⣴⣾⣻⣿⠿⠛⠁⠀⠀⠀⠀⠀
⠀⢸⣇⡀⠀⠀⠀⣯⠀⠀⠙⠻⣿⣷⣄⣀⣀⣀⣀⣀⣇⣀⣀⣀⣀⣠⣾⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡇⠉⠙⡎⠀⣿⠀⡄⣀⠀⡇⠙⣿⠿⠿⠿⠿⠿⡿⠿⢿⠿⣿⡿⠉⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡷⠀⠀⡇⢀⣿⠀⡇⢸⠀⡇⣿⣿⠉⠉⠉⠉⠉⡏⠉⠉⠉⠉⠹⠀⢸⠀⠀⠀⠀⠀⣰⡀⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⡇⠀⣿⠀⠉⠉⠀⡇⠉⣿⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠁⢹⣀⣀⠀⠀⠀⢹⠃⠀⠀⠀⠀⠀
⠀⢸⣇⠀⠨⡗⠀⣿⠀⠀⣀⢠⣗⠊⠉⠀⡠⠊⠩⠋⠙⡉⠛⢍⠉⢓⣶⣿⣿⡼⡇⠀⠀⢸⡀⠀⠀⠀⠀⠀
⠀⢸⣿⠤⣔⠣⠤⠿⠌⠁⠀⠀⠀⢀⡴⠋⠀⢀⠃⠀⠀⠐⡀⠀⠑⢤⣀⠉⠉⠉⠉⠑⢒⣼⣆⠀⠀⠀⠀⠀
⠤⣾⣿⡉⠀⠀⠀⠀⠀⠀⠀⣀⠔⠉⠀⠀⢀⠎⠀⠀⠀⠀⠱⠀⠀⠀⠉⠣⣀⡀⠀⠀⠀⠉⠁⠈⠁⠐⠢⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠁⠀⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠈⠳⣤⡀⠀⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣴⠞⠁⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠈⠽⢧⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠙⢿⣢⡀⠀⠀⠀
⠀⠐⣀⡴⠯⠤⠤⠀⠀⠀⠀⠀⠀⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣦⣀⠀
⣦⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶
⢯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸
⠀⠈⠙⠒⠦⢤⢤⣤⣤⣤⣴⣥⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣬⣤⣤⣤⣤⠤⣤⣤⠖⠒⠋⠁
""")
                typewriter_effect("You are sitting outside in the yard bored", reset)
                choice = input("Work out, Play basketball, Walk around. ").lower()
                
                if choice == "work out":
                    if karma > 4:
                        typewriter_effect("You feel refreshed after lifting some weights", bright_green)
                        r += 1
                        eventPass = True
                    if karma <= 4:
                        typewriter_effect("You strain yourself using the weights", bright_red)
                        health -= 2
                        eventPass = True
                elif choice == "play basketball":
                    if r >= 6 and karma >= 7:
                        typewriter_effect("Your team wins the game", bright_green)
                        r += 1
                        eventPass = True
                    if r < 6:
                        typewriter_effect("No one else wants to play basketball with you", reset)
                        eventPass = True
                    if r >= 6 and karma < 6:
                        typewriter_effect("You scrape your knee and lose the game", bright_red)
                        health -= 1
                        r -= 1
                        eventPass = True
                elif choice == "walk around":
                    if karma >= 8 and specialWalk != True:
                        typewriter_effect("You take a relaxing stroll around the yard", bright_green)
                        print()
                        typewriter_effect2("While on your walk you find ", "$10", green)
                        money += 10
                        eventPass = True
                        specialWalk = True
                    else:
                        typewriter_effect("You take a relaxing stroll around the yard", bright_green)
                        eventPass == True
                else:
                    print("error")

            if event == "medical":
                if health >= 7:
                    print("""
⠀⠀⠀⠀⠀⠀⠀⣠⠤⣀⢤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣴⡶⠶⠿⠥⢼⣀⡽⣸⡤⠼⠿⢵⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣜⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡟⢻⠂⠒⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠈⢦⣎⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣹⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢳⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣮⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀
⠘⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣔⣽⠏⠉⠉⠙⣕⡄⠀
⠀⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣿⡕⠢⣤⣤⠔⣺⣸⡀
⠀⢸⢻⡀⠀⠀⠀⠀⠀⠀⣀⣴⡟⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠙⢺⡶⣾⣶⣾⠟⢻⡇
⠀⠘⡌⢿⠶⣢⣤⣤⡲⢿⡾⢋⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⣴⠳⣏⣉⣠⣴⠟⠀
⠀⠀⠹⡄⠳⠤⠤⠤⠖⣉⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⢸⠍⠉⠉⠀⠀⠀
⠀⠀⠀⠙⣦⠀⣤⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢀⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡇⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢃⡞⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⢁⠞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⡆⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⢋⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠱⡈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠚⣁⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢄⠙⠦⣀⡀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠤⠖⠊⣁⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
                    typewriter_effect("You wonder if you should get a checkup from a doctor", reset)
                    print()
                    choice = input("Yes or No? ").lower()
                    if choice == "yes" and r <= 2:
                        typewriter_effect("The nurses tells you it isn't worth their time", reset)
                        eventPass = True
                    elif choice == "yes" and sick == False:
                        typewriter_effect("The nurses look you over and conclude your doing fine", reset)
                        typewriter_effect("You feel healthier", bright_green)
                        health += 3
                        eventPass = True
                    elif choice == "yes" and sick == True:
                        typewriter_effect("The nurses look you over and send you to the sick ward for care", bright_red)
                        typewriter_effect("A few days pass while you are in the sick ward", bright_yellow)
                        currentTime += 2
                        health += 2
                        sick = False
                        randomEvent(random.choice(events), any)
                    elif choice == "no":
                        typewriter_effect("You decide your healthy enough", reset)
                        eventPass = True
                    else:
                        print("error")
                elif health < 7:
                    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⡽⠷⣽⣷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣷⡟⠉⠀⠀⠀⠀⠈⠻⣯⢷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣝⢠⣾⣶⣶⣳⣶⣾⣦⢹⣼⡃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⡏⡽⣘⣓⡟⠘⣝⣛⣹⢹⣻⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣬⢉⠝⠧⠤⠛⡍⠁⡼⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡬⠊⣙⢚⡉⠞⣽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣤⢴⣾⣿⠟⠢⣤⠤⡴⢺⡟⣿⡓⠦⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡴⠚⠋⠁⣠⢿⡏⢸⠈⠢⢧⣴⠔⢁⡇⢸⣿⡀⠀⠉⠻⣆⠀⠀⠀
⠀⠀⠀⣼⠃⡄⠀⣠⣯⣾⣁⢀⢇⡠⢿⣿⢧⡸⠀⣈⡇⣷⠀⠀⢀⢹⡄⠀⠀
⠀⠀⢰⡇⠸⣇⢰⣏⣀⣇⡼⠋⠘⡅⣼⣿⡄⠇⠘⡅⠀⢹⠀⢸⡸⠘⣇⠀⠀
⠀⠀⡾⠁⠀⢿⣿⠁⢸⡇⢿⣦⡀⠘⣿⣿⡟⠀⢀⡜⠀⢸⡆⢸⠇⠀⢹⡄⠀
⠀⢸⡇⠀⠀⠸⣧⠀⣸⠀⠘⡇⠙⠢⣹⣿⢁⡴⠋⠀⢀⡼⣧⡼⡠⠀⠘⣇⠀
⠀⡟⠀⠀⢶⢄⣿⣄⡟⠀⢀⡇⠀⠀⢈⣷⡋⠀⠀⣄⣈⣛⣋⢗⠇⢠⡀⢹⡆
⢸⡇⢸⣿⠭⠳⣷⡉⠛⠒⠋⠁⠀⠀⢸⠉⠀⠀⠀⡇⠀⡰⡱⣓⢭⡻⠏⠀⣷
⢸⠁⠈⠓⠯⡓⠨⠵⡤⠤⠤⠤⣀⣀⣸⣀⣀⣀⢰⣀⣰⡿⠵⠵⣟⠓⢖⠀⢸
⢸⡆⠀⠉⢉⠽⡶⢤⠃⠀⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠁⠀⠀⢸
⠈⣇⠀⠀⣠⠊⠀⣸⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼
""")
                    typewriter_effect("One of the prison doctors notices you limping and asks if you want to get checked out", reset)
                    print()
                    choice = input("Yes or No? ").lower()
                    if choice == "yes" and sick == False:
                        typewriter_effect("The doctor gives you a check up before concluding you need to spend a few days in medical care", bright_red)
                        typewriter_effect("Four days pass while you are in the sick ward", bright_yellow)
                        currentTime += 4
                        health += 6
                        eventPass = True
                    elif choice == "yes" and sick == True:
                        typewriter_effect("The doctors gives you a check up and immediatly sends you to a medical bed", bright_red)
                        typewriter_effect("A week pass while you are in the sick ward", bright_yellow)
                        currentTime += 7
                        health += 10
                        eventPass = True
                    elif choice == "no":
                        typewriter_effect("You slowly limp away from the doctor", reset)
                        eventPass = True
                    else:
                        print("error")
            if event == "gangRecruitment":
                if gang == False:
                    if r >= 7:
                        typewriter_effect(random.name(names) + " walks up to you and asks if you'd like to join their gang")
            if event == "shoved":
                typewriter_effect(random.choice(names) + " shoves you to the ground.", bright_red)
                choice = input("Fight, Call a guard, Run: ").lower()
                if choice == "fight" and learnedMagic == True:
                    if __name__ == "__main__":
                        curses.wrapper(main)

                        

            
    if health >= 20:
        health = 20
    lastEvent = event
    eventPass = False
    
    return (money)





#The if statement that starts the game and prompts the player for their name and crime.
if crime == "theft":
    typewriter_effect("Hello " + name + ". Welcome to the breh Federal Prison", reset)
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
    typewriter_effect(cellMate + " will be your cellmate", reset)
    print()
    typewriter_effect("""
----------------
  A day passes
----------------""", bright_yellow)
    print()
    print()

#The loop that calls events to happen and checks if the players Repuation has run out or if they have Died
while play == True:
    if health <= 0:
        death = True
    if death == True:
        typewriter_effect("You Died!", red)
        play = False
    if r <= 0:
        death = True
        typewriter_effect("You were jumped because no one liked you", bright_red)
        typewriter_effect("You Died!", red)
        play = False
    if play == True:
        #Calling the events Function and Day Function
        randomEvent(random.choice(events), any)
        currentTime = dayCycle(currentTime)
    