import random

def flip_coin(times):
    heads_count = 0
    tails_count = 0

    for _ in range(times):
        result = random.choice(["Heads", "Tails"])
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    heads_percentage = (heads_count / times) * 100
    tails_percentage = (tails_count / times) * 100

    print(f"Total Flips: {times}")
    print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")

flip_coin(100)
