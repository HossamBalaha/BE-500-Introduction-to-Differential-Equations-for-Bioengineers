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
from sympy import symbols, Function, laplace_transform, inverse_laplace_transform, Eq, solve

# Define the parameters for the neural oscillation model.
x0 = 2  # Initial displacement (e.g., initial neuron signal strength).
v0 = -1  # Initial velocity (rate of change at t=0).

# Define the different symbols.
t, s = symbols("t s", real=True)
x = Function("x")(t)

lapX = laplace_transform(x, t, s)[0]  # Laplace Transform of x(t).
lapdX = laplace_transform(x.diff(t), t, s)[0]  # Laplace Transform of dx/dt.
lapdX2 = laplace_transform(x.diff(t, 2), t, s)[0]  # Laplace Transform of d^2x/dt^2.
print(f"Laplace Transform of x(t):\n{lapX}\n")
print(f"Laplace Transform of dx/dt:\n{lapdX}\n")
print(f"Laplace Transform of d^2x/dt^2:\n{lapdX2}\n")

# Laplace Transform of the left-hand side of the equation.
lapLHS = lapdX2 + 2 * lapdX + 5 * lapX
print(f"Laplace Transform of the left-hand side:\n{lapLHS}\n")

# Laplace Transform of the right-hand side of the equation.
lapRHS = laplace_transform(0, t, s)[0]
print(f"Laplace Transform of the right-hand side:\n{lapRHS}\n")

# # Solve for the Laplace Transform of x(s).
lapXs = solve(Eq(lapLHS, lapRHS), lapX)[0]  # Solve for x(s).
print(f"Laplace Transform of x(s):\n{lapXs}\n")

# Substitute the initial conditions into the equation.
lapXs = lapXs.subs({x.subs(t, 0): x0, x.diff(t).subs(t, 0): v0})  # Substitute initial conditions.
print(f"Laplace Transform of x(s) with initial conditions:\n{lapXs}\n")

# Inverse Laplace Transform to find x(t).
Xt = inverse_laplace_transform(lapXs, s, t)
print(f"Displacement x(t):\n{Xt}")
