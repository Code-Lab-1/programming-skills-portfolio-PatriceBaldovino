## Exercise 5: USB Shopper

    #A girl heads to a computer shop to buy some USB 
    #sticks. She loves USB sticks and wants as many as 
    #she can get for £50. They are £6 each.

    #Write a programme that calculates how many USB
    #sticks she can buy and how many pounds she will
    #have left.

        #You will to use the arithmetic operators to complete 
        #this exercise.

#Computer Shop
print('''

.--------------------------------------------.
|                                            |
|   ██████╗░███╗░░░███╗░█████╗░██╗░██████╗   |
|   ██╔══██╗████╗░████║██╔══██╗╚█║██╔════╝   |
|   ██████╦╝██╔████╔██║██║░░██║░╚╝╚█████╗░   |
|   ██╔══██╗██║╚██╔╝██║██║░░██║░░░░╚═══██╗   |
|   ██████╦╝██║░╚═╝░██║╚█████╔╝░░░██████╔╝   |
|   ╚═════╝░╚═╝░░░░░╚═╝░╚════╝░░░░╚═════╝░   |
|                                            |
|       ░██████╗██╗░░██╗░█████╗░██████╗░     |
|       ██╔════╝██║░░██║██╔══██╗██╔══██╗     |
|       ╚█████╗░███████║██║░░██║██████╔╝     |
|       ░╚═══██╗██╔══██║██║░░██║██╔═══╝░     |
|       ██████╔╝██║░░██║╚█████╔╝██║░░░░░     |
|       ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░     |
\'--------------------------------------------\'

''')

print("\\|□_□|/ Welcome to BMO\'s Computer Shop \\|□_□|/")
print()

##Store input numbers
print('.----------------------------.')
number = int(input(" Enter the amount of money: "))
print('\'----------------------------\'')

#Calculate
usb = int(number / 6)
money = number - (usb * 6)

#Printing of output
print('.----------------------------------.')
print("The amount of USB's you can buy: {0}".format(usb))
print()
print("The amount of money left: {0}".format(money))
print("\'----------------------------------\'")