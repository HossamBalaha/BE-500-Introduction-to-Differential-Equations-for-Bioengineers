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


# Define the logistic growth equation as a function to be used by the numerical solver.
# Inputs: t (float) time, P (float) population size, r (float) growth rate, K (float) carrying capacity
# Output: dP/dt = r * P * (1 - P/K) (float)
def LogisticGrowth(t, P, r, K):
  return r * P * (1.0 - P / K)


# Set parameters for the logistic growth model.
# Choose values that produce a realistic logistic curve.
r = 0.5  # Growth rate.
K = 100  # Carrying capacity.
P0 = [10]  # Initial population size.

# Define symbolic variables for analytical solution demonstration.
# These symbolic objects are used only with sympy for closed-form solution derivation.
tSym = symbols("t")  # Independent variable (time).
P = Function("P")(tSym)  # Dependent variable (population size).
C1 = symbols("C1")  # Constant of integration.

# Define the logistic differential equation symbolically (for dsolve).
logisticEquation = P.diff(tSym) - r * P * (1.0 - P / K)

# Solve the logistic equation analytically using sympy.dsolve.
# The result is a general solution that includes the integration constant C1.
analyticalSolution = dsolve(logisticEquation, P)

# Print the general analytical solution for instructional purposes.
print("Analytical General Solution:", analyticalSolution)

# Apply the initial condition symbolically and solve for the integration constant C1.
initialCondition = analyticalSolution.subs({tSym: 0, P: P0[0]})
constValue = solve(initialCondition.rhs - P0[0], C1)[0]

# Substitute the constant back into the analytic solution to get the specific solution.
print("Value of Constant:", constValue)
specificSolution = analyticalSolution.subs(C1, constValue)

# Print the specific analytical solution for verification.
print("Analytical Specific Solution:", specificSolution)

# Generate a numeric grid for plotting the analytical solution between 0 and 20.
# Use 100 points to give smooth curves for comparison with numerical solver output.
tAnalytical = np.linspace(0, 20, 100)
# Evaluate the symbolic analytical solution at numeric time points and cast to float array.
PAnalytical = np.array([specificSolution.rhs.subs(tSym, val) for val in tAnalytical], dtype=float)

# Solve the ODE numerically over the interval [0, 20] using solve_ivp.
# `args` passes model parameters (r, K) into the solver function.
sol = solve_ivp(
  LogisticGrowth,  # Callable defining the RHS of the ODE.
  [0, 20],  # Time interval for integration.
  P0,  # Initial condition for P.
  args=(r, K),  # Additional parameters passed to the RHS function.
  t_eval=np.linspace(0, 20, 100),  # Time points at which to store the computed solution.
)

# Plot the numerical solution points (red circles) showing the discrete solver output.
plt.plot(sol.t, sol.y[0], "ro", label="Numerical Solution", markersize=4)
# Plot the continuous analytical solution (blue line) for comparison.
plt.plot(tAnalytical, PAnalytical, label="Analytical Solution", color="blue", linewidth=1.5)

# Label axes, add title and legend to make the figure self-contained and informative.
plt.xlabel("Time (t)")
plt.ylabel("Population Size (P)")
plt.title("Logistic Growth Model: Analytical vs. Numerical.")
plt.legend()
plt.grid()

# Save the figure in PNG format with high quality for lecture materials.
plt.savefig("Lecture_03_Lab_Exercise_2_Growth.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot interactively for visual inspection.
