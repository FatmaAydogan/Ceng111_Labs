### **TASK 1 & 2: Define get_letter_grade() and get_feedback()**
def get_letter_grade(average):
    """Returns the letter grade based on the average."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def get_feedback(average):
    """Returns motivational feedback based on the average."""
    if average >= 90:
        return "Excellent work! You have mastered the material."
    elif average >= 80:
        return "Great work. Keep pushing for that A."
    elif average >= 70:
        return "Good effort, but there is room for improvement."
    elif average >= 60:
        return "You passed, but please review the materials closely."
    else:
        return "Critical: Please see your instructor immediately."

### **TASK 3 & 4: Default Parameters, GPA, and Study Hours**
PASSING_THRESHOLD = 60.0

def is_passing(average, threshold=PASSING_THRESHOLD):
    """Returns True if average meets the threshold, False otherwise."""
    return average >= threshold

def convert_to_4_scale(average):
    """Converts percentage average to a 4.0 GPA scale."""
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def recommend_study_hours(average):
    """Recommends weekly study hours based on current performance."""
    if average >= 85:
        return 10
    elif average >= 70:
        return 15
    elif average >= 60:
        return 20
    else:
        return 25

### **TASK 5: Exception Handling (try / except)**
def validate_grade(raw_input):
    """Attempts to convert string to float. Returns valid grade or -1.0 if error."""
    try:
        grade = float(raw_input)
        if 0.0 <= grade <= 100.0:
            return grade
        else:
            return -1.0
    except ValueError:
        return -1.0

    ### **TASK 6: Visual Separator Function**
def print_separator(char="-", width=44):
    """Prints a formatting line. Uses default characters if none provided."""
    print(char * width)

### **TASK 7: Refactor the Main Program**
def main():
    print_separator("=")
    print("          Welcome to StudyVault!          ")
    print_separator("=")

    student_name = input("Enter your name: ")
    print("\nYou will enter grades for 3 subjects.\n")

    total_gpa_points = 0.0

    for subject_num in range(1, 4):
        print(f"--- Subject {subject_num} ---")
        subject_name = input("  Subject name: ")

        subject_total = 0.0

        for grade_num in range(1, 4):
            valid = False
            while not valid:
                raw_val = input(f"  Grade {grade_num} (0-100): ")
                # TASK 7.2: Use validation function
                grade = validate_grade(raw_val)

                if grade != -1.0:
                    subject_total += grade
                    valid = True
                else:
                    print("  Invalid grade. Please enter a number between 0 and 100.")

        subject_average = round(subject_total / 3, 2)

        # TASK 7.3: Use our functions instead of long if/else blocks!
        letter = get_letter_grade(subject_average)
        feedback = get_feedback(subject_average)
        gpa = convert_to_4_scale(subject_average)
        hours = recommend_study_hours(subject_average)

        if is_passing(subject_average):
            status = "PASSING"
        else:
            status = "FAILING"

        total_gpa_points += gpa

        print_separator()
        print(f"  Subject     : {subject_name}")
        print(f"  Average     : {subject_average}%")
        print(f"  Grade       : {letter}")
        print(f"  GPA Points  : {gpa} / 4.0")
        print(f"  Status      : {status}")
        print(f"  Study hrs   : {hours} hrs/week recommended")
        print(f"  Feedback    : {feedback}")
        print_separator()
        print("")

    # SEMESTER SUMMARY
    overall_gpa = round(total_gpa_points / 3, 2)
    # We can even use our feedback function backwards by mapping GPA back to a percentage scale mentally,
    # or just write a custom one. For simplicity, we adapt it here:
    final_feedback = get_feedback(overall_gpa * 25) # Quick math to convert 4.0 scale to 100 scale for feedback

    print_separator("=")
    print(f"  SEMESTER SUMMARY FOR: {student_name}")
    print(f"  Overall GPA   : {overall_gpa} / 4.0")
    print(f"  {final_feedback}")
    print_separator("=")

# Start the program
main()
