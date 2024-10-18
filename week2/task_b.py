gradeInput = int(input("Enter your grade (0 - 100): "))
if 0 <= gradeInput<= 100:
    print("Your grade is: A")
elif 60 <= gradeInput <= 79:
    print("Your grade is: B")
elif 50 <= gradeInput<= 59:
    print("Your grade is: C")
elif 40 <= gradeInput <= 49:
    print("Your grade is: D")
elif 0 <= gradeInput<= 39:
    print("Your grade is: F")
else:
  print("Error: Grades must be between 0 and 100")
