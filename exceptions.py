from sys import exit 

x = int(input("x = "))
y = int(input("y = "))

try:
    result = x / y

except:
    print("Heyyy you cannot do it. what you think!")
    exit(1)


print(f"The result of {x} divided by {y} is equal to {result}")