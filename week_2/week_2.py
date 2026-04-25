### **TASK 1 & 2: Setup Week 2 Code and Define Constants**
student_name = "Ali"
course_name = "Introduction to Computer Science"

grade_1 = 87.5
grade_2 = 92.0
grade_3 = 78.0

total = grade_1 + grade_2 + grade_3

average = total / 3
average = round(average, 2)
print(student_name)
print(course_name)
print(total)
print(average)

PASSING_THRESHOLD = 60.0

### **TASK 3: Determine the letter grade using if / elif / else**
letter_grade = ""
feedback = ""

if average >= 90:
  letter_grade = "A"
  feedback = "Excellent work!"
elif average >= 80:
  letter_grade = "B"
  feedback = "Good job!"
elif average >= 70:
  letter_grade = "C"
  feedback = "Keep up the good work!"
elif average >= 60:
  letter_grade = "D"
  feedback = "You can do better!"
else:
  letter_grade = "F"
  feedback = "You need to work harder!"

### **TASK 4: Determine pass / fail status**
status = ""

if average >= PASSING_THRESHOLD:
  status = "Pass"
else:
  status = "Fail"

### **TASK 5: Detect a dangerous grade pattern using 'and' / 'or'**
has_low_grade = (grade_1 < 60) or (grade_2 < 60) or (grade_3 < 60)
needs_warning = (average < 75) and (has_low_grade == True)

### **TASK 6: Update the print block and add conditional output**
print("--------------------------------------------")
print("          STUDYVAULT - GRADE REPORT         ")
print("--------------------------------------------")
print("Student : " + student_name)
print("Course  : " + course_name)
print("")
print("Assignment 1 : " + str(grade_1))
print("Assignment 2 : " + str(grade_2))
print("Assignment 3 : " + str(grade_3))
print("")
print("Total Points  : " + str(total))
print("Your Average  : " + str(average) + "%")
print("Letter Grade  : " + letter_grade)
print("Status        : " + status)
print("")
print("Feedback: " + feedback)

# Conditional Output (Only prints if true)
if needs_warning:
    print("*** WARNING ***")
    print("You have at least one failing grade and a low average. Seek tutoring.")

print("--------------------------------------------")