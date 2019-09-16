number = int(input("Enter Number"))
guess = 2.00

def findSquareRoot(number, guess):
    if (abs(number - (guess * guess)) < 0.0005):
        print("Square root of : "+str(number)+" is : " + str(guess))
    else:
        guess = (number / guess + guess) / 2
        print("New Guess is : "+ str(guess))
        findSquareRoot(number, guess)

if __name__ == '__main__':
    findSquareRoot(number, guess)