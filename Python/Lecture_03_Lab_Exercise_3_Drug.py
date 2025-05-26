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


# Define the drug concentration equation as a function to be used by the numerical solver.
def DrugConcentration(t, C, k):
  return - k * C


# Set parameters for the drug simulation.
k = 0.5  # Elimination rate constant.
C0 = [10]  # Initial drug concentration.

# Define symbolic variables for analytical solution.
tSym = symbols("t")  # Independent variable (time).
C = Function("C")(tSym)  # Dependent variable (drug concentration).
C1 = symbols("C1")  # Constant of integration.

# Define the drug concentration equation symbolically.
drugEquation = C.diff(tSym) - (- k * C)

# Solve the drug equation analytically using dsolve from sympy.
analyticalSolution = dsolve(drugEquation, C)

# Print the general analytical solution.
print("Analytical General Solution:")
print(analyticalSolution)

# Apply the initial condition to solve for the constant C1.
initialCondition = analyticalSolution.subs({tSym: 0, C: C0[0]})
constValue = solve(initialCondition.rhs - C0[0], C1)[0]

# Print the value of the constant of integration C1.
print("Value of Constant:", constValue)

# Substitute the value of C1 back into the analytical solution.
specificSolution = analyticalSolution.subs(C1, constValue)

# Print the specific analytical solution with the initial condition applied.
print("Analytical Specific Solution:")
print(specificSolution)

# Generate 100 points between 0 and 20 for the analytical solution.
tAnalytical = np.linspace(0, 20, 100)
CAnalytical = np.array([specificSolution.rhs.subs(tSym, val) for val in tAnalytical], dtype=float)

# Solve the ODE numerically over the interval [0, 20] using solve_ivp and store the solution.
sol = solve_ivp(
  DrugConcentration,  # The function to solve.
  [0, 20],  # The interval of integration.
  C0,  # Initial condition.
  args=(k,),  # Additional arguments for the function (k,).
  t_eval=np.linspace(0, 20, 100),  # Points at which to store the computed solution.
)

# Plot the numerical solution as red dots.
plt.plot(sol.t, sol.y[0], "ro", label="Numerical Solution", markersize=4)

# Overlay the analytical solution as a blue line.
plt.plot(tAnalytical, CAnalytical, "b-", label="Analytical Solution", linewidth=1.5)

# Label the axes and add a title.
plt.xlabel("Time (t)")
plt.ylabel("Drug Concentration (C)")
plt.title("Drug Concentration Simulation: Analytical vs. Numerical.")

# Add a legend to distinguish between solutions.
plt.legend()

# Add a grid to the plot for better readability.
plt.grid()

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_03_Lab_Exercise_3_Drug.png", dpi=300, bbox_inches="tight")

# Display the plot.
plt.show()
