"""
get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(bonus)
    sales = float(input("Enter sales: $"))
print("bye")
