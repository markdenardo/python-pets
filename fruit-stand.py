# Fruit Stand Game
# Randomly picks a fruit from a basket until you say yes.

import random
answer=""
basket=["bananas","apples","cherries"]
while answer != "yes":
    pick=random.choice(basket)
    print(f"you got {pick}")
    answer=input("do you want this?")
print(f"enjoy your {pick}")
