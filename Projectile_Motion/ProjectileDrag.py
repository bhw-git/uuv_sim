import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def projectile_motion_with_drag(t, u, Cd, rho, A):
    # u[0] = x, u[1] = y, u[2] = vx, u[3] = vy

    # Constants
    g = 9.8  # Acceleration due to gravity (m/s^2)

    # Drag force components
    v = np.sqrt(u[2]**2 + u[3]**2)
    Fx_drag = -0.5 * Cd * rho * A * v * u[2] / np.sqrt(u[2]**2 + u[3]**2)
    Fy_drag = -0.5 * Cd * rho * A * v * u[3] / np.sqrt(u[2]**2 + u[3]**2)

    # System of ODEs
    dxdt = u[2]
    dydt = u[3]
    dvxdt = Fx_drag
    dvydt = -g + Fy_drag

    return [dxdt, dydt, dvxdt, dvydt]

# Generate random initial values
initial_velocity = 45  # Random initial velocity between 20 and 30 m/s
launch_angle = 75  # Random launch angle between 30 and 60 degrees
initial_height = 5  # Random initial height between 5 and 15 meters
Cd = 1.2  # Drag coefficient (for a sphere)
rho = 2.5  # Air density (kg/m^3)
A = 0.01  # Cross-sectional area (m^2)

# Convert launch angle to radians
launch_angle_rad = np.radians(launch_angle)

# Initial conditions
u0 = [0, initial_height, initial_velocity * np.cos(launch_angle_rad), initial_velocity * np.sin(launch_angle_rad)]

# Time span
t_span = (0, 2 * initial_velocity * np.sin(launch_angle_rad) / 9.8)  # Adjust time span based on the expected flight time

# Solve ODE using solve_ivp
solution = solve_ivp(projectile_motion_with_drag, t_span, u0, args=(Cd, rho, A),
                     t_eval=np.linspace(t_span[0], t_span[1], 1000), method='RK45')

# Plot the results
plt.plot(solution.y[0], solution.y[1])
plt.title('Projectile Motion with Drag using solve_ivp')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid(True)
plt.show()
