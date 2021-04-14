'''Question:-
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm.
How many rabbits and how many chickens do we have?
Hint:
Use for loop to iterate all possible solutions.
'''
heads=int(input("Enter the number of heads:"))
legs=int(input("Enter the number of legs:"))
if(legs%2!=0):
    print("Can't be counted.")
else:
    for chi in range(heads+1):
        rab=heads-chi
        if (2*chi)+(4*rab)==legs:
            print("Number of Chickens=",chi)
            print("Number of Rabbits=",rab)
