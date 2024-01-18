import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def projectile_state_equation(t, X):
    # u[0] = x, u[1] = y, u[2] = vx, u[3] = vy
    x, y, vx , vy = X
    g = 9.8  

    # System of ODEs
    dxdt = vx
    dydt = vy
    dvxdt = 0
    dvydt = -g

    Xdot =  [dxdt, dydt, dvxdt, dvydt]
    return Xdot

# Generate random initial values
initial_velocity = 45
launch_angle = 75  # Random launch angle between 30 and 60 degrees
initial_height = 0
 # random.uniform(5, 15)  # Random initial height between 5 and 15 meters

# Convert launch angle to radians
launch_angle_rad = np.radians(launch_angle)

# Initial conditions
X0 = [0, initial_height, initial_velocity * np.cos(launch_angle_rad), initial_velocity * np.sin(launch_angle_rad)]

# Time span
t_span = (0, 2 * (initial_velocity) * np.sin(launch_angle_rad) / 9.8)  # Adjust time span based on the expected flight time

# Solve ODE using solve_ivp
solution = solve_ivp(projectile_state_equation, t_span, X0, t_eval=np.linspace(t_span[0], t_span[1], 1000), method='RK45')

# Plot the results
plt.plot(solution.y[0], solution.y[1])
plt.title('Projectile Motion using solve_ivp')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.show()
