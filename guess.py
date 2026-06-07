import random
number = random.randint(1, 20)
attempts = 6
while attempts > 0:
    guess = int(input("Guess a number (1-20): "))

    if guess == number:
        print("Correct 🎉 You win!")
        break
    else:
        attempts -= 1
        print("Wrong 😅 Remaining attempts:", attempts)

        if guess < number:
            print("Too low 📉")
        elif guess > number:
            print("Too high 📈")

if attempts == 0:
    print("Game over 💀 The number was:", number)
