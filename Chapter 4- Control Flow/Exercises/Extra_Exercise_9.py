#

print('''
        _____
     _.'_____`._
   .'.-'  12 `-.`.
  /,' 11      1 `.\\
 // 10      /   2 \\\\
;;         /       ::
|| 9  ----O      3 ||   Please arrive at 9!
::                 ;;
 \\\\ 8           4 //
  \`. 7       5 ,'/
   '.`-.__6__.-'.'
    ((-._____.-))
    _))       ((_
   '--'SSt    '--'
''')

time = int(input("Enter time:"))
if time < 9:
    print("\nYoure early nice!\n")
elif time == 9 :
   print("\nOn time\n")
elif time > 9 and time <= 19:
   print("\n10 minutes late\n")
elif time > 19 and time <= 39:
  print("\n30 minutes late\n")
elif time > 39:
  print("\nZero marks\n") 
else:
    print("\nWhy bother coming\n")