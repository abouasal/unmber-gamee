import random
while True:
    number = random.randint(1,100)
    tries = 0
    is_winner = False
    while tries < 5:
        try:
           my_guess = int(input(" Enter your guess between 1 and 100: "))
        except ValueError:
            print("Invalid input!Please enter numbers only.")
            continue
        if my_guess < 1 or my_guess > 100:
            print("Out of range! Number must be betwween 1 and 100")
            continue
        tries += 1
        diff = abs (number - my_guess)
        print("Current attempt:", tries)
        print("Chances remaining:", 5-tries)
        if my_guess == number:
            print("You guessed it right! Victory!")
            is_winner = True
            break
        elif my_guess < number:
            print("Hint:Try a higher number.")
        else:
            print("Hint: Try a lower number.")
        if diff <= 5:
            print("Status:Extremely close!")
        elif diff <= 15:
            print("Status: Getting closer,but not quite there")
        else:
            print("Status: Too far away!")
        if is_winner:
            if tries == 1:
                print("Performance Grade: Exceptional")
            elif tries == 2:
                print("Performance Grade: Very Good")                                
            elif tries == 3:
                print("Performance Grade:Good")
            elif tries == 4:
                print("Performance Grade:Fair")
            elif tries == 5:
                print("Performance Grade:Lucky")  
        else:
            print("Game Over! You ran out of chances")
            print("The hidden number was:",number)
        restart_choice = input("Would you like to play another round?(yes/no):").strip().lower()
        if restart_choice not in ['yes','y']:
            print("Thanks for playing, bye!")
            break                  

