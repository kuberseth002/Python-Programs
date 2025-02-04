def add_zero():
  res=[]
  list=[]
  
  len=int(input("Enter length if list: "))
  for i in range(len):
    num=int(input("Enter a number:"))
    res.append(num)
    
  for i in range(len-2):
    for j in range(i+1,len):
      for k in range(j+1,len):
        if res[i] + res[j] + res[k]==0:
          list.append([res[i],res[j],res[k]])
  print(list)
add_zero()          
    