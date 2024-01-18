#packages
import numpy as np
from scipy.integrate import odeint  # odeint --> Ordinary Differential Equation and Integration
import matplotlib.pyplot as plt

m = 1 #mass
k = 10 
c = 0.5 #dampingcoefficient
F = 0

def spring_mass(x, t):
    x1 = x[0] #position
    x2 = x[1] #velocity
    dx1dt = x2 # First derivative of position
    dx2dt = (F - c*x2 - k*x1)/m # Second derivative of position
    return [dx1dt, dx2dt]

t = np.linspace(0, 20, 101) # Time in seconds
x0 = [1, 0] # Initial position and velocity

# Solve the differential equation
x = odeint(spring_mass, x0, t)
x1 = x[:,0] # Position
x2 = x[:,1] # Velocity

plt.plot(t, x1) # plot
plt.xlabel('Time (s)') # label for X axis
plt.ylabel('Position (m)') # label for Y axis
plt.title('Spring Mass System') # title
plt.grid() # display Grid
plt.show() # Display output Terminal
