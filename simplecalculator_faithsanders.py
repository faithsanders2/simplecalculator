#Faith Sanders 
#11/29

#Initialize 
#Function
def addition(num1, num2):
    #code that adds both parameters and prints. the result goes here
    solution = num1 + num2
    return solution
def subtraction(num1,num2): 
    #code that subtracts both parameters and prints. the result goes here
    solution = num1 - num2 
    return solution
def multiplication(num1, num2): 
    #code that multiplies both parameters and prints. the result goes here
    solution = num1 * num2 
    return solution
def division(num1, num2): 
    #code that divides both parameters and prints. the result goes here
    solution = num1 / num2 
    return solution
def mod(num1, num2): 
    #code that divides the second number into first and presents the remainder. the result goes here
    solution = num1 % num2
    return solution

def simpleCalculator(): 
    #If statements to figure out what operation to perform goes here 
    if option == 1: 
        print(addition(num1,num2)) 
    elif option == 2: 
       print(subtraction(num1, num2))
    elif option == 3: 
        print(multiplication(num1, num2))
    elif option == 4: 
       print(division(num1, num2))
    elif option == 5: 
        print(mod(num1, num2)) 
    elif option == 6: 
        quit()

#Main
print("Welcome to Simple Calculator by Texas Instrument c.2023)")
print("Please choose an operation: (Type in a number be3tween 1-5)")
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n5. Mod\n6. Quit")
option = int(input("Option: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

simpleCalculator()


