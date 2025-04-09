import matplotlib.pyplot as plt

student_name = ["Aryan", "Aarav", "Ayaan", "Anaya", "Aarvi"]
marks = [90, 85, 95, 88, 92]


plt.plot(student_name, marks, marker='o', color='b', linestyle='dotted')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.title('Student Marks')
plt.show()