secret_number = 7
guess_limit = 3
guess_number = 0

while guess_number < guess_limit:
    guess = int(input("guess :"))
    if guess == secret_number:
        print("Congratulations! You win.")
        break
    guess_number += 1
else:
    print("You lost!")
