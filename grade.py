import matplotlib.pyplot as plt

# set style to a dark background
plt.style.use("dark_background")

# get student data from user input
num_students = 10
student_names = []
grades = []
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter score for student {i+1}: "))
    student_names.append(name)
    grades.append(score)

# create a dot graph of the grades
plt.scatter(student_names, grades, color="#f7dc6f")
plt.title("Student Grades", color="white")
plt.xlabel("Student Names", color="white")
plt.ylabel("Grade", color="white")
plt.tick_params(axis='both', colors='white')

# create a pie chart of the grade distribution
labels = ["A", "B", "C", "D", "F"]
grade_counts = [len([g for g in grades if g >= 90]),
                len([g for g in grades if g >= 80 and g < 90]),
                len([g for g in grades if g >= 70 and g < 80]),
                len([g for g in grades if g >= 60 and g < 70]),
                len([g for g in grades if g < 60])]
plt.figure()
plt.pie(grade_counts, labels=labels, autopct="%1.1f%%", colors=["#1abc9c", "#f1c40f", "#e67e22", "#e74c3c", "#c0392b"])
plt.title("Grade Distribution", color="white")
plt.legend(labels, loc="best", bbox_to_anchor=(0.9, 0.9), facecolor="#282828")
plt.show()
