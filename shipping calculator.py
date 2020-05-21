def shippingfee(num):
     n=10.95+2.95*(num-1)
     return n

objectnum = int(input('the num of objects:'))
if objectnum>0:
    charge = shippingfee(objectnum)
    charge = round(charge, 2)
    print(f'the shipping fee is {charge}')
