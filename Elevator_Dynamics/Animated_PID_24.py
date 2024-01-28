import numpy as np
from Elevator_animate28.elevator import sim_run

# Simulator Options
options = {}
options['FIG_SIZE'] = [7, 7] # [Width, Height]
options['PID_DEBUG'] = False

# Physics Options
options['GRAVITY'] = True
options['FRICTION'] = True
options['ELEVATOR_MASS'] = 1000
options['COUNTERWEIGHT_MASS'] = 1000
options['PEOPLE_MASS'] = 180

# Controller Options
options['CONTROLLER'] = True
options['START_LOC'] = 3
options['SET_POINT'] = 27
options['OUTPUT_GAIN'] = 2000


class PDController:
    def __init__(self, reference):
        self.r = reference
        self.integral = 0
        self.prev_time = 0
        self.prev_error = None
        self.output = 0
        self.windup = 5
        self.output_max = 2.5
        # Part of PID DEBUG
        self.output_data = np.array([[0, 0, 0, 0]])

    def run(self, x, t):
        kp = 2
        kd = 4
        ki = 0.4

        # Controller run time.
        if t - self.prev_time < 0.05:
            return self.output
        else:
            dt = t - self.prev_time
            self.prev_time = t

        err = self.r - x
        P_out = kp * err
        
        # INSERT CODE ABOVE
        I_out = 0
        self.integral += err * dt
        if self.integral > self.windup:
            self.integral = self.windup
        elif self.integral < -1 * self.windup:
            self.integral = -1 * self.windup
        I_out = self.integral  * ki


        # HINT: Use self.prev_error to store old
        # error values and dt for time difference.
        if self.prev_error != None:
            err_dot = (err - self.prev_error) / dt
            D_out = kd * err_dot
            self.prev_error = err
        else:
            D_out = 0
            # Set this to error.
            self.prev_error = err

        self.output = P_out + D_out + I_out

        if self.output > self.output_max:
            self.output = self.output_max
        elif self.output < self.output_max*-1:
            self.output = self.output_max*-1


        self.output_data = np.concatenate((self.output_data, \
            np.array([[t, P_out, I_out, D_out]])))

        return self.output

sim_run(options, PDController)