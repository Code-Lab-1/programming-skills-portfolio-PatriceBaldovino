#Exercise 7:
  #September 21, 2022

'''
    - Create 5 subjects variables and take marks from the user
    - calculate the total marks of the students and store those 
      in variable "mark_obtained"
    - total_marks is equal to 500.
    - calculate average of the marks and store it in variable "average"
    - calculate percentage of the student and store it in variable "percentage"
    - Print average and percentage marks of the student
'''

print()
#Input the scores
math_score = input("Enter score in math: ")
english_score = input("Enter score in english: ")
science_score = input("Enter score in science: ")
history_score = input("Enter score in history: ")
PE_score = input("Enter score in PE: ")
print()

# Adding of Marks
marks_obtained = math_score + english_score + science_score + history_score + PE_score
total_marks = 500
average = int(marks_obtained) / 5
percentage = int(marks_obtained) / 500 * 100

print("Average: ", average)
print("Percentage: ", percentage)