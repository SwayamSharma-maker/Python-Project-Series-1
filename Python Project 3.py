import random

print(" ")
print("Rock, Paper, Scissors")

def whoWon (c, u):
    if c.lower() == u:
        print(f"Both players chose {c}. It's a tie!")

    elif u == 'r':
        if c == "S":
            print("Rock smashes scissors. You Win!")
        else:
            print("Paper covers rock. You lose!")

    elif u == 'p':
        if c == 'R':
            print("Paper covers rock. You win!")
        else:
            print("Scissors cut paper. You lose!")

    elif u == 's':
        if c == 'P':
            print("Scissors cut paper.You win!")
        else:
            print("Rock smashes scissors. You lose!")


while True:

    uAct = input("Enter a choice, Rock (r), Paper (p) or Scissors (s)? ")
    uAct = uAct.lower()

    PosCoAct = ['R', 'P', 'S']
    cAct = random.choice(PosCoAct)
    

    print(f"You chose {uAct} and the computer chose {cAct}. \n")

    whoWon(cAct, uAct)

    pAg = input("Do you want to play again (Y/N)? ")
    if pAg.lower() == "n":
        print("Thank you for playing!")
        break