import random

first = input("What’s your first name? ")
last = input("What’s your last name? ")

nickname1 = first[:3] + last[-3:]
nickname2 = first[-2:] + last[:2]
nickname3 = first[:2] + last[:2] + random.choice(["_", "007", "99", "!"])

print("\nHere are your nickname options:")
print("⭐", nickname1)
print("⭐", nickname2)
print("⭐", nickname3)

style = input("\nDo you want a short or fun one? (short/fun): ")
if style == "short":
    print("Try this one:", nickname1)
else:
    print("Try this fun one:", nickname3)

with open("nicknames.txt", "w") as file:
    file.write(nickname1 + "\n")
    file.write(nickname2 + "\n")
    file.write(nickname3 + "\n")
