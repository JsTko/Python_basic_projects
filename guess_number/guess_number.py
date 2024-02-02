import random

print("Wellcome in my simple guess the number")
status = True
guess_number = 0
total_guess_number = 0
total_number_found = 0
number = random.randint(0,1000)

while status == True:
    
    guess = input("Guess the number: ")

    if guess.isdigit == False:
        print("YOU NEED TO USE A DIGIT!!!")
        continue
    else: guess = int(guess)

    if guess > number:
        print("TO HIGH!")
        guess_number += 1
        continue
    elif guess < number:
        print("TO LOW!")
        guess_number += 1
        continue
    else:
        print("GOOD JOB! you do it in " + str(guess_number))
        decision = input("Do you want to continue?: ")
        if decision != "yes":
            status = False
            total_guess_number += guess_number
            total_number_found += 1
            break
        else:
            number = random.randint(0, 1000)
            print(guess_number)
            total_guess_number += guess_number
            total_number_found += 1
            guess_number = 0
            continue
print("Nice game you got: " + str(total_number_found) + " numbers")
print("And you don that in: " + str(total_guess_number) + " gueses")
