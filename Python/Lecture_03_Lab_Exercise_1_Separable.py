'''
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: May 26th, 2025
# Last Modification Date: May 27th, 2025
# Permissions and Citation: Refer to the README file.
'''

# Import necessary libraries.
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from sympy import symbols, Function, dsolve, solve


# Define the separable equation as a function to be used by the solver.
def SeparableEquation(x, y):
  return x * y


# Set the initial condition y(0) = 1 as a list.
x0 = 0
y0 = [1]

x = symbols("x")  # Define a symbol 't' for time or independent variable.
# Define a function 'y' that depends on 't'.
y = Function("y")(x)
# Define a constant of integration 'C1' for the solution.
C1 = symbols("C1")

# Define the separable differential.
separableEquation = y.diff(x) - x * y

# Solve the separable equation analytically using dsolve from sympy.
analyticalSolution = dsolve(separableEquation, y)

# Print the analytical solution to the console.
print("Analytical General Solution:", analyticalSolution)

# Solve the initial value problem using the analytical solution.
analyticalSolution = analyticalSolution.subs({y: y0[0]})

# Solve for the constant of integration C1 using the initial condition.
constValue = solve(analyticalSolution.rhs.subs(x, x0) - y0[0], C1)[0]

# Substitute the constant of integration C1 back into the analytical solution.
print("Value of Constant:", constValue)

# Create a specific solution by substituting the value of C1 into the analytical solution.
specificSolution = analyticalSolution.subs(C1, constValue)

# Print the analytical solution with the initial condition applied.
print("Analytical Specific Solution:", specificSolution)

# Generate 100 points between 0 and 2 for the analytical solution.
xAnalytical = np.linspace(0, 2, 100)
# Compute the analytical solution at the generated points.
yAnalytical = np.array([specificSolution.rhs.subs(x, val) for val in xAnalytical], dtype=float)

# Solve the ODE numerically over the interval [0, 2] using solve_ivp and store the solution.
sol = solve_ivp(
  SeparableEquation,  # The function to solve.
  [0, 2],  # The interval of integration.
  y0,  # Initial condition.
  t_eval=np.linspace(0, 2, 100),  # Points at which to store the computed solution.
)

# Plot the numerical solution as red dots.
plt.plot(sol.t, sol.y[0], "ro", label="Numerical Solution", markersize=4)
# Plot the analytical solution as a blue line.
plt.plot(xAnalytical, yAnalytical, label="Analytical Solution", color="blue", linewidth=1.5)

# Label the x-axis as 'x'.
plt.xlabel("x")
# Label the y-axis as 'y'.
plt.ylabel("y")
# Set the plot title.
plt.title("Solving Separable Equation: Analytical vs. Numerical.")
# Display the legend to distinguish between solutions.
plt.legend()
# Add a grid to the plot for better readability.
plt.grid()

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_03_Lab_Exercise_1_Separable.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
