# snake water gun
import random

def gamewin(comp,player):
    if comp==player:
        return None 
    elif comp=='S':
        if player=='W':
            return False
        elif player=='G':
            return True
    elif comp=='W':
        if player=='G':
            return False
        elif player=='S':
            return True
    elif comp=='G':
        if player=='S':
            return False
        elif player=='W':
            return True

print("Computer's turn to choose form Snake(S), Water(W) and Gun(G) :)")
rand=random.randint(1,3)
if rand==1:
    comp='S'
elif rand==2:
    comp='W'
elif rand==3:
    comp='G'

player=input("Your turn to choose from Snake(S), Water(W) and Gun(G) =) ").upper()
print("Computer choosed:",comp)

'''a = gamewin(comp, player)
if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
else:
    print("Choose the correct option >[ ")
'''

if gamewin(comp,player)==None:
    print("Game is tie,Play again!!")
elif gamewin(comp,player)==False:
    print("You lose Computer Wins ;)")
else :#gamewin (comp,player)==True:
    print("You Win and Computer Loses:(")
