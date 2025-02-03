import math

def factor(n):
  while n%2==0:
    i=2
    while i*i<=n:
      while n%i==0:
        print(i,end=" ")
        n//i
        i+=1
        if n>1:
         print(n)
  n=int(input("enter a number: "))
  print("prime factor are: ",end=" ")        
  factor(n)
  
