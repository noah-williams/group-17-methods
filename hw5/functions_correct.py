import math

## opens a file in read mode
## filename received as a parameter
def openFile(filename):
    try:
        infile = open(filename, "r")

        print("File opened.")
    except FileNotFoundError:
        print("\nThat file does not exist.")

## takes two numbers and returns
## the result of a division
def numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("\nYou tried to divide by zero.")
    except TypeError:
        print("\nYou tried to input the wrong data type.")

## takes in two points
## finds the distance between the points
def dist(x1, y1, x2, y2):
    ## exponent
    ## I think you need an absolute value
    dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
    dist = math.sqrt(dist)

    return dist

## takes in a string -- reverses it
## then compares the two
def isPalindrome(temp):
    ## reverses the array
    test = temp[::-1]

    if(test == temp):
        return True

    else:
        return False

## has input to receive two numbers
## divides the two, then outputs the result
def divide():
    ## / always outputs a float
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num2 != 0:
        div = num1 / num2
        print("Your numbers divided is:", div)
    else:
        print("Error: Divide by Zero.")
        
        
        
## returns the squareroot of a particular number
def sq(num):
    ## No checking for negative numbers...negative will throw an error
    return math.sqrt(num)

## grabs user's name
## greets them by their entire name
## names should be strings
def greetUser(first, middle, last):
    print("Hello!")
    ## This will be spaced weird I think     Perhaps fixed? -js
    print("Welcome to the program, ", first, " ", middle, " ", last, ". \n")
    print("Glad to have you!")

## takes in a Python list
## attempts to display the item at the index provided
def displayItem(numbers, index):
    ## Doesn't check if the array has that index
    print("Your item at", index, "index is", numbers[index])
