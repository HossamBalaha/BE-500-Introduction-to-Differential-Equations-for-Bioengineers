"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Permissions and Citation: Refer to the README file.
"""

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D  # Import 3D plotting tools.


def FitzHughNagumo(z, epsilon=0.08, a=0.7, b=0.8, I=0.5):
  """
  FitzHugh-Nagumo Model for Neuron Dynamics.

  Parameters:
  z (array-like): State variables [v, w] where v is the membrane potential and w is the recovery variable.
  epsilon (float): Time scale separation parameter.
  a (float): Parameter for recovery variable.
  b (float): Parameter for recovery variable.
  I (float): External stimulus (current).

  Returns:
  np.array: Derivatives of the state variables [dv/dt, dw/dt].
  """
  v, w = z  # Unpack the state variables.
  dvdt = v - v ** 3 / 3 - w + I
  dwdt = epsilon * (v + a - b * w)
  return np.array([dvdt, dwdt])


def FitzHughNagumoDerivative(z, epsilon=0.08, a=0.7, b=0.8, I=0.5):
  """
  Derivative of the FitzHugh-Nagumo Model for Neuron Dynamics.

  Parameters:
  Returns:
  """
  v, w = z  # Unpack the state variables.
  # Compute the Jacobian matrix of the FitzHugh-Nagumo model.
  J = np.array([
    [1 - v ** 2, -1],  # Derivative of dv/dt with respect to v and w.
    [epsilon, -epsilon * b]  # Derivative of dw/dt with respect to v and w.
  ])
  return J


def RungeKutta4TwoDimensional(f, z0, tSpan, dt):
  """
  Runge-Kutta 4th order method for solving ODEs.

  Parameters:
  f (function): The function representing the ODE.
  z0 (float): Initial condition for the state variable (var1, var2, etc.).
  tSpan (tuple): Time span for the solution.
  dt (float): Time step size.

  Returns:
  tuple: Time points and corresponding solution values.
  """
  t = np.arange(tSpan[0], tSpan[1], dt)
  z = []  # Initialize an empty list to store the solution.
  z.append(np.array(z0))  # Append the initial condition.

  for i in range(1, len(t)):
    k1 = f(z[i - 1]) * dt
    k2 = f(z[i - 1] + k1 / 2.0) * dt
    k3 = f(z[i - 1] + k2 / 2.0) * dt
    k4 = f(z[i - 1] + k3) * dt
    zn = z[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    z.append(zn)  # Append the new state to the solution list.

  # Convert the list to a numpy array for easier manipulation.
  z = np.array(z)
  return t, z


# Parameters.
epsilon = 0.08  # Time scale separation.
a = 0.7  # Parameter for recovery variable.
b = 0.8  # Parameter for recovery variable.
I = 1.5  # External stimulus.
# I = 2.5  # External stimulus.

z0 = [1.0, 0.1]  # Initial conditions (v0, w0).
tSpan = (0, 100)  # Time span for the solution.
dt = 0.01  # Time step size.

# Solve using RK4.
f = lambda z: FitzHughNagumo(z, epsilon, a, b, I)  # Define the function for RK4.
t, z = RungeKutta4TwoDimensional(f, z0, tSpan, dt)
# Compute the response of the FitzHugh-Nagumo system.
dzValues = np.array([FitzHughNagumo(zI, epsilon, a, b, I) for zI in z])

# Find the equilibrium points.
equilibriumPoints = []
for i in range(0, 100):
  for j in range(0, 100):
    # Solve for equilibrium points using fsolve.
    # The equilibrium occurs when dx/dt = 0 and dy/dt = 0.
    # [i, j]: Initial guess for the equilibrium point.
    equilibrium = fsolve(lambda z: FitzHughNagumo(z, epsilon, a, b, I), [i, j])
    if (not any(np.isclose(equilibrium, e).all() for e in equilibriumPoints)):
      equilibriumPoints.append(equilibrium)

# Print the equilibrium points.
print("Equilibrium Points:", equilibriumPoints)

# Check stability of equilibria.
stability = []
for eq in equilibriumPoints:
  J = FitzHughNagumoDerivative(eq, epsilon, a, b, I)
  eigenvalues = np.linalg.eigvals(J)  # Compute eigenvalues of the Jacobian.
  if (np.all(eigenvalues < 0)):
    stability.append((eq, "Stable"))  # Stable equilibrium.
  elif (np.all(np.real(eigenvalues) == 0) and np.any(np.imag(eigenvalues) != 0)):
    stability.append((eq, "Periodic Behavior"))  # Periodic behavior.
  elif (np.any(eigenvalues > 0)):
    stability.append((eq, "Unstable"))
  else:
    # Saddle point or neutral stability.
    stability.append((eq, "Saddle Point (or Neutral)"))

  # Print stability of equilibria.
print("Stability of Equilibria:")
for eq, status in stability:
  print(f"Equilibrium Point: {eq}, Stability: {status}")

# Set the figure size for better visibility.
fig = plt.figure(figsize=(12, 8))

# Plot the results of the FitzHugh-Nagumo system using RK4.
plt.subplot(2, 2, 1)
plt.plot(t, z[:, 0], label="v", lw=2)
plt.plot(t, z[:, 1], label="w", lw=2)
plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("State Variables", fontsize=12)
plt.title(f"Solution of FitzHugh-Nagumo System Using RK4", fontsize=14)
plt.legend()  # Add legend for initial conditions.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

# Plot the response of the FitzHugh-Nagumo system over time.
plt.subplot(2, 2, 2)
plt.plot(t, dzValues[:, 0], label="dv/dt", lw=2)
plt.plot(t, dzValues[:, 1], label="dw/dt", lw=2)
plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("FitzHugh-Nagumo System Response", fontsize=12)
plt.title(f"Response of FitzHugh-Nagumo System Over Time", fontsize=14)
plt.legend()  # Add legend for response.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

# Plot the phase portrait and vector field of the FitzHugh-Nagumo system.
N = 100  # Number of points in the grid for vector field.
U, V = np.zeros((N, N)), np.zeros((N, N))  # Initialize velocity components for vector field.
xVals = np.linspace(-5, 5, N)  # Range of prey population values.
yVals = np.linspace(-5, 5, N)  # Range of predator population values.
X, Y = np.meshgrid(xVals, yVals)  # Create a grid of prey and predator populations.
for i in range(X.shape[0]):
  for j in range(X.shape[1]):
    state = [X[i, j], Y[i, j]]  # Current state (prey, predator).
    derivatives = FitzHughNagumo(state, epsilon, a, b, I)  # Compute derivatives.
    U[i, j], V[i, j] = derivatives  # Store the derivatives in U and V.

plt.subplot(2, 2, 3)
for initCond in [
  [1.0, 0.0],  # Initial condition 1.
  [2.0, 1.0],  # Initial condition 2.
  [3.0, 2.0],  # Initial condition 3.
]:
  # Solve the system for each initial condition.
  sol = solve_ivp(
    lambda t, z: FitzHughNagumo(z, epsilon, a, b, I),
    [0, 100],  # Time span for the solution.
    initCond,  # Initial condition.
    t_eval=np.linspace(0, 100, 200),
  )  # Solve the system using solve_ivp.
  # Plot the trajectory.
  plt.plot(sol.y[0], sol.y[1], label=f"IC: {initCond}", lw=2)  # Plot trajectory of the system.
  # Plot the starting point as star.
  plt.plot(sol.y[0][0], sol.y[1][0], "r*", markersize=10, label=f"Start Point: {initCond}")  # Starting point.
  # Plot the end point as circle.
  plt.plot(sol.y[0][-1], sol.y[1][-1], "go", markersize=10, label=f"End Point: {initCond}")  # End point.
plt.scatter(
  [eq[0] for eq in equilibriumPoints],
  [eq[1] for eq in equilibriumPoints],
  color="magenta",
  label="Equilibrium Points",
  s=10,
)  # Equilibrium points.
# Plot vector field using streamplot.
plt.streamplot(X, Y, U, V, color="b", density=1.5, linewidth=0.5, arrowsize=1.5)  # Vector field.
plt.xlabel("v", fontsize=12)
plt.ylabel("w", fontsize=12)
plt.title(f"Phase Portrait of FitzHugh-Nagumo System", fontsize=14)
plt.legend()  # Add legend for phase portrait.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

# Plot the bifurcation diagram by changing the parameter external stimulus I.
extValues = np.linspace(0.0, 2.5, 10)  # Range of I values for bifurcation analysis.
stable, unstable = [], []  # Lists to hold stable and unstable points.
for extValue in extValues:
  eqPoints = []
  for i in range(0, 100):
    for j in range(0, 100):
      # Solve for equilibrium points using fsolve.
      equilibrium = fsolve(lambda z: FitzHughNagumo(z, epsilon, a, b, extValue), [i, j])
      if (
        # (equilibrium[0] >= 0) and
        # (equilibrium[1] >= 0) and
        (not any(np.isclose(equilibrium, e).all() for e in eqPoints))
      ):
        eqPoints.append(equilibrium)
  if (eqPoints):
    for eq in eqPoints:
      J = FitzHughNagumoDerivative(eq, epsilon, a, b, extValue)
      eigenvalues = np.linalg.eigvals(J)  # Compute eigenvalues of the Jacobian.
      if (np.all(eigenvalues < 0)):
        stable.append((extValue, eq[0], eq[1]))  # Append stable equilibrium points.
      elif (np.any(eigenvalues > 0)):
        unstable.append((extValue, eq[0], eq[1]))  # Append unstable equilibrium points.

# Convert stable and unstable lists to numpy arrays for plotting.
stable = np.array(stable)
unstable = np.array(unstable)

# Plot the bifurcation diagram as 3D line plots.
ax = fig.add_subplot(2, 2, 4, projection="3d")
# ax.plot3D(stable[:, 0], stable[:, 1], stable[:, 2], "b-", label="Stable", lw=2)  # Stable points.
# ax.plot3D(unstable[:, 0], unstable[:, 1], unstable[:, 2], "r--", label="Unstable", lw=2)  # Unstable points.
# Plot points as scatter for better visibility.
ax.scatter(stable[:, 0], stable[:, 1], stable[:, 2], c="b", marker="o", s=20, label="Stable Points")
ax.scatter(unstable[:, 0], unstable[:, 1], unstable[:, 2], c="r", marker="x", s=20, label="Unstable Points")
ax.set_xlabel("Parameter (I)", fontsize=12)  # X-axis label.
ax.set_ylabel("v", fontsize=12)  # Y-axis label.
ax.set_zlabel("w", fontsize=12)  # Z-axis label.
ax.set_title("Bifurcation Diagram by Varying I", fontsize=14)  # Title.
ax.legend()  # Add legend for bifurcation diagram.
plt.grid()  # Add grid to the plot.
plt.tight_layout()  # Adjust layout to prevent overlap.

plt.savefig("Lecture_10_Lab_Exercise_2_FHN.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
plt.close()  # Close the plot to free memory.
