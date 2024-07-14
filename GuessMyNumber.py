import random
rd=random.randint(1,10)
count=0
print("--------------Guessing Game--------------")
while True:
    count=count+1
    guess=int(input("Enter the guess number:"))
    if guess==rd:
        print("Correct!!!")
        break
    elif guess>rd:
        print("Guess is higher")
    else:
        print("Guess is lower")

print("Number of attempts it took to win the game is:",count)