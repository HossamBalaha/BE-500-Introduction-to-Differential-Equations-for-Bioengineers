"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: July 9th, 2025
# Last Modification Date: July 9th, 2025
# Permissions and Citation: Refer to the README file.
"""

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def HillEquation(x, beta=1.0, n=2, k=1.0, gamma=0.1):
  """
  Hill equation function.

  Parameters:
  x (float): The input variable.
  beta (float): Maximum response.
  n (int): Hill coefficient.
  k (float): Half-maximal effective concentration.
  gamma (float): Baseline response.

  Returns:
  float: The response of the Hill equation.
  """
  result = (beta * (x ** n) / (k ** n + x ** n)) - (gamma * x)
  return result


def HillEquationDerivative(t, x, beta=1.0, n=2, k=1.0, gamma=0.1):
  """
  Derivative of the Hill equation for use in ODE solvers.

  Parameters:
  t (float): Time variable (not used in this case).
  x (float): The input variable.
  beta (float): Maximum response.
  n (int): Hill coefficient.
  k (float): Half-maximal effective concentration.
  gamma (float): Baseline response.

  Returns:
  float: The derivative of the Hill equation.
  """
  num = beta * (x ** n)
  numDerivative = beta * n * (x ** (n - 1))
  den = k ** n + x ** n
  denDerivative = n * (x ** (n - 1))
  result = (numDerivative * den - num * denDerivative) / (den ** 2) - gamma
  return result


def RungeKutta4(f, x0, tSpan, dt):
  """
  Runge-Kutta 4th order method for solving ODEs.

  Parameters:
  f (function): The function representing the ODE.
  x0 (float): Initial condition.
  tSpan (tuple): Time span for the solution.
  dt (float): Time step size.

  Returns:
  tuple: Time points and corresponding solution values.
  """
  t = np.arange(tSpan[0], tSpan[1], dt)
  x = np.zeros(len(t))
  x[0] = x0

  for i in range(1, len(t)):
    k1 = f(x[i - 1]) * dt
    k2 = f(x[i - 1] + k1 / 2.0) * dt
    k3 = f(x[i - 1] + k2 / 2.0) * dt
    k4 = f(x[i - 1] + k3) * dt
    x[i] = x[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0

  return t, x


# Parameters.
beta = 1.0  # Maximum production rate.
n = 1  # Hill coefficient.
k = 1.0  # Half-maximal effective concentration.
gamma = 0.1  # Degradation/dilution rate.
x0 = 0.5  # Initial condition for the gene product concentration.
tSpan = (0, 50)  # Time span for the solution.
dt = 0.01  # Time step size.

# Solve using RK4.
f = lambda x: HillEquation(x, beta, n, k, gamma)
t, x = RungeKutta4(f, x0, tSpan, dt)
# Compute the response of the Hill equation.
dxValues = [HillEquation(xI, beta, n, k, gamma) for xI in x]

# Find the equilibrium points.
equilibriumPoints = []
for i in range(0, 100):
  equilibrium = fsolve(lambda x: HillEquation(x, beta, n, k, gamma), i)
  if ((equilibrium[0] >= 0) and (not any(np.isclose(equilibrium, e) for e in equilibriumPoints))):
    equilibriumPoints.append(equilibrium[0])

# Print the equilibrium points.
print("Equilibrium Points:", equilibriumPoints)

# Check stability of equilibria.
stability = []
for eq in equilibriumPoints:
  derivativeAtEq = HillEquationDerivative(0, eq, beta, n, k, gamma)
  if (derivativeAtEq < 0):
    stability.append((eq, "Stable"))
  elif (derivativeAtEq > 0):
    stability.append((eq, "Unstable"))
  else:
    stability.append((eq, "Neutral"))

# Print stability of equilibria.
print("Stability of Equilibria:")
for eq, status in stability:
  print(f"Equilibrium Point: {eq}, Stability: {status}")

plt.figure(figsize=(12, 8))  # Set the figure size for better visibility.

# Plot the results of the Hill equation solution and the RK4 method.
plt.subplot(2, 2, 1)
plt.plot(t, x, label="Gene Product Concentration", lw=2)
plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("Concentration (x)", fontsize=12)
plt.title(f"Solution of Hill Equation Using RK4 (n = {n} and k = {k})", fontsize=14)
plt.legend()  # Add legend for initial conditions.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

# Plot the response of the Hill equation derivative over time.
plt.subplot(2, 2, 2)
plt.plot(t, dxValues, label="Hill Equation Response", lw=2)
plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("Hill Equation Response (dx/dt)", fontsize=12)
plt.title(f"Response of Hill Equation Over Time (n = {n} and k = {k})", fontsize=14)
plt.legend()  # Add legend for response.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

# Plot the bifurcation diagram by changing the parameter k and n = 1.
n = 1  # Set n to 1 for the bifurcation diagram.
kValues = np.linspace(0.1, 15, 500)  # Range of k values from 0.1 to 5.0.
stable, unstable = [], []  # Lists to hold stable and unstable points.
for kValue in kValues:
  eqPoints = []
  for i in range(0, 100):
    sol = fsolve(lambda x: HillEquation(x, beta, n, kValue, gamma), i)
    if ((sol[0] >= 0) and (not any(np.isclose(sol, e) for e in eqPoints))):
      eqPoints.append(sol[0])
  if (eqPoints):
    for eq in eqPoints:
      derivativeAtEq = HillEquationDerivative(0, eq, beta, n, kValue, gamma)
      if (derivativeAtEq < 0):
        stable.append((kValue, eq))  # Append stable equilibrium points.
      elif (derivativeAtEq > 0):
        unstable.append((kValue, eq))  # Append unstable equilibrium points.

# Convert stable and unstable lists to numpy arrays for plotting.
stable = np.array(stable)
unstable = np.array(unstable)

# Plot the bifurcation diagram.
plt.subplot(2, 2, 3)
plt.plot(stable[:, 0], stable[:, 1], "b-", label="Stable", lw=2)
plt.plot(unstable[:, 0], unstable[:, 1], "r--", label="Unstable", lw=2)
plt.xlabel("Parameter (k)", fontsize=12)
plt.ylabel("Equilibrium Points (x)", fontsize=12)
plt.title("Bifurcation Diagram of Hill Equation (n = 1)", fontsize=14)
plt.legend()  # Add legend for bifurcation diagram.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

# Plot the bifurcation diagram by changing the parameter n.
k = 1.0  # Set k to 1 for the bifurcation diagram.
nValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Range of n values.
stableN, unstableN = [], []  # Lists to hold stable and unstable points.
for nValue in nValues:
  eqPoints = []
  for i in range(0, 100):
    sol = fsolve(lambda x: HillEquation(x, beta, nValue, k, gamma), i)
    if ((sol[0] >= 0) and (not any(np.isclose(sol, e) for e in eqPoints))):
      eqPoints.append(sol[0])
  if (eqPoints):
    for eq in eqPoints:
      derivativeAtEq = HillEquationDerivative(0, eq, beta, nValue, k, gamma)
      if (derivativeAtEq < 0):
        stableN.append((nValue, eq))  # Append stable equilibrium points.
      elif (derivativeAtEq > 0):
        unstableN.append((nValue, eq))  # Append unstable equilibrium points.

# Convert stable and unstable lists to numpy arrays for plotting.
stableN = np.array(stableN)
unstableN = np.array(unstableN)

# Plot the bifurcation diagram for n.
plt.subplot(2, 2, 4)
plt.plot(stableN[:, 0], stableN[:, 1], "b-", label="Stable", lw=2)
plt.plot(unstableN[:, 0], unstableN[:, 1], "r--", label="Unstable", lw=2)
plt.xlabel("Parameter (n)", fontsize=12)
plt.ylabel("Equilibrium Points (x)", fontsize=12)
plt.title("Bifurcation Diagram of Hill Equation (k = 1)", fontsize=14)
plt.legend()  # Add legend for bifurcation diagram.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

plt.savefig("Lecture_10_Lab_Exercise_1_Hill.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
plt.close()  # Close the plot to free memory.
