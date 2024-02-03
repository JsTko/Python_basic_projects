import random

difficulty = 15
max_roll = 100

def settings(): #Game settings

    while True:

        difficulty_options = {"easy" : 30, "normal" : 20, "hard" : 15, "impossible" : 10}
        max_range_options = {"easy" : 10, "normal" : 100, "hard" : 1000, "impossible" : 10000}
        settings_option = input("what you want to change? ")

        if settings_option == "difficulty":
            play = input("easy, normal, hard, impossible?")

            try:
                global difficulty
                difficulty = difficulty_options[play]
                print(difficulty)
                return difficulty
            except:
                print("INVALID VALUE!")
                continue
            
        elif settings_option == "range":
            play = input("easy, normal, hard, impossible?")
            
            try:
                global max_roll
                max_roll = max_range_options[play]
                print(max_roll)
                return max_roll
            except:
                print("INVALID!")
                continue
        else:
            break

def gen_num(num): #Random number generator]
    max_range = max_roll
    return num + random.randint(0, max_range)

def sum_score(): #Count score

    global total_score, total_correct, total_fails

    try:
        total_score += score
        total_fails += fails
        total_correct += correct
    except:
        total_score = 0
        total_fails = 0
        total_correct = 0
        total_score += score
        total_fails += fails
        total_correct += correct

    print("NICE GAME! you got:")
    print(f"You made ", total_score, " guesses")
    print(f"you were correct ", total_correct, " times")
    print(f"You lose ", total_fails, "times")

    return total_score, total_correct, total_fails

def game(): #Game works
    
    global correct, fails, score
    number = gen_num(0)
    round_score = 0
    score = 0
    correct = 0
    fails = 0

    while True:
        
        print(f"", round_score, "/", difficulty)
        #print(number) #only for tests
        guess = input("whats your guess? ")

        try:
            guess = int(guess)
        except:
            print("USE ONLY NUMBERS!!!")
            continue

        if round_score >= difficulty:
            fails += 1
            score += round_score
            round_score = 0
            print("YOU LOSE!!!")
            play = input("do you want to try again? ")
            if play == "yes":
                continue
            else:
                sum_score()
                break

        if guess > number:
            round_score += 1
            print("TO HIGH!")
            continue
        elif guess < number:
            round_score += 1
            print("TO LOW!")
            continue
        else:
            round_score += 1
            correct += 1
            score += round_score
            round_score = 0
            print("CORRECT!!!")
            number = gen_num(0)
            play = input("want play again?")

            if play != "yes":
                sum_score()
                break
        
while True: #Program works
    
    player_input = input("start, settings, quit: ")
    if player_input == "start":
        game()
    elif player_input == "settings":
        settings()
    else:
        break