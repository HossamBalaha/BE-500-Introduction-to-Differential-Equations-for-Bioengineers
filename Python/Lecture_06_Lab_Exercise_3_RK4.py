"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 17th, 2025
# Last Modification Date: June 18th, 2025
# Permissions and Citation: Refer to the README file.
"""

# Import necessary libraries.
import numpy as np
import prettytable as pt
import matplotlib.pyplot as plt


def EulerMethod(C0, k, h, tSpan):
  """
  Implements Euler's method for solving the ordinary differential equation
  representing drug elimination from the body.

  Parameters:
  C0 (float): Initial concentration of the drug in mg/L.
  k (float): Rate constant for drug elimination in 1/h.
  h (float): Time step for Euler's method in hours.
  tSpan (tuple): Time span for the simulation as (start time, end time).

  Returns:
  tEuler (numpy.ndarray): Time vector for Euler's method.
  CEuler (numpy.ndarray): Concentration values calculated using Euler's method.
  """
  # Time vector.
  tEuler = np.arange(*tSpan, h)
  CEuler = np.zeros(len(tEuler))
  CEuler[0] = C0

  # Apply Euler's method.
  for i in range(len(tEuler) - 1):
    CEuler[i + 1] = CEuler[i] + h * (-k * CEuler[i])

  return tEuler, CEuler


def ImprovedEulerMethod(C0, k, h, tSpan):
  """
  Implements the Improved Euler's method (Heun's method) for solving the
  ordinary differential equation representing drug elimination from the body.

  Parameters:
  C0 (float): Initial concentration of the drug in mg/L.
  k (float): Rate constant for drug elimination in 1/h.
  h (float): Time step for Improved Euler's method in hours.
  tSpan (tuple): Time span for the simulation as (start time, end time).

  Returns:
  tImprovedEuler (numpy.ndarray): Time vector for Improved Euler's method.
  CImprovedEuler (numpy.ndarray): Concentration values calculated using Improved Euler's method.
  """
  # Time vector.
  tImprovedEuler = np.arange(*tSpan, h)
  CImprovedEuler = np.zeros(len(tImprovedEuler))
  CImprovedEuler[0] = C0

  # Apply Improved Euler's method (Heun's method).
  for i in range(len(tImprovedEuler) - 1):
    # Calculate the slope at the beginning of the interval.
    slope1 = -k * CImprovedEuler[i]
    # Predict the next value using Euler's method.
    CPredict = CImprovedEuler[i] + h * slope1
    # Calculate the slope at the predicted value.
    slope2 = -k * CPredict
    # Average the slopes to get a better estimate.
    CImprovedEuler[i + 1] = CImprovedEuler[i] + (h / 2.0) * (slope1 + slope2)

  return tImprovedEuler, CImprovedEuler


def RungeKutta4(C0, k, h, tSpan):
  """
  Implements the Runge-Kutta 4th order method for solving the ordinary differential equation
  representing drug elimination from the body.

  Parameters:
  C0 (float): Initial concentration of the drug in mg/L.
  k (float): Rate constant for drug elimination in 1/h.
  h (float): Time step for Runge-Kutta method in hours.
  tSpan (tuple): Time span for the simulation as (start time, end time).

  Returns:
  tRK4 (numpy.ndarray): Time vector for Runge-Kutta method.
  CRK4 (numpy.ndarray): Concentration values calculated using Runge-Kutta method.
  """
  # Time vector.
  tRK4 = np.arange(*tSpan, h)
  CRK4 = np.zeros(len(tRK4))
  CRK4[0] = C0

  # Apply Runge-Kutta method.
  for i in range(len(tRK4) - 1):
    k1 = -k * CRK4[i]
    k2 = -k * (CRK4[i] + h / 2.0 * k1)
    k3 = -k * (CRK4[i] + h / 2.0 * k2)
    k4 = -k * (CRK4[i] + h * k3)
    CRK4[i + 1] = CRK4[i] + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

  return tRK4, CRK4


# Parameters.
C0 = 100  # Initial concentration in mg/L.
k = 0.2  # Rate constant in 1/h.
h = 1  # Time step for Euler's method.
tSpan = (0, 6)  # Time span for the simulation (exclusive of the end time).

# Numerical solution using Euler's method.
# Call the Euler's method function to get the time vector and concentration values.
tEuler, CEuler = EulerMethod(C0, k, h, tSpan)

# Numerical solution using Improved Euler's method.
# Call the Improved Euler's method function to get the time vector and concentration values.
tImprovedEuler, CImprovedEuler = ImprovedEulerMethod(C0, k, h, tSpan)

# Numerical solution using Runge-Kutta 4th order method.
# Call the Runge-Kutta 4th order method function to get the time vector and concentration values.
tRK4, CRK4 = RungeKutta4(C0, k, h, tSpan)

# Print the parameters used in the simulation.
tExact = np.linspace(tSpan[0], tSpan[1] - h, 100)
CExact = C0 * np.exp(-k * tExact)

# Calculate absolute error between RK4 method and the exact solution.
absError = np.abs(CRK4 - np.interp(tRK4, tExact, CExact))

# Print the parameters used in the simulation.
print(f"Parameters used in the simulation:")
print(f"Initial concentration (C0): {C0} mg/L")
print(f"Rate constant (k): {k} 1/h")
print(f"Time step (h): {h} hours")
print(f"Time span: {tSpan[0]} to {tSpan[1] - h} hours")

# Create a table to display the results.
table = pt.PrettyTable()
table.field_names = ["Time", "Euler's", "Improved Euler's", "RK4", "Exact", "Absolute Error"]
for t, euler, impEuler, rk4, error in zip(tEuler, CEuler, CImprovedEuler, CRK4, absError):
  exact = np.interp(t, tExact, CExact)  # Interpolate exact solution at time t.
  table.add_row([f"{t:.3f}", f"{euler:.3f}", f"{impEuler:.3f}", f"{rk4:.3f}", f"{exact:.3f}", f"{error:.3f}"])
print(table)

# Plot the results.
plt.plot(tExact, CExact, "r-", label="Exact Solution")
plt.plot(tEuler, CEuler, "bo-", label="Euler's Method")
plt.plot(tImprovedEuler, CImprovedEuler, "go-", label="Improved Euler's Method")
plt.plot(tRK4, CRK4, "mo-", label="Runge-Kutta 4th Order Method")
plt.xlabel("Time (hours).")
plt.ylabel("Drug Concentration (mg/L).")
plt.title("Numerical vs Exact Solutions for Drug Elimination.")
plt.grid(True)  # Enable the grid for better readability.
plt.legend()  # Show the legend on the plot.
plt.tight_layout()  # Adjust the layout to prevent overlap of labels and titles.

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_06_Lab_Exercise_3_RK4.png", dpi=300, bbox_inches="tight")

# Display the plot.
plt.show()
