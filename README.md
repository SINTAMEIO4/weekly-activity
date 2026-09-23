# student_marks_list.py
# Stores and analyzes a student's marks in five subjects using a list

# --- Create list of marks ---
marks = [78, 85, 60, 92, 70]

# --- Display all marks ---
print("All marks:", marks)

# --- Total and average ---
total_marks = sum(marks)
average_mark = total_marks / len(marks)
print(f"Total Marks: {total_marks}")
print(f"Average Mark: {average_mark:.2f}")

# --- Highest and lowest ---
print(f"Highest Mark: {max(marks)}")
print(f"Lowest Mark: {min(marks)}")

# --- Modify third subject's mark (index 2) ---
marks[2] = 88
print("Updated marks:", marks)
