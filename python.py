
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y= []
for i in x:
    y.append(3*i+2)
# Line Chart
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Chart')
plt.show()
