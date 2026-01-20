'''
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Permissions and Citation: Refer to the README file.
'''

# Import necessary libraries.
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from sympy import symbols, Function, dsolve, solve


# Define the separable equation as a function to be used by the solver.
# Inputs: x (float) independent variable, y (float) dependent variable
# Output: dy/dx = x * y (float)
def SeparableEquation(x, y):
  return x * y


# Set the initial condition y(0) = 1 as a list.
# Using a list matches the signature expected by solve_ivp for vector-valued y.
x0 = 0
y0 = [1]

# Define symbolic variable for analytical solution steps.
# Used only for deriving and demonstrating the closed-form solution.
x = symbols("x")  # Define a symbol 'x' for independent variable.
# Define a function 'y' that depends on 'x'.
y = Function("y")(x)
# Define a constant of integration 'C1' for the solution.
C1 = symbols("C1")

# Define the separable differential symbolic expression (dy/dx - x*y = 0).
# This expression is passed to sympy.dsolve to compute the general solution symbolically.
separableEquation = y.diff(x) - x * y

# Solve the separable equation analytically using dsolve from sympy.
# `dsolve` returns a general solution containing the integration constant C1.
analyticalSolution = dsolve(separableEquation, y)

# This block is added to handle cases where the solution might be a list.
# For example, dy/dx = x/y can have multiple solutions; show options when present.
if (isinstance(analyticalSolution, list)):
  print("Analytical Solution is a list, please pick one of the solutions.")
  print("Length of Analytical Solution:", len(analyticalSolution))
  # Print each solution with its index.
  for i, sol in enumerate(analyticalSolution):
    print(f"Solution {i + 1}:", sol)
  # Prompt the user to select a solution if multiple solutions exist.
  selection = input("Select the solution number (1 or 2): ")
  if (selection.isdigit()):
    selection = int(selection) - 1  # Convert to zero-based index.
  else:
    print("Invalid selection, defaulting to the first solution.")
    selection = 0
  # Select the chosen solution based on user input.
  analyticalSolution = analyticalSolution[selection]

# Print the analytical solution to the console.
print("Analytical General Solution:", analyticalSolution)

# Apply the initial condition symbolically to determine the constant of integration.
# `subs` applies the initial condition and `solve` isolates C1.
analyticalSolution = analyticalSolution.subs({y: y0[0]})
constValue = solve(analyticalSolution.rhs.subs(x, x0) - y0[0], C1)[0]

# Substitute the constant of integration C1 back into the analytical solution
# to obtain the specific solution matching the initial condition.
print("Value of Constant:", constValue)
specificSolution = analyticalSolution.subs(C1, constValue)

# Print the analytical solution with the initial condition applied for verification.
print("Analytical Specific Solution:", specificSolution)

# Generate points where both the analytical and numerical solutions will be evaluated.
# Choosing 100 points provides a smooth curve for plotting between 0 and 2.
xAnalytical = np.linspace(0, 2, 100)
# Evaluate the symbolic analytical solution on the numeric grid (convert to float array).
yAnalytical = np.array([specificSolution.rhs.subs(x, val) for val in xAnalytical], dtype=float)

# Solve the ODE numerically over the interval [0, 2] using SciPy's solve_ivp.
# We use `t_eval` to get values at the same points used for plotting the analytical solution.
sol = solve_ivp(
  SeparableEquation,  # The function to solve (callable f(t, y)).
  [0, 2],  # The interval of integration [t0, tf].
  y0,  # Initial condition as a list for compatibility with vector-valued solvers.
  t_eval=np.linspace(0, 2, 100),  # Time points at which to store the computed solution.
)

# Plot the numerical solution points (red circles) to illustrate discrete solver output.
plt.plot(sol.t, sol.y[0], "ro", label="Numerical Solution", markersize=4)
# Plot the continuous analytical solution (blue line) for comparison.
plt.plot(xAnalytical, yAnalytical, label="Analytical Solution", color="blue", linewidth=1.5)

# Label the axes and add title and legend to make the figure self-contained.
plt.xlabel("x")
# Label the y-axis as 'y'.
plt.ylabel("y")
plt.title("Solving Separable Equation: Analytical vs. Numerical.")
plt.legend()
plt.grid()

# Save the figure: PNG at high resolution suitable for lecture slides.
plt.savefig("Lecture_03_Lab_Exercise_1_Separable.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot interactively.
