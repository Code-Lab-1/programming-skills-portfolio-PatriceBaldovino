#Class Activity
    #November 3, 2022

#Take a number from user, and print its table up to 10th.

def mult():
  ourNum = int(input("Enter the number you want to generate a multiplication table for: "))
  ourRange = range(1,11)
  for x in ourRange:
    result = ourNum * x
    print(ourNum," x ",x," = ",result)

print()
mult()
print()