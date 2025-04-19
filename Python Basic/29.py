# calculator
def add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Mul(a,b):
    return a*b
def div(a,b):
    return a/b

operator=input("Enter operator:")
if operator=='+':
    print(add(20,30))

if operator=='-':
    print(Sub(20,30))


if operator=='*':
    print(Mul(20,30))
    
    
if operator=='/':
    print(div(20,30))