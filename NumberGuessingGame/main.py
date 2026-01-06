import random
def guess():
    r_num:int = random.randrange(1,11)
    attempts:int = 0
    while True:
        user_guess = input("guess the number between 1 and 10: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("enter a number next time")
            continue
        if(user_guess > 10 or user_guess < 1):
            print("Guess must be between 1 and 10")
            continue
        if(user_guess == r_num):
            attempts += 1
            print(f"you guessed the number in {attempts} attempts")
            break
        elif(user_guess < r_num):
            attempts += 1
            print("guess a little higher")
        else:
            attempts += 1
            print("guess a little lower")
guess()
    