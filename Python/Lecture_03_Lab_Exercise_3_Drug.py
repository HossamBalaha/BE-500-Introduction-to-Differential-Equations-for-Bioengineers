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


# Define the drug concentration equation as a function to be used by the numerical solver.
# Inputs: t (float) time, C (float) drug concentration, k (float) elimination rate
# Output: dC/dt = -k * C (float)
def DrugConcentration(t, C, k):
  return - k * C


# Set parameters for the drug simulation.
# k controls how quickly the drug is eliminated from the compartment.
k = 0.5  # Elimination rate constant.
C0 = [10]  # Initial drug concentration.

# Define symbolic variables for analytical solution demonstration.
# Used only for deriving the closed-form exponential decay solution.
tSym = symbols("t")  # Independent variable (time).
C = Function("C")(tSym)  # Dependent variable (drug concentration).
C1 = symbols("C1")  # Constant of integration.

# Define the drug concentration differential symbolically for dsolve.
drugEquation = C.diff(tSym) - (- k * C)

# Solve the drug equation analytically using sympy.dsolve and display the result.
analyticalSolution = dsolve(drugEquation, C)
print("Analytical General Solution:")
print(analyticalSolution)

# Apply the initial condition to solve for the constant C1 symbolically.
initialCondition = analyticalSolution.subs({tSym: 0, C: C0[0]})
constValue = solve(initialCondition.rhs - C0[0], C1)[0]

# Print the constant and substitute back to obtain the specific solution.
print("Value of Constant:", constValue)
specificSolution = analyticalSolution.subs(C1, constValue)
print("Analytical Specific Solution:")
print(specificSolution)

# Generate a numeric grid for plotting the analytical solution over 0..20.
# Using 100 points yields a smooth exponential curve for comparison.
tAnalytical = np.linspace(0, 20, 100)
CAnalytical = np.array([specificSolution.rhs.subs(tSym, val) for val in tAnalytical], dtype=float)

# Solve the ODE numerically over the interval [0, 20] using solve_ivp.
# `args` contains the elimination rate k for the solver function.
sol = solve_ivp(
  DrugConcentration,  # The function to solve (callable f(t, y)).
  [0, 20],  # The interval of integration [t0, tf].
  C0,  # Initial condition as a list.
  args=(k,),  # Additional arguments for the RHS function.
  t_eval=np.linspace(0, 20, 100),  # Points at which to store the computed solution.
)

# Plot the numerical solution points (red circles) to illustrate discrete solver output.
plt.plot(sol.t, sol.y[0], "ro", label="Numerical Solution", markersize=4)

# Overlay the analytical exponential decay (blue line) for comparison.
plt.plot(tAnalytical, CAnalytical, "b-", label="Analytical Solution", linewidth=1.5)

# Label the axes, add title and legend to make the figure self-contained.
plt.xlabel("Time (t)")
plt.ylabel("Drug Concentration (C)")
plt.title("Drug Concentration Simulation: Analytical vs. Numerical.")
plt.legend()
plt.grid()

# Save the figure: PNG at high resolution suitable for lecture slides.
plt.savefig("Lecture_03_Lab_Exercise_3_Drug.png", dpi=300, bbox_inches="tight")

# Display the plot interactively so the results can be inspected visually.
plt.show()
