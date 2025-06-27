"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 25th, 2025
# Last Modification Date: June 25th, 2025
# Permissions and Citation: Refer to the README file.
"""

# Import necessary libraries.
from sympy import symbols, inverse_laplace_transform

# Define the different symbols.
t, s = symbols("t s", real=True)
a, b, c, d = symbols("a b c d", real=True, positive=True)

# Inverse Laplace Transform of a function.

# Example 1: Inverse Laplace Transform of F(s) = 1 / (s + 2).
F1 = 1 / (s + 2)
f1 = inverse_laplace_transform(F1, s, t)
# Display the result of the Inverse Laplace Transform.
print(f"Inverse Laplace Transform of {F1} is:\n\t{f1}")
print("")

# Example 2: Inverse Laplace Transform of F(s) = 3 / (s^2 + 9).
F2 = 3 / (s ** 2 + 9)
f2 = inverse_laplace_transform(F2, s, t)
# Display the result of the Inverse Laplace Transform.
print(f"Inverse Laplace Transform of {F2} is:\n\t{f2}")
print("")

# Example 3: Inverse Laplace Transform of F(s) = (b * s + d) / (s^2 + c^2).
F3 = (b * s + d) / (s ** 2 + c ** 2)
f3 = inverse_laplace_transform(F3, s, t)
# Display the result of the Inverse Laplace Transform.
print(f"Inverse Laplace Transform of {F3} is:\n\t{f3}")
print("")

# Example 4: Inverse Laplace Transform of F(s) = (s + 1) / (s^2 + 4 * s + 5).
F4 = (s + 1) / (s ** 2 + 4 * s + 5)
f4 = inverse_laplace_transform(F4, s, t)
# Display the result of the Inverse Laplace Transform.
print(f"Inverse Laplace Transform of {F4} is:\n\t{f4}")
