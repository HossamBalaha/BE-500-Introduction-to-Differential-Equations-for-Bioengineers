'''
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 2nd, 2025
# Last Modification Date: June 2nd, 2025
# Permissions and Citation: Refer to the README file.
'''

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def HeartOscillations(t, y, omega0, gamma, F0=0.0, omegaF=0.0):
  """
  Defines the system of ordinary differential equations (ODEs) for the heart oscillations.

  Parameters:
  t (float): Time variable.
  y (list): List containing the state variables [x, v].
  omega0 (float): Natural frequency.
  gamma (float): Damping coefficient.
  F0 (float): Amplitude of the forcing function (default is 0).
  omegaF (float): Frequency of the forcing function (default is 0).

  Returns:
  list: Derivatives [dx/dt, dv/dt].
  """
  x, v = y  # Unpack the state variables.
  # Derivative of displacement is velocity.
  dxdt = v
  # Derivative of velocity is acceleration with damping and forcing term.
  dvdt = -2 * gamma * v - omega0 ** 2 * x + F0 * np.cos(omegaF * t)
  return [dxdt, dvdt]


omega0 = 2 * np.pi  # Natural frequency (1 Hz).
y0 = [1.0, 0.0]  # Initial displacement and velocity.
tSpan = (0, 20)  # Time span for the simulation.
# Create a time vector for plotting.
tEval = np.linspace(*tSpan, 1000)
colors = ["gray", "green", "red", "orange", "purple"]  # Colors for plotting.

# Set the parameters for different oscillation types.
valuesDict = {
  "Undamped"          : {"Gamma": 0.0, "F0": 0.0, "OmegaF": 0.0},
  "Underdamped"       : {"Gamma": 0.5, "F0": 0.0, "OmegaF": 0.0},
  "Critically Damped" : {"Gamma": 2 * np.pi, "F0": 0.0, "OmegaF": 0.0},
  "Overdamped"        : {"Gamma": 3 * np.pi, "F0": 0.0, "OmegaF": 0.0},
  "Forced Oscillation": {"Gamma": 0.5, "F0": 1.0, "OmegaF": 2 * np.pi},
}

# ==============================================================
# ========= Analytical Solutions for the Oscillations ==========
# ==============================================================
# Find the analytical solution for the undamped case.
# Calculate the analytical solution for undamped oscillation.
A = y0[0]  # Initial displacement.
B = y0[1] / omega0  # Initial velocity scaled by natural frequency.
xUndamped = A * np.cos(omega0 * tEval) + B * np.sin(omega0 * tEval)

# Find the analytical solution for the underdamped case.
# Calculate the damped natural frequency.
omegad = np.sqrt(omega0 ** 2 - valuesDict["Underdamped"]["Gamma"] ** 2)
# Calculate the analytical solution for underdamped oscillation.
A = y0[0]  # Initial displacement.
B = y0[1] * omegad  # Initial velocity scaled by damped frequency.
xUnderdamped = (
  np.exp(-valuesDict["Underdamped"]["Gamma"] * tEval) *
  (A * np.cos(omegad * tEval) + B * np.sin(omegad * tEval))
)

# Find the analytical solution for the critically damped case.
# Calculate the analytical solution for critically damped oscillation.
A = y0[0]  # Initial displacement.
B = y0[1] / valuesDict["Critically Damped"]["Gamma"]  # Initial velocity scaled by damping coefficient.
xCritically = (A + B * tEval) * np.exp(-valuesDict["Critically Damped"]["Gamma"] * tEval)

# Find the analytical solution for the overdamped case.
# Calculate the roots of the characteristic equation.
r1 = -valuesDict["Overdamped"]["Gamma"] + np.sqrt(valuesDict["Overdamped"]["Gamma"] ** 2 - omega0 ** 2)
r2 = -valuesDict["Overdamped"]["Gamma"] - np.sqrt(valuesDict["Overdamped"]["Gamma"] ** 2 - omega0 ** 2)
# Calculate the analytical solution for overdamped oscillation.
A = y0[0]  # Initial displacement.
B = y0[1] / (r2 - r1)  # Initial velocity scaled by the difference of the roots.
xOverdamped = A * np.exp(r1 * tEval) + B * np.exp(r2 * tEval)

# ==============================================================
# ========== Numerical Solutions for the Oscillations ==========
# ==============================================================
# Solve the ODE for the different oscillation types.
solutions = {}
for key, params in valuesDict.items():
  sol = solve_ivp(
    lambda t, y: HeartOscillations(
      t,  # Unpack the time .
      y,  # Unpack the state variables.
      omega0,  # Natural frequency.
      params["Gamma"],  # Damping coefficient.
      F0=params["F0"],  # Forcing amplitude.
      omegaF=params["OmegaF"],  # Forcing frequency.
    ),
    tSpan,  # Time span for the simulation.
    y0,  # Initial conditions for the oscillation.
    t_eval=tEval,  # Time points at which to store the computed solution.
  )
  solutions[key] = sol
# ==============================================================

# Plot the results for each oscillation type.
plt.figure(figsize=(16, 8))

plt.subplot(1, 2, 1)  # Create a subplot for the first part of the plot.

# Plot the analytical solution for undamped oscillation.
plt.plot(tEval, xUndamped, label="Undamped", linewidth=2, color=colors[0])
# Plot the analytical solution for underdamped oscillation.
plt.plot(tEval, xUnderdamped, label="Underdamped", linewidth=2, color=colors[1])
# Plot the analytical solution for critically damped oscillation.
plt.plot(tEval, xCritically, label="Critically Damped", linewidth=2, color=colors[2])
# Plot the analytical solution for overdamped oscillation.
plt.plot(tEval, xOverdamped, label="Overdamped", linewidth=2, color=colors[3])

plt.xlabel("Time (t)")  # Label the x-axis as time.
plt.ylabel("Displacement x(t)")  # Label the y-axis as displacement.
plt.grid(True)  # Enable the grid for better readability.
plt.legend()  # Show the legend on the plot.
plt.tight_layout()  # Adjust the layout to prevent overlap of labels and titles.
plt.title("Oscillations of the Heart (Analytical Solution)")  # Set the title for the plot.

plt.subplot(1, 2, 2)  # Create a subplot for the second part of the plot.

# Plot the numerical solutions for each oscillation type.
for i, (key, sol) in enumerate(solutions.items()):
  # Plot the displacement over time for each oscillation type.
  plt.plot(sol.t, sol.y[0], label=key, linewidth=2, color=colors[i])

plt.xlabel("Time (t)")  # Label the x-axis as time.
plt.ylabel("Displacement x(t)")  # Label the y-axis as displacement.
plt.grid(True)  # Enable the grid for better readability.
plt.legend()  # Show the legend on the plot.
plt.tight_layout()  # Adjust the layout to prevent overlap of labels and titles.
plt.title("Oscillations of the Heart (Numerical Solutions)")  # Set the title for the plot.

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_04_Lab_Exercise_3_Heart.png", dpi=300, bbox_inches="tight")

# Display the plot.
plt.show()
