
### **PROJECT TASK: Upgrading StudyVault**

#**The Goal:** Update your program so that it no longer asks for a fixed number of grades. Instead, it should keep asking for grades until the user enters **-1**. All valid grades should be stored in a **list**.

#*Requirements:**
#1. Create an empty list called `all_grades`.
#2. Use a `while` loop to get input from the user.
#3. If the input is -1, break the loop.
#4. Otherwise, use `append()` to add the grade to the list.
#5. After the loop, calculate the average using `sum(all_grades) / len(all_grades)`.
def main():
    all_grades = []

    print("Welcome to StudyVault Dynamic Grade Entry")
    print("(Enter -1 to stop and calculate average)")

    while True:
        user_input = float(input("Enter grade: "))

        if user_input == -1:
            break

        # TODO: Add the user_input to all_grades list
        all_grades.append(user_input)

    if len(all_grades) > 0:
        avg = sum(all_grades) / len(all_grades)
        print(f"\nProcessed {len(all_grades)} grades.")
        print(f"Your average is: {avg:.2f}%")
    else:
        print("No grades were entered.")

main()

"""Task Summary
6. Write is safe__position(position, x_limits, y_limits).
7. Inside the function, unpack the three tuples into clear variables.
8. Return True only when both coordinates are inside their limits, including the boundaries.
9. Use a for loop to test every position in the list and print the tuple with the result."""
positions = [(2.5,1.2),(5.4,2.8),(3.1,-0.2),(4.9,2.9)]
x_limits=(0.0,5.0)
y_limits= (0.0,3.0)

def is_safe_position(position, x_limits, y_limits):
    x, y = position
    x_min, x_max = x_limits
    y_min, y_max = y_limits
    return x_min <= x <= x_max and y_min <= y <= y_max
for pos in positions:
    result = is_safe_position(pos, x_limits, y_limits)
    print(pos, result)

"""Task Summary
10. Write average
_
list(values) without using sum.
11. Write count_above__limit(values, limit).
12. Write max_value(values) without using max.
13. Print the average current, the number of values above 13.0, and the maximum value."""

currents = [12.0 ,12.5 ,13.0,13.0,13.5 ,14.0]
def average_list(values):
    total = 0
    for i in values:
        total += i
        return total/len(currents)
def count_above_limit(values , limit):
    count = 0
    for i in values:
        if i > limit:
            count +=1
    return count
def max_value(values):
    if not values:
        return None
    max_value = values[0]
    for i in values:
        if i > max_value:
            max_value = i
        return max_value
avg_res = average_list(currents)
count_res = count_above_limit(currents, 13.0)
max_res = max_value(currents)
print(avg_res)
print(count_res)
print(max_res)

"""14. Write warning_times(samples, limits) and return a list of minutes outside the safe range.
15. Write first_high_temperature_time(samples, high_limit) using a while loop.
16. If no high temperature exists, return -1.
17. Print the warning-time list and then print the first high-temperature time."""

samples =[(0,20.1),(5,20.4),(10,21.0),(15,23.6),(20,22.2),(25,19.7),(30,20.3)]
limits = (20.0,23.0)
def warning_times(samples, limits):
   warnings = []
   low_limit, high_limit = limits
   for minute, temperature in samples:
       if temperature < low_limit or temperature > high_limit:
           warnings.append(minute)
   return warnings
def first_high_temperature_time(samples, high_limit):
   i = 0
   while i < len(samples):
       minute, temperature = samples[i]
       if temperature > high_limit:
           return minute
       i += 1
   return -1
warnings_list = warning_times(samples, limits)
first_high_time = first_high_temperature_time(samples, limits[1])
print(warnings_list)
print(first_high_time)

"""18. Write average_voltage(cells).
19. Write countbad__cells(cells, limits).
20. Write firstbad__cell(cells, limits) using while and return the cell number, not the list index.
21. Write pack_ready(cells, limits, maxbad__cells).
22. Return True only if the average voltage is between 3.90 and 4.05 inclusive and the bad-cell count is atmost max bad cells."""

cells = [(1, 3.98), (2, 4.01), (3, 3.76), (4, 4.05), (5, 3.81), (6, 4.12)]
cell_limits = (3.80, 4.10)

def average_voltage(cells):
    total = 0
    for _, voltage in cells:
        total += voltage
    return total / len(cells)


def count_bad_cells(cells, limits):
    low, high = limits
    count = 0
    for _, voltage in cells:
        if voltage < low or voltage > high:
            count += 1
    return count


def first_bad_cell(cells, limits):
    low, high = limits
    i = 0
    while i < len(cells):
        cell_num, voltage = cells[i]
        if voltage < low or voltage > high:
            return cell_num
        i += 1
    return -1


def pack_ready(cells, limits, max_bad_cells):
    avg = average_voltage(cells)
    bad_count = count_bad_cells(cells, limits)
    if 3.90 <= avg <= 4.05 and bad_count <= max_bad_cells:
        return True
    return False


cells = [(1, 3.98), (2, 4.01), (3, 3.76), (4, 4.05), (5, 3.81), (6, 4.12)]
cell_limits = (3.80, 4.10)


def average_voltage(cells):
    total = 0
    for _, voltage in cells:
        total += voltage
    return total / len(cells)


def count_bad_cells(cells, limits):
    low, high = limits
    count = 0
    for _, voltage in cells:
        if voltage < low or voltage > high:
            count += 1
    return count


def first_bad_cell(cells, limits):
    low, high = limits
    i = 0
    while i < len(cells):
        cell_num, voltage = cells[i]
        if voltage < low or voltage > high:
            return cell_num
        i += 1
    return -1


def pack_ready(cells, limits, max_bad_cells):
    avg = average_voltage(cells)
    bad_count = count_bad_cells(cells, limits)
    if 3.90 <= avg <= 4.05 and bad_count <= max_bad_cells:
        return True
    return False





