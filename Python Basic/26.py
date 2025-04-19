# hcf number

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

if num1 > num2:
  smaller=num2
else:
  smaller=num1
  
for i in range(1,smaller+1):
  if num1%i==0 and num2%i==0:
    hcf=i
print(hcf)

lcm=(num1*num2)/hcf
print(lcm)  