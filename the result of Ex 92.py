from alex import PrimeNumIndicate


num = int(input('Please Input an Positive Int Number Greater Than One >'))
i = PrimeNumIndicate(num)
if i:
    print('This number is a Prime Number')
else:
    print('This number is not a Prime Number')