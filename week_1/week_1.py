#### **TASK 1: Store student and course information**
student_name = "Ali"
course_name = "Introduction to Computer Science"

### **TASK 2: Store three assignment grades**
# Create three float variables to hold the grades for three separate assignments.
grade_1 = 87.5
grade_2 = 92.0
grade_3 = 78.0

### **TASK 3: Calculate the total and the average**
total = grade_1 + grade_2 + grade_3
average = total / 3
average = round(average, 2)

### **TASK 4: Print the grade report**
print("--------------------------------------------")
print("          STUDYVAULT - GRADE REPORT         ")
print("--------------------------------------------")

# To combine a string and a number, we use str() to convert the number
print("Student : " + student_name)
print("Course  : " + course_name)
print("")
print("Assignment 1 : " + str(grade_1))
print("Assignment 2 : " + str(grade_2))
print("Assignment 3 : " + str(grade_3))
print("")
print("Total Points : " + str(total))
print("Your Average : " + str(average) + "%")
print("--------------------------------------------")