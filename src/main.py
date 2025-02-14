import numpy as np
import matplotlib.pyplot as plt
import math


# --- Auxiliary constants ---
gravitational_acceleration = 9.81  # m/s²
pulley_radius = 0.02  # m
convert_rpm = 2 * math.pi / 60  # rad/s

# --- Experimental datas ---
electric_current = np.array([1, 2, 3, 4, 5, 6])
speed_RPM = np.array([1, 2, 3, 4, 5, 6])
angular_speed = speed_RPM * convert_rpm
mass = np.array([1, 2, 3, 4, 5, 6])
weight = mass * gravitational_acceleration
torque = weight * pulley_radius


# --- Function to plot ---
def plot_graph(x, y, xlabel, ylabel, title, color='blue', fit_degree=None):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color=color, marker='o')

    if fit_degree is not None:
        coef = np.polyfit(x, y, fit_degree)
        poly = np.poly1d(coef)
        x_fit = np.linspace(min(x), max(x), 100)
        plt.plot(x_fit, poly(x_fit), '--', color=color)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(alpha=0.5)
    plt.show()


# --- Graphs ---
plot_graph(electric_current, speed_RPM, "Electric Current [A]", "Speed [RPM]", "Speed vs Electric Current", 'blue',
           fit_degree=2)
plot_graph(electric_current, torque, "Electric Current [A]", "Torque [N m]", "Torque vs Electric Current", 'red',
           fit_degree=2)
plot_graph(torque, speed_RPM, "Torque [N m]", "Speed [RPM]", "Speed vs Torque", 'green',
           fit_degree=2)
plot_graph(weight, angular_speed, "Weight [kg]", "Angular Speed [rad/s]", "Angular Speed vs Weight", 'purple',
           fit_degree=2)
