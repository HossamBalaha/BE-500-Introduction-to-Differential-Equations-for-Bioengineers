'''
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 10th, 2025
# Last Modification Date: June 10th, 2025
# Permissions and Citation: Refer to the README file.
'''

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def KneeModel(t, y, c, k, F0=0.0, omegaF=0.0):
  """
  Defines the system of ordinary differential equations (ODEs) for the knee model.

  Parameters:
  t (float): Time variable.
  y (list): List containing the state variables [x, v].
  c (float): Damping coefficient.
  k (float): Spring constant.
  F0 (float): Amplitude of the forcing function (default is 0).
  omegaF (float): Frequency of the forcing function (default is 0).

  Returns:
  list: Derivatives [dx/dt, dv/dt].
  """
  x, v = y  # Unpack the state variables.
  # Derivative of displacement is velocity.
  dxdt = v
  # Derivative of velocity is given by the equation of motion.
  dvdt = -c * v - k * x + F0 * np.cos(omegaF * t)
  return [dxdt, dvdt]


m = 1.0  # Mass of the knee joint.
c = 0.5  # Damping coefficient.
k = 4.0  # Spring constant.
F0 = 2.0  # Forcing amplitude.
omega0 = 3  # Natural frequency of the system.
y0 = [0.1, 0.0]  # Initial displacement and velocity.
tSpan = (0, 50)  # Time span for the simulation.
# Create a time vector for plotting.
tEval = np.linspace(*tSpan, 2500)

# ==============================================================
# ==================== Analytical Solution =====================
# ==============================================================
partA = np.exp(-0.25 * tEval) * (0.467 * np.cos(1.984 * tEval) - 0.107 * np.sin(1.984 * tEval))
partB = -0.367 * np.cos(3 * tEval) + 0.11 * np.sin(3 * tEval)
analyticalSolution = partA + partB  # Combine the parts to get the analytical solution.

# ==============================================================
# ===================== Numerical Solution =====================
# ==============================================================
numericalSolution = solve_ivp(
  lambda t, y: KneeModel(
    t,  # Unpack the time.
    y,  # Unpack the state variables.
    c,  # Damping coefficient.
    k,  # Spring constant.
    F0=F0,  # Forcing amplitude.
    omegaF=omega0,  # Forcing frequency.
  ),
  tSpan,  # Time span for the simulation.
  y0,  # Initial conditions for the oscillation.
  t_eval=tEval,  # Time points at which to store the computed solution.
)
# ==============================================================

# Create a figure for the plot with specified size.
plt.figure(figsize=(10, 6))

# Plot the analytical solution.
plt.plot(tEval, analyticalSolution, label="Analytical Solution", linewidth=2, color="black")
plt.plot(
  numericalSolution.t, numericalSolution.y[0],
  label="Numerical Solution", linewidth=2, color="red", linestyle="--"
)

plt.xlabel("Time (t)")  # Label the x-axis as time.
plt.ylabel("Displacement x(t)")  # Label the y-axis as displacement.
plt.grid(True)  # Enable the grid for better readability.
plt.legend()  # Show the legend on the plot.
plt.tight_layout()  # Adjust the layout to prevent overlap of labels and titles.
plt.title("Knee Model: Analytical vs Numerical Solution")  # Set the title of the plot.

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_05_Lab_Exercise_1_Knee.png", dpi=300, bbox_inches="tight")

# Display the plot.
plt.show()
