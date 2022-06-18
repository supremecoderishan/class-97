import random
print ("Number geussing game")
number = random.randint(1,9)
chances= 0
print ("geuss a number (between 1 and 9)")
while chances < 5:

    geuss= int(input("Enter your geuss:-"))


    if geuss == number:
     print ("CONGRATULATION YOU WON")
     break 

    elif geuss < number: 
        print ("your number was too low, geuss higher than", geuss) 

    else: 

        print ("your number was too high, geuss higher lower", geuss)

    chances += 1

if not chances < 5:
    print("YOU LOOSE THE NUMBER IS", number)
