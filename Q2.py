import random

class Main:
    def GuessNumber(self, number):
        a = 1
        b = int(number)
        state = ''
        while (state != 'c'):
            comp = random.randint(a,b)
            state = input('Is' + str(comp) +'too high(h), too low(l), or correct(c):')
            if(state == 'h'): b = comp -1
            elif(state == 'l'): b = comp +1
        print('Well done, the computer guessed the correct number' + str(comp) + 'correctly')
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()
        
        