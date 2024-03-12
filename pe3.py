import random

def main():
    n = random.randint(1, 100)
    print("A random number has been generated between 1 and 100. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess == n:
                print("EXACTLY! You guessed the correct number.")
                break
            elif guess < n:
                print("The number is greater than", guess)
            else:
                print("The number is less than", guess)
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
