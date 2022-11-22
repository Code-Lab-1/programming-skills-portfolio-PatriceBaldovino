## Exercise 2: Greetings

'''
    Start with the list you used in Exercise 1, but instead of just
    printing each person’s name, print a message to them. The text of
    each message should be the same, but each message should be
    personalized with the person’s name.
'''

## List of names
names = ['\tVi','\tCaitlyn','\tMel','\tViktor','\tJinx']

#Print of messages
print("Greetings to: \n")
message = f"\tHello, {names[0].title()}!!!"
print(message)

message = "\tHello, {0}!!!".format(names[1])
print(message)

message = f"\tHello, {names[2].title()}!!!"
print(message)

message = "\tHello, {0}!!!".format(names[3])
print(message)

message = f"\tHello, {names[4].title()}!!!"
print(message)