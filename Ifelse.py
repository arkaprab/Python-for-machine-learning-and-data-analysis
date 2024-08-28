a=30
b=78

if(a>b) :
    print("A is greater than B")
else:
    print("B is greater than A")

c=int(input("Enter value of 'c':"))
d=int(input("Enter the value of 'd':"))
if(c>d):
    print("'c' is greater than 'd'.")
else:
    print("'d' is greater than 'c'.")

# implementation of elif statement
r=5
c=6
u=8
if(r>c and r>u):
    print("'r' is the largest element.")
elif(c>r and c>u) :
    print("'c' is the largest element.")
else:
    print("'u' is the largest element.")
print("Thank you.")