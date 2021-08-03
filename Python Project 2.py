import random

i = 1 #iterator
g = None

print(" ")
print("Guess the number game")
print(" ")

while True:
    num = random.randint(1, 10)
    
    while i <= 5:

        g = input("Try: ")
        if g == num:
            print("Yay correct guess!")
            print("You won the game!")
            i = 6
            break

        else:
            print("Better Luck next Time!")
            i += 1


    if i >= 5 and g != num:
        print("You Lost!")

    

    print("Thanks for plaing!")
    input("Enter any key to exit. ")  
    break 