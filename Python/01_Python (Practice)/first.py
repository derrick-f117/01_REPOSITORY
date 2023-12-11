#!/bin/python3

#HELLO
def nl():
    print("\n")

print("Hello, World!")
print("^^^^^^^^^^^^^")
print("-" * 13)
print("-" * 19)

#let's do a quiz;
nl()

print("Let's do a quiz!😁")
print("^^^^^^^^^^^^^^^^^^^")
print("#1. Math 😈")
print("-" * 11)

def q1Math():
    print("Question 1:")
    print("===========")
    print("Solve the following:")
    q1a = input("1 + 3 =  ")
    q1b = input("23 + 45 * 65 =  ")
    q1c = input("84 / 24 * 8 - 5 =  ")
    nl()
    if int(q1a) == 1 + 3 and int(q1b) == 23 + 45 * 65 and int(q1c) == 84 / 24 * 8 - 5:
        print("Sheesh! You're on fire!🔥🔥🔥")
        nl()
    elif int(q1a) == 1 + 3 and int(q1b) == 23 + 45 * 65 and int(q1c) != 84 / 24 * 8 - 5:
        print("You were really close, but the answer to part three is "+str(84 / 24 * 8 - 5))
        nl()
        print("You can try again")
        nl()
    elif int(q1a) == 1 + 3 and int(q1b) != 23 + 45 * 65 and int(q1c) == 84 / 24 * 8 - 5:
        print("You were really close, but the answer to part two is "+str(23 + 45 * 65))
        nl()
        print("You can try again")
        nl()
    elif int(q1a) != 1 + 3 and int(q1b) == 23 + 45 * 65 and int(q1c) == 84 / 24 * 8 - 5:
        print("You were really close, but the answer to part one is "+str(1 + 3))
        nl()
        print("You can try again")
        nl()
    elif int(q1a) != 1 + 3 and int(q1b) != 23 + 45 * 65 and int(q1c) == 84 / 24 * 8 - 5:
        print("At least you got one right 🤷🏾‍♂️")
        print("Allow me to help;")
        print("Part one is "+str(1 + 3))
        print("Part two is "+str(23 + 45 * 65))
        nl()
        print("Practice makes perfect!")
        nl()
    elif int(q1a) != 1 + 3 and int(q1b) == 23 + 45 * 65 and int(q1c) != 84 / 24 * 8 - 5:
        print("At least you got one right 🤷🏾‍♂️")
        print("Allow me to help;")
        print("Part one is "+str(1 + 3))
        print("Part three is "+str(84 / 24 * 8 - 5))
        nl()
        print("Practice makes perfect!")
        nl()
    elif int(q1a) == 1 + 3 and int(q1b) != 23 + 45 * 65 and int(q1c) != 84 / 24 * 8 - 5:
        print("At least you got one right 🤷🏾‍♂️")
        print("Allow me to help;")
        print("Part two is "+str(23 + 45 * 65))
        print("Part three is "+str(84 / 24 * 8 - 5))
        nl()
        print("Practice makes perfect!")
        nl()
    else:
        print("Okay, maybe this wasn't for you. Let's try sth else.")
        nl()

def q2Math():
    print("Question2")
    carValue = "1800000"
    carSaleLoss = "20%"
    print(f"""Samuel bought a car for {carValue}. He later sold the car at a {carSaleLoss} loss. Find:
        ...the loss he incurred on the sale of the car.
        ...the selling price of the car.""")
    q2a = input("The loss: ")
    q2b = input("The selling price: ")
    nl()
    carSaleLossVal = 20 / 100 * int(carValue)
    carSaleVal = 80 / 100 * int(carValue)
    if int(q2a) == carSaleLossVal and int(q2b) == carSaleVal:
        print("Dynamite!🧨")
        nl()
    elif int(q2a) != carSaleLossVal and int(q2b) == carSaleVal:
        print("You missed the first one. The correct answer is "+str(carSaleLossVal))
        print("You can always try again😁.")
    elif int(q2a) == carSaleLossVal and int(q2b) != carSaleVal:
        print("You missed the second one. The correct answer is "+str(carSaleVal))
        nl()
        print("You can always try again😁.")
        nl()
    else:
        print("Okay, maybe not the subject for you🤷🏾‍♂️")
        print("The correct answer to the first part is "+str(carSaleLossVal))
        print("The correct answer to the second part is "+str(carSaleVal))
        nl()
        print("Practice makes perfect.")
        nl()
    
q1Math()
q2Math()

nl()

print("#1. Physics 😈")
print("-" * 14)

def q1Physics():
    print("Question 1")
    print("==========")
    print("NB: Where answers are stated, the answer has to be exactly the same as mine.")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("State Newton's:")
    q1pa = input("First law of motion: ")
    q1pb = input("Second law of motion: ")
    q1pc = input("Third law of motion: ")
    ans1pa = "A body remains in its state of rest or motion in a straight line unless acted upon by an external force."
    ans1pb = "The rate of change of linear momentum of a body is directly proportional to the resultant external force acting on the body and takes place in the direction of the force."
    ans1pc = "For every action, there is an equal and opposite reaction."
    if q1pa == ans1pa and q1pb == ans1pb and q1pc == ans1pc:
        nl()
        print("You're amazing!🤩")
        nl()
    elif q1pa != ans1pa and q1pb == ans1pb and q1pc == ans1pc:
        nl()
        print(f"""Part one is incorrect. The correct answer is 
        \"{ans1pa}\"""")
        print("Just keep trying.")
        nl()
    elif q1pa == ans1pa and q1pb != ans1pb and q1pc == ans1pc:
        nl()
        print(f"""Part two is incorrect. The correct answer is
        \"{ans1pb}\"""")
        nl()
    elif q1pa == ans1pa and q1pb == ans1pb and q1pc != ans1pc:
        nl()
        print(f"""Part three is incorrect. The correct answer is
        \"{ans1pc}\"""")
        nl()
    elif q1pa != ans1pa and q1pb != ans1pb and q1pc == ans1pc:
        nl()
        print(f"""Part one and part two are both incorrect. The correct respective answers are:
            \"{}\"
            \"\"""")
