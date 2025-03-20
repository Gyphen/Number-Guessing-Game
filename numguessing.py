import random
randnumber = random.randint(1, 100)

name =input("Name: ")
print(f"Welcome to my game {name}!")
print("I'm thinking of a number between 1 and 100")
print(f"Choose a difficulty.",)
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (1 chance)")
difficulty = int(input("Enter 1, 2, or 3: "))


class Guessing:
    def __init__(self, chances):
        self.chances = chances
        
        
    def guess(self):
        while self.chances > 0:
            guess = int(input("Enter your guess:"))
            if guess == randnumber:
                print("Congratulations! You guessed the number")
                break
            elif guess < randnumber:
                print("Your guess is less than the number")
                self.chances -= 1
                continue
            elif guess > randnumber:
                print("Your guess is greater than the number")
                self.chances -= 1
                continue
        if self.chances == 0:
            print("You have run out of chances. The number was", randnumber)
            

                
        
if difficulty == 1:
    print("Great you have chosen Easy, you have 10 chances to guess the number")
    Guessing(10).guess()
    
elif difficulty == 2:
    print("Great you have chosen Medium, you have 5 chances to guess the number")
    Guessing(5).guess()
    
elif difficulty == 3:
    print("Great you have chosen Hard, you have 1 chance to guess the number")
    Guessing(1).guess()

