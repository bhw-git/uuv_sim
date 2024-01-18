import numpy as np
from scipy.integrate import ode, solve_ivp
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0
        self.previous_time = 0

    def compute(self, current_position, t):
        error = self.setpoint - current_position
        P = self.Kp * error
        #print(P)
        self.integral += error
        I = self.Ki * self.integral * 0.1
        
        delT = t - self.previous_time
        if(delT < 0.01):
            derivative = 0
        else:
            derivative = (error - self.prev_error)/delT
        
        D = self.Kd * derivative
        control_output = P + I + D
        # print(control_output)
        self.prev_error = error
        self.previous_time = t
        return control_output

def elevator_system(t, y, pid_controller):
    position = y[0]
    velocity = y[1]
    control_output = pid_controller.compute(position, t)
    #acceleration =(T - m*g - b*velocity) / m
    a_gravity = (m1 - m2) * g / (m1 + m2)
    #print(a_gravity)
    a_control = control_output * control_gain / (m1 + m2)
    # print(t, a_gravity)
    acceleration =  a_gravity + a_control
    dydt = [velocity, acceleration]
    return dydt

desired_floor = 3
initial_position = 30
initial_velocity = 0
Kp = 0.1 #0.2
Ki = 0
Kd = 1.6 #0.4
'''
Kp = 4
Ki =  0.000001
Kd =  0.0054 '''

control_gain = 2000
m1 = 1000
m2 = 1000
g = -9.81
#b = 100
T = 2000

pid_controller = PIDController(Kp, Ki, Kd, desired_floor)

t = np.arange(0, 35, 0.05)
initial_conditions = [initial_position, initial_velocity]

#ode.set_integrator('dopri5')
solution = solve_ivp(elevator_system, (t[0], t[-1]), initial_conditions, t_eval = t, args=(pid_controller,))

#print(solution)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False)

ax1.plot(solution.t, solution.y[0])
ax1.set_ylabel('Elevator Position')
ax1.set_title('Elevator Position and Acceleration over Time')
ax1.grid(True)

ax2.plot(t, solution.y[1], 'r')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Elevator Velocity')
ax2.grid(True)
# print(solution.t)
acc = np.diff(solution.y[1])/np.diff(solution.t)
ax3.plot(t[1:], acc, 'g')
ax3.set_xlabel('Time (seconds)')
ax3.set_ylabel('Elevator Acceleration')
ax3.grid(True)

plt.show()