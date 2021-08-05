# a very basic guessing game for begginers learning if and else statements !
answer = 5

guess = int(input("Please enter a number between 1 and 10: "))

if guess != answer:
    if guess > answer:
        print("Please guess lower !")
    else:
        print("Please guess higher !")
    guess = int(input("Please enter a number between 1 and 10: "))
    if guess == answer:
        print("yay you have guessed it correctly :D")
    else:
        print("sorry you have not guessed it correctly :(")
else:
    print("YAY you got it first time :DDD")
