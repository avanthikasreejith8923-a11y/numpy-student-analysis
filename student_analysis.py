import numpy as np
print("NumPy version:", np.__version__)

# 10 students, 5 subjects
scores = np.array([
    [85, 90, 78, 92, 88],
    [70, 65, 80, 75, 72],
    [90, 95, 88, 97, 91],
    [55, 60, 58, 62, 50],
    [78, 82, 74, 85, 79],
    [92, 88, 95, 90, 94],
    [45, 50, 48, 55, 42],
    [88, 84, 90, 87, 85],
    [60, 65, 70, 68, 63],
    [75, 78, 72, 80, 76]
])

students = np.array(["Ava", "Binu", "Chinnu", "Divya", "Eshu",
                     "Fathima", "Gowri", "Hari", "Irfan", "Jishnu"])
subjects = np.array(["Maths", "Physics", "Chemistry", "CS", "English"])

student_avg = np.mean(scores, axis=1)
subject_avg = np.mean(scores, axis=0)
total_marks = np.sum(scores, axis=1)
std_per_student = np.std(scores, axis=1)
topper_index = np.argmax(total_marks)
weak_index = np.argmin(total_marks)
most_consistent = np.argmin(std_per_student)
p90 = np.percentile(scores, 90)
elite = students[student_avg >= p90]
passed = students[student_avg > 75]

print("="*40)
print("       STUDENT PERFORMANCE REPORT")
print("="*40)
for i in range(len(students)):
    print(f"{students[i]}: Avg={round(student_avg[i],2)} | Total={total_marks[i]} | Std={round(std_per_student[i],2)}")
print("="*40)
print(f"Topper: {students[topper_index]}")
print(f"Needs Improvement: {students[weak_index]}")
print(f"Most Consistent: {students[most_consistent]}")
print(f"90th Percentile Mark: {p90}")
print(f"Elite Students: {elite}")
print(f"Students above 75 avg: {passed}")
