quad_a=int(input("Enter the value:"))
quad_b=int(input("Enter the linear value:"))
quad_c=int(input("Enter a constant value:"))

delta=quad_b**2 -4*quad_a*quad_c
root1=(-quad_b+delta**0.5)/2*quad_a
root2=(-quad_b - delta**0.5)/2*quad_a

print(f"The roots are ({root1},{root2})")


