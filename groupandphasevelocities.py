import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dx = 0.01
dt = 0.005
N = 10000
k1 = 4
k2 = 6

def omega1(k1):
    return 0*k1 + 0

def omega2(k2):
    return 0*k2 + 3

v_phase1 = omega1(k1)/k1
v_phase2 = omega2(k2)/k2

#v_phase = (omega2(k2) + omega1(k1))/(k2+k1)
v_group = (omega2(k2) - omega1(k1))/(k2-k1)


xs = np.linspace(0, 10, N)
ts = np.linspace(0, 10, N)

fig, ax = plt.subplots()
plt.title("Phase and Group Velocity")
plt.xlabel("t")
plt.ylabel("y")
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)

line1, = ax.plot(ts, np.cos(k1*(xs)-omega1(k1)*(ts))+np.cos(k2*(xs)-omega2(k2)*(ts)), color='blue')
line2, = ax.plot(ts, 2*np.cos(((k2-k1)*(xs)-(omega2(k2)-omega1(k1))*(ts))/2), color='red', linestyle='dashed')
line3, = ax.plot(ts, -2*np.cos(((k2-k1)*(xs)-(omega2(k2)-omega1(k1))*(ts))/2), color='red', linestyle='dashed')
line4, = ax.plot(ts, np.cos(((k2+k1)*(xs)-(omega2(k2)+omega1(k1))*(ts))/2), color='green', linestyle='dashed')
#point1, = ax.plot(0, 2, color='red', marker='o', markersize=4)


def animate(i):
    t1 = i*dt
    x1 = i*dx
    line1.set_ydata(np.cos(k1*(xs+x1)-omega1(k1)*(ts+t1))+np.cos(k2*(xs+x1)-omega2(k2)*(ts+t1)))
    line2.set_ydata(2*np.cos(((k2-k1)*(xs+x1)-(omega2(k2)-omega1(k1))*(ts+t1))/2))
    line3.set_ydata(-2*np.cos(((k2-k1)*(xs+x1)-(omega2(k2)-omega1(k1))*(ts+t1))/2))
    line4.set_ydata(np.cos(((k2+k1)*(xs+x1)-(omega2(k2)+omega1(k1))*(ts+t1))/2))
    #point1.set_xdata(v_group*(x1+xs[i]))
    return line1, line2, line3, line4, #point1, 

ani = FuncAnimation(fig, animate, N, interval=20, blit=True)
plt.show()
