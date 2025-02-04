import math
def eucilidean():
  x=int(input("Enter a number:"))
  x1=int(input("Enter a second number:"))
  y=int(input("Enter a third number:"))
  y1=int(input("Enter fourth number:"))
  
  distance=math.sqrt(((x-x1)**2)+((y-y1)))
  print(distance)
eucilidean()  

  