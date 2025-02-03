power=int(input("Enter the value:"))

if power<=0 or power>=31:
  print("it is not between 1-30")
else:
  print("table of 2:")
  for i in range(power+1):
    print(f"2^{i}={2**i}")
  