import os
import mymodule
import time
from mymodule import pswrd as isPasswordCorrect

os.system('pyinstaller --onefile ten_math_functions.py')
os.system('cls')




def timer(s):
        while s: 
                time.sleep(1)
                s -= 1


def main():     
        print("\nEnter (0) TO VIEW DESCRIPTION OF ALL THE FUNCTIONS\n")
        print("Enter (1) TO FIND FACTORIAL")
        print("Enter (2) TO CHECK PRIMES")
        print("Enter (3) TO CHECK IF A NUMBER IS EVEN OR ODD")
        print("Enter (4) TO PRINT REVERSE OF A NUMBER")
        print("Enter (5) TO CHECK IF A NUMBER IS PALINDROME")
        print("Enter (6) TO CHECK IF A NUMBER IS ARMSTRONG")
        print("Enter (7) TO CHECK DIVISIBILITY OF 2 NUMBERS")
        print("Enter (8) TO COUNT NUMBER OF DIGITS OF A NUMBER")
        print("Enter (9) TO FIND SUM OF DIGITS OF A NUMBER")
        print("Enter (10) TO PRINT DIGITS OF A NUMBER IN WORDS")

        print("\n------------\n")

        input1 = 0
        input2 = 0

        listSelector = input("\nEnter your selection (0-10 only): ")

        if listSelector == '0':
                mymodule.description()

                print("\n------------\n")

                cls = input("\nPress ENTER to clear the screen ")

                os.system('cls')
                main()
        elif listSelector == '1':
                print("You selected OPTION 1")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.factorial(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")

        elif listSelector == '2':
                print("You selected OPTION 2")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.isPrime(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")

        elif listSelector == '3':
                print("You selected OPTION 3")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.oddOrEven(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")

        elif listSelector == '4':
                print("You selected OPTION 4")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.reverse(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")

        elif listSelector == '5':
                print("You selected OPTION 5")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.isPalindrome(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")
                
        elif listSelector == '6':
                print("You selected OPTION 6")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.isArmstrong(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")
                
        elif listSelector == '7':
                print("You selected OPTION 7")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter the 1st number: "))
                        input2 = int(input("Enter the 2nd number: "))
                        mymodule.divisible(input1, input2)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")
                
        elif listSelector == '8':
                print("You selected OPTION 8")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.numOfDigits(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")
                
        elif listSelector == '9':
                print("You selected OPTION 9")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.sumOfDigits(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")
                
        elif listSelector == '10':
                print("You selected OPTION 10")

                print("\n------------\n")

                try:
                        input1 = int(input("\nEnter a number: "))
                        mymodule.toWord(input1)
                except ValueError:
                        print("Invalid input")
                except EOFError:
                        print("Invalid Input.")

                print("\n------------\n")
                
        else:
                print("Invalid data entered.")
                print("\n------------\n")




        continuationSelector = input("Do you want to continue? (1-YES, 0-NO): ")

        if continuationSelector == '1':
                os.system('cls')

                print("Hello! Welcome!")
                print("What would you like to try?\n")

                main()
        elif continuationSelector == '0':
                print("THANK YOU!")
                timer(3)

        elif listSelector not in '123456789' and listSelector != '10':
                print("Invalid data entered. Terminating...")
                timer(2)
        else: 
                print("Invalid data entered. Terminating...")
                timer(2)

        listSelector = None
        continuationSelector = None


attemptCounter = 3

while attemptCounter > 0:
        enteredPassword = input("Enter the password: ")

        if isPasswordCorrect(enteredPassword) == True:
                attemptCounter = 0

                a = input("\nAccess granted! Press ENTER to continue")
                os.system('cls')

                print("Hello! Welcome!")
                print("What would you like to try?\n")

                main()
        elif isPasswordCorrect(enteredPassword) == False and attemptCounter > 0:
                print("\nWrong Password\n")
                attemptCounter -= 1
        elif isPasswordCorrect(enteredPassword) == False and attemptCounter == 0:
                print("\nToo many wrong attempts. Terminated")
                attemptCounter -= 1