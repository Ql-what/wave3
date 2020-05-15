from math import sqrt


def Hypotenuse(a, b):
    if a > 0 and b > 0:
        hy = sqrt(a**2 + b**2)
        return hy
    else:
        return 'Invalid Value'


print("---- Right Triangle Hypotenuse Calculator ----")
side1 = int(input('please enter the dimension of a shorter side >'))
side2 = int(input('please enter the dimension of another shorter side >'))
print(f'The dimension of hypotenuse is {Hypotenuse(side1, side2)}')