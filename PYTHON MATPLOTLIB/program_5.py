
# Pie Chart

import matplotlib.pyplot as plt

students = ["Shankar","Supriya","Santtosh","Akshay"]
percentage = [40, 30, 50, 35]

plt.pie(percentage,labels=students,autopct="%1.1f%%")
plt.title("Student's Percentage")

plt.show()