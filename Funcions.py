'''
To demonstrate 
'''

def facto(number):
    fact=1
    for i in range(1,number+1):
        fact=fact*i
    print("Factorial ->" , fact)

facto(0)
facto(1)
facto(9)
facto(19)

