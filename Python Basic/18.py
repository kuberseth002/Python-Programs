# amstrong number
num=int(input("Enter a number:"))
temp=num
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
    
if num==sum:
    print("True")
else:
    print("False")
    
    
    

# interval of amstrong

    

# Program to check Armstrong numbers in a certain interval

lower = 100
upper = 2000

for num in range(lower, upper + 1):
   order = len(str(num))    
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
    
