
def tictactoeboard():
    print("     |    |     ")
    print("     |    |     ")
    print("----------------")
    print("     |    |     ")
    print("     |    |     ")
    print("----------------")
    print("     |    |     ")
    print("     |    |     ")

def checkplacement():
    global x
    global continue1
    rightanswer = input("Was this the right spot? ")
    if (rightanswer == "yes") or (rightanswer == "Yes"):
        xtracker = []
        xtracker.append("top left")
        if x > 0:
            continue1 = True
    elif (rightanswer == "no") or (rightanswer == "No"):
            x += 1
            x -= 1
    return continue1
    

print("Let's play tic-tac-toe!")
print("There are 9 positions on the board. To put your 'x' and/or 'o', type the corresponding position (top right, bottom left, middle middle). Use lowercase only!")
yesno = input("Ready? ")
if (yesno == "yes") or (yesno == "Yes"):
    print("Let's start!")
if (yesno == "no") or (yesno == "No"):
    print("Game over")
    exit()

x = 1
tictactoeboard()

while x == 1:
    player1 = input("Where do you want to go?: ")
    if player1 == "top left":
        print("  \/ |    |     ")
        print("  /\ |    |     ")
        print("----------------")
        print("     |    |     ")
        print("     |    |     ")
        print("----------------")
        print("     |    |     ")
        print("     |    |     ")
        checkplacement()
        if continue1 == True:
            continue

    elif player1 == "top middle":
        print("     | \/ |     ")
        print("     | /\ |     ")
        print("----------------")
        print("     |    |     ")
        print("     |    |     ")
        print("----------------")
        print("     |    |     ")
        print("     |    |     ")
    
    #elif player1 == "top right":

