"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 27th, 2025
# Last Modification Date: June 27th, 2025
# Permissions and Citation: Refer to the README file.
"""

# Import necessary libraries.
from sympy import symbols, Function, Heaviside, laplace_transform, inverse_laplace_transform, Eq, solve
import matplotlib.pyplot as plt

# Equation should be:
# dC/dt + k * C = R(t)
# R(t) = R0 * u(t - a).
# where u(t - a) is the unit step function that starts at t = a.
# So: dC/dt = R0 * u(t - a) - k * C (or) dC/dt + k * C = R0 * u(t - a).

# Define the parameters.
k = 0.5  # Elimination rate constant (1/hour).
C0 = 0  # Initial concentration of the drug (mg/L).
a = 2  # Time (hours). Constant infusion starting at t = a.
R0 = 20  # Rate of infusion (mg/hour).

# Define the different symbols.
t, s = symbols("t s", real=True)
C = Function("C")(t)  # Concentration of the drug as a function of time.
R = R0 * Heaviside(t - a)  # Infusion rate function.

lapdC = laplace_transform(C.diff(t), t, s)[0]  # Laplace Transform of dC/dt.
print(f"Laplace Transform of dC/dt:\n{lapdC}\n")

lapC = laplace_transform(C, t, s)[0]  # Laplace Transform of C(t).
print(f"Laplace Transform of C(t):\n{lapC}\n")

# Laplace Transform of the left-hand side of the equation.
lapLHS = lapdC + k * lapC
print(f"Laplace Transform of the left-hand side:\n{lapLHS}\n")

# Laplace Transform of the right-hand side of the equation.
lapRHS = laplace_transform(R, t, s)[0]
print(f"Laplace Transform of the right-hand side:\n{lapRHS}\n")

# Solve for the Laplace Transform of C(s).
lapCs = solve(Eq(lapLHS, lapRHS), lapC)[0]  # Solve for C(s).
print(f"Laplace Transform of C(s):\n{lapCs}\n")

# Substitute the initial condition C(0) = C0 into the equation.
lapCs = lapCs.subs(C.subs(t, 0), C0)  # Substitute the initial condition.
print(f"Laplace Transform of C(s) with initial condition:\n{lapCs}\n")

# Inverse Laplace Transform to find C(t).
Ct = inverse_laplace_transform(lapCs, s, t)
print(f"Concentration of the drug C(t):\n{Ct}")

# Create a time vector for plotting.
timeVector = [i / 10 for i in range(100)]  # From 0 to 10 hours in steps of 0.1 hours.
# Calculate the concentration of the drug at each time point.
concentration = [Ct.subs(t, time) for time in timeVector]
# Plot the concentration of the drug over time.
plt.figure()
plt.plot(timeVector, concentration, label="C(t)", color="blue")
plt.title("Concentration of the Drug Over Time")
plt.xlabel("Time (hours)")
plt.ylabel("Concentration (mg/L)")
plt.tight_layout()
plt.grid()

# Save the plot as a PNG file with high resolution.
plt.savefig(
  "Lecture_07_Lab_Exercise_3_Drug.png",
  dpi=300,
  bbox_inches="tight",
)
# Display the plot.
plt.show()
