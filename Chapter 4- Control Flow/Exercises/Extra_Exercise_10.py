
# Defining a list of elements
actions = ["wake", "wash", "eat", "work", "play", "sleep"]
for action in actions:
    if action == "work":
        break          # if the action is sleep, this would terminate the loop completely
    elif action == "play":
        continue       # if the action is play, the loop continues to next iteration 
    else:
        print (action)