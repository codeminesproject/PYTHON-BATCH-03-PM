
import matplotlib.pyplot as plt

students = ["Shankar","Supriya","Santtosh","Akshay"]
percentage = [89.98,81.90,78.56,85.67]

plt.bar(students,percentage)
plt.xlabel("Percentage")
plt.ylabel("Students")
plt.title("Student's Percentage")

plt.show()