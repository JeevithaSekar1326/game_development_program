import random
def guess_the_number():
    print("WELCOME TO GUESS THE NUMBER!")
    print("I am thinking of a number between 1 to 100.Can you guess what it is?")
    target_number=random.randint(1,100)
    attempts=0
    while True:
        guess=int(input("Enter your guess"))
        attempts+=1
        if guess==target_number:
            print(f"Congratulations! You guessed the number{target_number}correctly in {attempts}attempts.")
            break
        elif guess<target_number:
            print("Too Low! Try guessing Higher.")
        else:
            print("Too High! Try guessing Lower.")
        if attempts==5:
            print(f"Sorry, You've reached the maximum number of attempts.The number was {target_number}.GAME OVER.")
            break
if_name=="_main_":
    guess_the_number()