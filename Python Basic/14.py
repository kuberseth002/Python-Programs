# prime number

num=int(input("Enter a number:"))
if num>1:
  for i in range(2,num):
    if num%i==0:
      print("not prime")
      break
    else:
      print("it is prime")
      break
else:
  print("not prime")
  
  
  # interval of prime numbers
  
lower_interval=100
upper_interval=300

for num in range(lower_interval,upper_interval):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
      else:
        print(num)
        break
        