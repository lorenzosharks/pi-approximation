import matplotlib.pyplot as plt
import random
import math

i=0
c=0
b=0

#set-up plot
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axis('equal')

#add circle
circle1 = plt.Circle((0, 0), 1, fill=False, edgecolor="red")
plt.gca().add_patch(circle1)

#add square
square_vertices = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)]
x, y = zip(*square_vertices)
plt.plot(x, y, 'b-')

#generate a random point
x = random.random() * 2 - 1
y = random.random() * 2 - 1

#plot the random point
for i in range(10000):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if (x**2)+(y**2)<1:
        plt.plot(x, y, 'bo')
        c=c+1
    elif (x**2)+(y**2)>1:
        plt.plot(x, y, 'ro')
        b=b+1
    elif (x**2)+(y**2)>1:
        plt.plot(x, y, 'go')
        b=b+1
a=c/b

#add text
text1 = plt.text(-1.1, 1.2, "Pi approximation: " + str(a))

#display plot
plt.show()