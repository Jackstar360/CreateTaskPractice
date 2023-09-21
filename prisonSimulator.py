import random

play = True
name = input("What is your name: ")
crime = input("What is your crime: ").lower()
death = False
events = ["requestedMoney"]
bank = int(5)
rep = 5
names = ["Tim", "Bob", "Sir Granferbrableharmfremdabble II", "Miles", "Brooke", "Lucas", "Ari", "Terrance", "Phillip", "Geofrery", "Hecter", "Walter", "Hank", "Jesse", "Jeff", "The Bulkans", "Steve", "Stabbin Mike", "Kenneth Pinyan", "Ted Kaczynski, Destroyer of Industrial Society", "Emmett", "Andrea"]
time = 5
sick = False
repUpdate = False

if crime == "theft":
    print ("Hello " + name + ". Welcome to the breh Federal Prison")
    print (random.choice(names) + " will be your cellmate")
    print()
    print()



def dayCycle(timeCycle):
    print()
    print()
    print("An hour passes")
    timeCycle += 1
    statCheck = input("Check your Stats? ").lower()
    if statCheck == "yes":
        print("\033[0;33m" + "Name: " + name)
        print("Crime: " + crime)
        print("Money: $" + str(bank))
        print("Time: " + str(timeCycle) + "\033[0;37m")   
        
    return int(timeCycle)
    


def randomEvent(event, money, rep1):
    if 
    eventPass = False
    if death == False and time <= 20:
        if eventPass == False:
            #Prisoner asks for money
            if event == "requestedMoney":
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
                print ("A fellow prisoner asks you for " + "\033[0;32m" + "$5" + "\033[0;37m")      
                choice = input("Yes or No: ")
                if choice == "yes" and money >= 5:
                    print("\033[0;92m" + "He appreciates the gesture" + "\033[0;37m")
                    money -= 5
                    rep1 += 1
                    eventPass = True
                elif choice == "yes" and money <= 5:
                    print("\033[0;91m" + "He smacks you for lying" + "\033[0;37m")
                    rep1 -= 1
                    eventPass = True
                elif choice == "no":
                    print ("\033[0;91m" + "He glares at you" + "\033[0;37m")
                    rep1 -= 1
                    eventPass = True

    eventPass = False
    return (event, money, rep1)



repUpdate = True
rep = randomEvent(any, any, rep)



while play == True:
    if rep <= 0:
        death = True
        print("You were jumped because no one liked you")
        print("\033[0;31m" + "You Died!" + "\033[0;37m")
        break
    randomEvent(random.choice(events), int(bank), any)
    time = dayCycle(time)