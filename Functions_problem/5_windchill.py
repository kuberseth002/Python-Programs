def wind(t,v):
  return 35.74 + 0.6215 * t + (0.4275*t-35.74)*(v**0.16)

t=float(input("Enter temperature:"))
v=float(input("Enter speed:"))


if(t) > 50 or v > 120 or v<3:
  print("invalid input")

else:
  print(f"wind chill:{wind(t,v):.2f}")