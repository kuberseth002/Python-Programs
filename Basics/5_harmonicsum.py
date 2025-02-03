num=int(input("Enter a number:"))

if num <= 0:
  print("it must be greater than 0")
else:
  sum=0
  for i in range(1,num+1):
    sum+=1/i
    print(f"The {num} th number is:{sum}")