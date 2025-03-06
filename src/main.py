import numpy as np
import matplotlib.pyplot as plt
import math

# --- Auxiliary constants ---
gravitational_acceleration = 9.81  # m/s²
pulley_radius = 0.02  # m
convert_rpm = 2 * math.pi / 60  # rad/s

# --- Experimental datas ---
electric_current = np.array([48, 103, 154, 217, 321])
speed_RPM = np.array([0, 0, 161, 213, 317])
angular_speed = speed_RPM * convert_rpm
mass = np.array([1, 2, 3, 4, 5])
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


# --- Fuction to plot speed vs current
def plot_speed_vs_current(current, speed, start_current):
    plt.figure(figsize=(10, 6))

    # Separar os dados em duas regiões
    current_working = current[current >= start_current]
    speed_working = speed[current >= start_current]

    # Plotar dados experimentais
    plt.scatter(current, speed, color='blue', marker='o', label='Dados Experimentais')

    # Ajustar uma função linear para a região onde o motor está funcionando
    if len(current_working) > 1:
        coef = np.polyfit(current_working, speed_working, 1)  # Ajuste linear
        poly = np.poly1d(coef)
        x_fit = np.linspace(min(current_working), max(current), 100)
        plt.plot(x_fit, poly(x_fit), '--', color='blue', label='Ajuste Linear')

    # Adicionar linha vertical para indicar o ponto de partida
    plt.axvline(x=start_current, color='red', linestyle=':', label=f'Corrente de Partida (~{start_current} mA)')

    # Configurações do gráfico
    plt.xlabel("Corrente Elétrica [mA]")
    plt.ylabel("Velocidade [RPM]")
    plt.title("Velocidade vs Corrente Elétrica")
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()


# --- Graphs ---
start_current = 154  # mA (valor aproximado onde o motor começaria a girar)
plot_speed_vs_current(electric_current, speed_RPM, start_current)
plot_graph(electric_current, torque, "Corrente Elétrica [A]", "Torque [N m]", "Torque vs Corrente Elétrica", 'red',
           fit_degree=2)
plot_graph(torque, speed_RPM, "Torque [N m]", "Velocidade [RPM]", "Velocidade vs Torque", 'green',
           fit_degree=2)
plot_graph(weight, angular_speed, "Peso [kg]", "Velocidade Angular [rad/s]", "Velocidade Angular vs Peso", 'purple',
           fit_degree=2)
