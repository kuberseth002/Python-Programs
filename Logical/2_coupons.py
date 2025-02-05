import random

def collect_coupons(n):
    collected = set() 
    count = 0 

    while len(collected) < n:
        coupon = random.randint(1, n)  
        collected.add(coupon)  
        count += 1 

    return count

n = int(input("Enter the number of distinct coupons: "))

total_numbers = collect_coupons(n)

print("Total random numbers needed:", total_numbers)