'''
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: May 26th, 2025
# Last Modification Date: May 26th, 2025
# Permissions and Citation: Refer to the README file.
'''

# Import necessary libraries.
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from sympy import symbols, Function, dsolve, solve


# Define the logistic growth equation as a function to be used by the numerical solver.
def LogisticGrowth(t, P, r, K):
  return r * P * (1.0 - P / K)


# Set parameters for the logistic growth model.
r = 0.5  # Growth rate.
K = 100  # Carrying capacity.
P0 = [10]  # Initial population size.

# Define symbolic variables for analytical solution.
tSym = symbols("t")  # Independent variable (time).
P = Function("P")(tSym)  # Dependent variable (population size).
C1 = symbols("C1")  # Constant of integration.

# Define the logistic differential equation symbolically.
logisticEquation = P.diff(tSym) - r * P * (1 - P / K)

# Solve the logistic equation analytically using dsolve from sympy.
analyticalSolution = dsolve(logisticEquation, P)

# Print the general analytical solution.
print("Analytical General Solution:", analyticalSolution)

# Solve for the constant of integration C1 using the initial condition P(0) = P0.
initialCondition = analyticalSolution.subs({tSym: 0, P: P0[0]})
constValue = solve(initialCondition.rhs - P0[0], C1)[0]

# Print the value of the constant of integration C1.
print("Value of Constant:", constValue)

# Substitute the constant of integration C1 back into the analytical solution.
specificSolution = analyticalSolution.subs(C1, constValue)

# Print the specific analytical solution with the initial condition applied.
print("Analytical Specific Solution:", specificSolution)

# Generate 100 points between 0 and 20 for the analytical solution.
tAnalytical = np.linspace(0, 20, 100)
# Compute the analytical solution at the generated points.
PAnalytical = np.array([specificSolution.rhs.subs(tSym, val) for val in tAnalytical], dtype=float)

# Solve the ODE numerically over the interval [0, 20] using solve_ivp and store the solution.
sol = solve_ivp(
  LogisticGrowth,  # The function to solve.
  [0, 20],  # The interval of integration.
  P0,  # Initial condition.
  args=(r, K),  # Additional arguments for the function (r, K).
  t_eval=np.linspace(0, 20, 100),  # Points at which to store the computed solution.
)

# Plot the numerical solution as red dots.
plt.plot(sol.t, sol.y[0], "ro", label="Numerical Solution", markersize=4)
# Plot the analytical solution as a blue line.
plt.plot(tAnalytical, PAnalytical, label="Analytical Solution", color="blue", linewidth=1.5)

# Label the x-axis as 't'.
plt.xlabel("Time (t)")
# Label the y-axis as 'P'.
plt.ylabel("Population Size (P)")
# Set the plot title.
plt.title("Logistic Growth Model: Analytical vs. Numerical.")
# Display the legend to distinguish between solutions.
plt.legend()
# Add a grid to the plot for better readability.
plt.grid()

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_03_Lab_Exercise_2_Growth.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
