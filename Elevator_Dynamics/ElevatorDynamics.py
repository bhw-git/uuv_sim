import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 1000  # mass of the elevator in kg
g = 9.81  # acc due to gravity in m/s^2
b = 100  # damping coefficient in kg/s

def elevator(y, t, T):
    x, v = y  # position and velocity
    a = (T - m*g - b*v) / m  # acceleration
    return [v, a]

t = np.linspace(0, 10, 1000)

y0 = [0, 0]

T = 11000

sol = odeint(elevator, y0, t, args=(T,))

plt.figure()
plt.plot(t, sol[:, 0],color = 'Orange')
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')
plt.title('Elevator position over time')
plt.grid()
plt.show()