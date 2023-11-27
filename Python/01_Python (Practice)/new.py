#!/bin/python3

def nl():
    print("\n")

nl()
print("MY PRACTICE SESSION")

nl()

print("My name is Derrick Abuga and I am learning how to code in python. I would like to be a Penetration Tester or SOC Analyst in the future.")

nl()

myName = "Derrick Abuga"
myActivity = "learning how to code in python"
myGoal1 = "Penetration Tester"
myGoal2 = "SOC Analyst"

print("My name is "+myName+" and I am "+myActivity+". I would like to be a "+myGoal1+" or "+myGoal2+" in the future.")

nl()

print(f"My name is {myName} and I am {myActivity}. I would like to be a {myGoal1} or {myGoal2} in the future.")

nl()

print("""I am interested in:
    1. Coding
    2. Cybersecurity
    3. Gaming
    4. Game development
    5. Artificial Intelligence
And that's why I want to learn more about them.""")

nl()

#I am going for breakfast, after which I will build a calculator.

print("Time to Build Some Stuff")
nl()
print("#1: Calculator")
nl()

intro = "Welcome to my Calculator!"
under = "^^^^^^^^^^^^^^^^^^^^^^^^^"
print(intro)
print(under)

x = input("Give me a number: ")
op = input("Give me an operator: ")
y = input("Give me another number: ")


def calculator():
    if op == "+" or op == "plus":
        print("The answer is:")
        print(int(x) + int(y))
        print("\n")
        print("Thank you for using my calculator.")
    elif op == "-" or op == "minus":
        print("The answer is:")
        print(int(x) - int(y))
        print("\n")
        print("Thank you for using my calculator.")
    elif op == "x" or op == "*" or op == "times" or op =="multiplication":
        print("The answer is:")
        print(int(x) * int(y))
        print("\n")
        print("Thank you for using my calculator.")
    elif op == "/" or op == ":" or op == "division":
        print("The answer is:")
        print(int(x) / int(y))
        print("\n")
        print("Thank you for using my calculator.")
    elif op == "**" or op == "^" or op == "raise to" or op == "index":
        print("The answer is:")
        print(int(x) ** int(y))
        print("\n")
        print("Thank you for using my calculator.")
    else:
        nl()
        print("Error 001: Operator not recognised.")
        print("\n")
        print("Thank you for using my calculator.")

calculator()

nl()