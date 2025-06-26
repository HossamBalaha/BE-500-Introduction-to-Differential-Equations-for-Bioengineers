"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 17th, 2025
# Last Modification Date: June 18th, 2025
# Permissions and Citation: Refer to the README file.
"""

# Import necessary libraries.
from sympy import symbols, exp, sin, cos, laplace_transform, inverse_laplace_transform, Eq, solve

# Define the different symbols.
t, s = symbols("t s", real=True)
a, b, c, d = symbols("a b c d", real=True)


# Laplace Transform of a function.

# Example 1: Laplace Transform of f(t) = e^(-2t) * sin(3t)
f1 = exp(-2 * t) * sin(3 * t)
F1 = laplace_transform(f1, t, s)
# Display the result of the Laplace Transform.
print(f"Laplace Transform of {f1} is: {F1[0]}")
