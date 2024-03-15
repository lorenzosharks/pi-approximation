import matplotlib.pyplot as plt
import random
import math

i=0
c=0
b=0

d=float(input("Size of the graph and circle (Larger radius = more accuracy): "))
accuracy=int(input("Number of points generated (More points equals more accuracy): "))

#set-up plot
plt.xlim(-d, d)
plt.ylim(-d, d)
plt.axis('equal')

#add circle
circle1 = plt.Circle((0, 0), d, fill=False, edgecolor="red")
plt.gca().add_patch(circle1)

#add square
square_vertices = [(-d, -d), (-d, d), (d, d), (d, -d), (-d, -d)]
x, y = zip(*square_vertices)
plt.plot(x, y, 'b-')

#plot the random point
for i in range(accuracy):
    x = random.random() * 2 * d - d
    y = random.random() * 2 * d - d
    if (x**2)+(y**2)<(d**2):
        plt.plot(x, y, 'bo')
        c=c+1
    elif (x**2)+(y**2)>(d**2):
        plt.plot(x, y, 'ro')
        b=b+1
a=(4*c)/(b+c)

#add text
text1 = plt.text(-1.1, d+0.2, "Pi approximation: " + str(a))

#display plot
plt.show()