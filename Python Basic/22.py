# power of two

# term=10

# result=list(map(lambda x: 2**x,range(term)))

# print(term)




# num=int(input("Enter a number:"))
# n=lambda x: num**x
# for i in range(1,11):
#   print(num,f"n of {i}= {n(i)}")
  
  
  





term=10

result=list(map(lambda x: 2**x,range(term)))
print("total terms are:",term)
for i in range(term):
  print("2 raised to power is",i,result[i])
  
