import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0

    def compute(self, current_position):
        error = self.setpoint - current_position
        P = self.Kp * error
        self.integral += error
        I = self.Ki * self.integral * 0.1
        derivative = (error - self.prev_error)/0.1
        D = self.Kd * derivative
        control_output = P + I + D
        self.prev_error = error
        return control_output

def elevator_system(y, t, pid_controller):
    position, velocity = y
    control_output = pid_controller.compute(position)
    #acceleration =(T - m*g - b*velocity) / m
    a_gravity = (m1 - m2) * g / (m1 + m2)
    a_control = control_output * control_gain / (m1 + m2) 
    acceleration =  a_gravity + a_control
    dydt = [velocity, acceleration]
    return dydt

desired_floor = 3
initial_position = 30
initial_velocity = 0

Kp = 3.0
Ki =  0 #0.1
Kd =  0.01
control_gain = 100
m1 = 1000
m2 = 900
g = -9.81
b = 100
T = 2000

pid_controller = PIDController(Kp, Ki, Kd, desired_floor)

t = np.arange(0, 50, 0.1)
initial_conditions = [initial_position, initial_velocity]


solution = odeint(elevator_system, initial_conditions, t, args=(pid_controller,))

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.plot(t, solution[:, 0])
ax1.set_ylabel('Elevator Position')
ax1.set_title('Elevator Position and Acceleration over Time')
ax1.grid(True)

ax2.plot(t, solution[:, 1], 'r')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Elevator Velocity')
ax2.grid(True)

plt.show()
