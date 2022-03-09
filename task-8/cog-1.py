import numpy as np
#Question-1
x=input("Enter first number ")
y=input("Enter last number ")
x=int(x)
y=int(y)
s=". 0. 0. 0. 0. 0."
p=""
for i in range(x,y):
    p=p+str(i)+s
print("Output is ")
print(p+str(y))