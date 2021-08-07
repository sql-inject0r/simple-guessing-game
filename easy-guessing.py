# a very basic guessing game for begginers learning if and else statements !
import random
highest = 10
answer = random.randint(1,10)
print(answer) # TODO:remove after testing
guess = int(input("Please enter a number between 1 and {}: ".format(highest)))

while guess != answer:
    guess =int(input("enter a number between 1 and {}: ".format(highest)))
    if guess == answer:
        print("you got it :D")
        break
    else: # nested if else condition 
        if guess > answer:
            print("Please guess lower !")
        else:
            print("please guess higher !")
