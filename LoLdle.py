from colorama import *
from random import * 
from champs import champdict
guesscount = 0

answer = list(champdict.keys())[randint(0,len(list(champdict.keys()))-1)]
while True:
    a = []               
    guess = input("Guess a champion!: ").capitalize()
    guesscount+=1
    if guess in list(champdict.keys()):
        if guess == answer:
            break
        if champdict[guess]["Species"] == champdict[answer]["Species"]:
            print(Fore.GREEN + champdict[guess]["Species"] + Style.RESET_ALL)
        elif champdict[guess]["Species"] != champdict[answer]["Species"] and (champdict[answer]["Species"] in champdict[guess]["Species"] or champdict[guess]["Species"] in champdict[answer]["Species"]):
            print(Fore.YELLOW + champdict[guess]["Species"] + Style.RESET_ALL)
        elif champdict[guess]["Species"] != champdict[answer]["Species"]:
            print(Fore.RED + champdict[guess]["Species"] + Style.RESET_ALL)

        if champdict[guess]["Nation"] == champdict[answer]["Nation"]:
            print(Fore.GREEN + champdict[guess]["Nation"] + Style.RESET_ALL)
        elif champdict[guess]["Nation"] != champdict[answer]["Nation"] and (champdict[answer]["Nation"] in champdict[guess]["Nation"] or champdict[guess]["Nation"] in champdict[answer]["Nation"]):
            print(Fore.YELLOW + champdict[guess]["Nation"] + Style.RESET_ALL)
        elif champdict[guess]["Nation"] != champdict[answer]["Nation"]:
            print(Fore.RED + champdict[guess]["Nation"] + Style.RESET_ALL)

        if champdict[guess]["Position"] == champdict[answer]["Position"]:
            print(Fore.GREEN + champdict[guess]["Position"] + Style.RESET_ALL)
        elif champdict[guess]["Position"] != champdict[answer]["Position"] and (champdict[answer]["Position"] in champdict[guess]["Position"] or champdict[guess]["Position"] in champdict[answer]["Position"]):
            print(Fore.YELLOW + champdict[guess]["Position"] + Style.RESET_ALL)
        elif champdict[guess]["Position"] != champdict[answer]["Position"]:
            print(Fore.RED + champdict[guess]["Position"] + Style.RESET_ALL)

        if champdict[guess]["Resource"] == champdict[answer]["Resource"]:
            print(Fore.GREEN + champdict[guess]["Resource"] + Style.RESET_ALL)
        elif champdict[guess]["Resource"] != champdict[answer]["Resource"]:
            print(Fore.RED + champdict[guess]["Resource"] + Style.RESET_ALL)

        if champdict[guess]["Range"] == champdict[answer]["Range"]:
            print(Fore.GREEN + champdict[guess]["Range"] + Style.RESET_ALL)
        elif champdict[guess]["Range"] != champdict[answer]["Range"] and (champdict[answer]["Range"] in champdict[guess]["Range"] or champdict[guess]["Range"] in champdict[answer]["Range"]):
            print(Fore.YELLOW + champdict[guess]["Range"] + Style.RESET_ALL)
        elif champdict[guess]["Range"] != champdict[answer]["Range"]:
            print(Fore.RED + champdict[guess]["Range"] + Style.RESET_ALL)
    else: print("This champion is currently not in list.")

print("You found the champion!! It was " + answer +". You have found it in " + str(guesscount) + " tries.")