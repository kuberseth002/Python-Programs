# natural number
# 1st way
# n=int(input("Enter a number:"))
# natural_num=n*(n+1)/2
# print(int(natural_num))

# 2nd way

num=int(input("Enter a number:"))
if num<0:
  print("take only positive number")
else:
  sum=0
  while(num>0):
    sum+=num
    num-=1
  print(sum)