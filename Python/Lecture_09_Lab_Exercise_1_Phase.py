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
from scipy.integrate import solve_ivp


def System1D(t, state, params):
  # Function to compute the derivatives for a 1D system.
  x = state[0]  # Unpack the state variable.
  # Example: A simple cubic polynomial system.
  dxdt = -x * (x - 1) * (x + 1)  # Derivative of x.
  return [dxdt]


def System2D(t, state, params):
  #  Function to compute the derivatives for a 2D system.
  x, y = state  # Unpack the state variables.
  alpha, beta, gamma, delta = params  # Unpack the parameters.
  dxdt = alpha * x - beta * x * y  # Derivative of x.
  dydt = -gamma * y + delta * x * y  # Derivative of y.
  return [dxdt, dydt]


# Create a grid of initial conditions for 1D system.
xVals = np.linspace(-15, 15, 50)  # Range of x values for 1D system.
X = xVals

# Compute the vector field for 1D system.
U = np.zeros_like(X)  # Initialize velocity component for 1D system.
for i in range(X.shape[0]):
  state = [X[i]]  # Unpack the state variable for 1D system.
  derivatives = System1D(0, state, None)  # Compute the derivative.
  U[i] = derivatives[0]  # Store the derivative in U.

# Normalize the vector field for 1D system.
magnitude = np.sqrt(U ** 2 + 1)  # Magnitude for normalization.
UNormalized = U / magnitude  # Normalize the horizontal component.
V = 1.0 / magnitude  # Normalize the vertical component.

# Plot the vector field for 1D system.
plt.figure(figsize=(8, 6))
plt.quiver(X, np.zeros_like(X), UNormalized, V, color="b")  # Plot vector field using quiver.
plt.xlabel("x")
plt.ylabel("dx/dt")
plt.title("Phase Portrait for 1D System")

# Add trajectories for 1D system.
# Example initial conditions for 1D system.
initialConditions = [-2.5, 0.0, 2.5]
tSpan = (0, 25)  # Time span for integration for 1D system.
tEval = np.linspace(tSpan[0], tSpan[1], 1000)

# Loop through each initial condition for 1D system.
for ic in initialConditions:
  # Solve the system for each initial condition for 1D system.
  sol = solve_ivp(System1D, tSpan, [ic], args=((),), t_eval=tEval)
  # Plot the trajectory for 1D system.
  plt.plot(sol.t, sol.y[0], label=f"IC: {ic}")
  # Plot the starting point as star for 1D system.
  plt.plot(sol.t[0], sol.y[0][0], "r*", markersize=10)

plt.legend()  # Add legend for initial conditions for 1D system.
plt.grid()  # Add grid to the plot for 1D system.
plt.savefig("Lecture_09_Lab_Exercise_1_Phase1D.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot for 1D system.
plt.close()  # Close the plot to free memory for 1D system.

# Create a grid of initial conditions.
xVals = np.linspace(-10, 50, 100)  # Range of x values.
yVals = np.linspace(-10, 50, 100)  # Range of y values.
X, Y = np.meshgrid(xVals, yVals)  # Create a grid.

# Compute the vector field.
alpha = 1.0  # Parameter alpha.
beta = 0.1  # Parameter beta.
gamma = 1.0  # Parameter gamma.
delta = 0.05  # Parameter delta.
params = [alpha, beta, gamma, delta]  # Parameters for the system.
U, V = np.zeros_like(X), np.zeros_like(Y)  # Initialize velocity components.
for i in range(X.shape[0]):
  for j in range(X.shape[1]):
    state = [X[i, j], Y[i, j]]
    derivatives = System2D(0, state, params)
    U[i, j], V[i, j] = derivatives

# Plot the vector field.
plt.figure(figsize=(8, 6))
# plt.quiver(X, Y, U, V, color="b") # Plot vector field using quiver.
plt.streamplot(X, Y, U, V, color="b", density=1.5, linewidth=0.5, arrowsize=1.5)  # Plot vector field using streamplot.
plt.xlabel("x")
plt.ylabel("y")
plt.title("Phase Portrait")

# Add trajectories (optional).
# Example initial conditions.
initialConditions = [
  [0, 0],
  [10, 5],
  [20, 10],
  [15, 5],
  [15, 15],
]
tSpan = (0, 25)  # Time span for integration.
tEval = np.linspace(tSpan[0], tSpan[1], 500)

# Loop through each initial condition.
for ic in initialConditions:
  # Solve the system for each initial condition.
  sol = solve_ivp(System2D, tSpan, ic, args=(params,), t_eval=tEval)
  # Plot the trajectory.
  plt.plot(sol.y[0], sol.y[1], label=f"IC: {ic}")
  # Plot the starting point as star.
  plt.plot(sol.y[0][0], sol.y[1][0], "*", markersize=10, label=f"Start: {ic}")
  # Plot the end point as circle.
  plt.plot(sol.y[0][-1], sol.y[1][-1], "o", markersize=10, label=f"End: {ic}")

plt.legend()  # Add legend for initial conditions.
plt.grid()  # Add grid to the plot.
plt.savefig(" Lecture_09_Lab_Exercise_1_Phase2D.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
plt.close()  # Close the plot to free memory.
