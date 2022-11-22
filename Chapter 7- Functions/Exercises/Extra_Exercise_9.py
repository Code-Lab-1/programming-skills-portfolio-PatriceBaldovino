#Class Activity
    #November 3, 2022

#Take 4 numbers from user and give its average and percentage

def num():
  a = int(input("Input 1st number: "))
  b = int(input("Input 2nd number: "))
  c = int(input("Input 3rd number: "))
  d = int(input("Input 4th number: "))
  sum = int(a+b+c+d)
  average = sum / 4
  percentage = float(sum) / 400 * 100
  print("The Average: {0}".format(average))
  print("The Percentage: {0}".format(percentage))

print()
num()
print()