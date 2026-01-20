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
from sympy import symbols, exp, sin, cos, laplace_transform

# Define the different symbols.
t, s = symbols("t s", real=True)
a, b, c, d = symbols("a b c d", real=True, positive=True)

# Laplace Transform of a function.

# Example 1: Laplace Transform of f(t) = t * e^(-2t).
f1 = t * exp(-2 * t)
F1 = laplace_transform(f1, t, s)
# Display the result of the Laplace Transform.
print(f"Laplace Transform of {f1} is:\n\t{F1[0]}")
print("")

# Example 2: Laplace Transform of f(t) = e^(-2t) * sin(3t).
f2 = exp(-2 * t) * sin(3 * t)
F2 = laplace_transform(f2, t, s)
# Display the result of the Laplace Transform.
print(f"Laplace Transform of {f2} is:\n\t{F2[0]}")
print("")

# Example 3: Laplace Transform of f(t) = 1 - e^(-at) * (b * sin(ct) + d * cos(ct)).
f3 = 1 - exp(-a * t) * (b * sin(c * t) + d * cos(c * t))
F3 = laplace_transform(f3, t, s)
# Display the result of the Laplace Transform.
print(f"Laplace Transform of {f3} is:\n\t{F3[0]}")
