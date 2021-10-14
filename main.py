import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def f(x):
    n = 0
    while x != 1:
        
        if x % 2 == 0:
            x /= 2
        else:
            x = (3*x) + 1
        
        n += 1
        f = open("points.txt", "a")
        f.write(f"{str(n)}, {str(int(x))}\n")

x = int(input("Enter any positive integer: "))
f(x)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("points.txt", "r").read()
    dataArray = pullData.split("\n")
    xArr = []
    yArr = []
    for line in dataArray:
        if len(line) > 1:
            x,y = line.split(",")
            xArr.append(int(x))
            yArr.append(int(y))
    
    ax1.clear()
    ax1.plot(xArr, yArr, marker="o", markerfacecolor="grey", markersize="10")

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

