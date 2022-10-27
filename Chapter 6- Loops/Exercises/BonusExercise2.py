#print the following - 26/10/2022

#print("The following lines will print each letters of Apple")
#apple = ['A','p','p','l','e\n']
#for i in apple:
#  print(i)
#  if i == 'e':
#    break

#print the following

#print("The following lines will print each letters of Banana")
#apple = ['B','a','n','a','n','a\n']
#for i in apple:
#  print(i)
#  if i == apple[0::5]:
#    break

#print the following 

#print("The following lines will print each letters of Car")
#apple = ['C','a','r\n']
#for i in apple:
#  print(i)
#  if i == 'r':
#    break

#print the following 

#print("The following lines will print each letters of Dolphin")
#apple = ['D','o','l','p','h','i','n\n']
#for i in apple:
#  print(i)
#  if i == 'n':
#    break

words =["Apple\n","Banana\n","Car\n","Dolphin\n"]
for word in words:
    #THis loop is fetching word from the list 
    print("The following lines will print each letters of" +word)
    for letter in word:
      #this loop is fecthing letter for the word
      print(letter)