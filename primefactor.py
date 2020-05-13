x = int(input("Enter an integer (2 or greater): "))
num = 2
fac = []
print("The prime factor of", x, "are:")
while num <= x:
    if x % num == 0:
        fac.append(num)
        x /= num
    elif x % num != 0:
        num += 1

for y in fac:
    int(y)
    print(y)