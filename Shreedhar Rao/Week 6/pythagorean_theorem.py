# This is a code where you input a part of the pythagorean theorem and get the result
from math import sqrt

ans = input("what variable are you trying to find? a, b, or c: ")
if ans == 'c':
    varA = int(input("What is 'a' equal to?: "))
    varB = int(input("What is 'b' equal to?: "))
    varC = sqrt(varA * varA + varB * varB)
    print("c is equal to:")
    print(varC)
elif ans == 'b':
    varC = int(input("What is 'c' equal to?: "))
    varA = int(input("What is 'a' equal to?: "))
    varB = sqrt(varC * varC - varA * varA)
    print("b is equal to: ")
    print(varB)
elif ans == 'a':
    varC = int(input("What is 'c' equal to?: "))
    varB = int(input("What is 'B' equal to?: "))
    varA = sqrt(varC * varC - varB * varB)
    print("A is equal to: ")
    print(varA)