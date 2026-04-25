### **TASK 1: Define constants and display a welcome banner**
PASSING_THRESHOLD = 60.0
NUM_SUBJECTS = 3
NUM_GRADES_PER_SUBJECT = 3

# --- Welcome banner ---
print("============================================")
print("           Welcome to StudyVault!")
print("============================================")

### **TASK 2: Collect the student's name using input()**
student_name = input("Enter your name: ")

print("")
print("You will enter grades for " + str(NUM_SUBJECTS) + " subjects.")
print("Each subject has " + str(NUM_GRADES_PER_SUBJECT) + " assignments.")
print("")

### **TASK 3: Create an accumulator variable for the overall average**
# === FOR LOOP: repeat for each subject ===
# range(1, NUM_SUBJECTS + 1) produces: 1, 2, 3
# The loop variable subject_num takes each value in turn
total_average_sum = 0.0
for subject_num in range(1, NUM_SUBJECTS + 1):

    print("--- Subject " + str(subject_num) + " ---")
    subject_name = input("  Subject name: ")

    # Accumulator for grades within this subject
    grade_total = 0.0

    # === NESTED FOR LOOP: collect each grade ===
    for grade_num in range(1, NUM_GRADES_PER_SUBJECT + 1):

        # === WHILE LOOP: keep asking until we get a valid grade ===
        # A while loop runs as long as its condition is True
        while True:
            # True means "loop forever until we explicitly stop"
            raw_input = input("  Grade " + str(grade_num) + " (0-100): ")

            # Convert the string input to a float for arithmetic
            grade = float(raw_input)

            if 0 <= grade <= 100:
                # Valid grade: exit the while loop with break
                break
            else:
                # Invalid grade: print message and loop again (continue is implicit here)
                print("  Invalid grade. Please enter a number between 0 and 100.")

        # Add the valid grade to the running total
        grade_total = grade_total + grade

    # --- Calculate this subject's average ---
    subject_average = grade_total / NUM_GRADES_PER_SUBJECT
    subject_average = round(subject_average, 2)

    # --- Determine letter grade (Week 3-4 logic, reused inside the loop) ---
    if subject_average >= 90:
        letter_grade = "A"
        feedback = "Outstanding!"
    elif subject_average >= 80:
        letter_grade = "B"
        feedback = "Really good work!"
    elif subject_average >= 70:
        letter_grade = "C"
        feedback = "Passing. Push harder."
    elif subject_average >= 60:
        letter_grade = "D"
        feedback = "At risk. Seek support."
    else:
        letter_grade = "F"
        feedback = "See your advisor urgently."

    # --- Determine pass / fail ---
    if subject_average >= PASSING_THRESHOLD:
        status = "PASS"
    else:
        status = "FAIL"

    # --- Print this subject's result ---
    print("  Result: " + str(subject_average) + "% | "
          + letter_grade + " | " + status + " | " + feedback)
    print("")

    # --- Add this subject's average to the running total ---
    total_average_sum = total_average_sum + subject_average

# === AFTER THE LOOP: calculate and display overall summary ===

overall_average = total_average_sum / NUM_SUBJECTS
overall_average = round(overall_average, 2)

# Determine overall letter grade (same logic applied again)
if overall_average >= 90:
    overall_letter = "A"
elif overall_average >= 80:
    overall_letter = "B"
elif overall_average >= 70:
    overall_letter = "C"
elif overall_average >= 60:
    overall_letter = "D"
else:
    overall_letter = "F"

print("============================================")
print("  SEMESTER SUMMARY FOR: " + student_name)
print("============================================")
print("  Subjects completed : " + str(NUM_SUBJECTS))
print("  Overall average    : " + str(overall_average) + "%")
print("  Overall grade      : " + overall_letter)
print("============================================")