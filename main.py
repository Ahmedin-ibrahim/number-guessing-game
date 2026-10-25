import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))

while guess != number:
    if guess < number:
        print("Hot")
    else:
        print("Cold")
    guess = int(input("Guess again: "))
else:
    print(f"\n🎉 Congratulations!")
    