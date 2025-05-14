# Import necessary libraries for numerical computations and plotting.
import numpy as np  # Library for numerical operations.
import matplotlib.pyplot as plt  # Library for creating plots.
from sympy import symbols, diff, lambdify  # Library for symbolic mathematics.

# Define the variable and the function f(x) = x^3 + 2x^2 - 5x + 1.
x = symbols("x")  # Create a symbolic variable 'x'.
f = x ** 3 + 2 * x ** 2 - 5 * x + 1  # Define the polynomial function f(x).

# Compute the derivative of the function f(x).
fPrime = diff(f, x)  # Use the diff() function to compute the derivative f'(x).
print("Function:", f)  # Print the symbolic function f(x).
print("Derivative:", fPrime)  # Print the symbolic derivative of f(x).

# Generate x values for plotting over the range [-5, 5] with 500 points.
xVals = np.linspace(-5, 5, 500)  # Create an array of 500 evenly spaced values between -5 and 5.

# Convert the symbolic function f(x) into a numerical function for evaluation.
fFunc = lambdify(x, f, "numpy")  # Convert the symbolic f(x) to a numerical function.
fVals = fFunc(xVals)  # Evaluate f(x) at each point in xVals.

# Convert the symbolic derivative f'(x) into a numerical function for evaluation.
fPrimeFunc = lambdify(x, fPrime, "numpy")  # Convert the symbolic f'(x) to a numerical function.
fPrimeVals = fPrimeFunc(xVals)  # Evaluate f'(x) at each point in xVals.

# Plot the original function f(x) and its derivative f'(x).
plt.figure(figsize=(10, 5))  # Create a new figure with a specified size.
plt.plot(xVals, fVals, label="f(x)", color="orange")  # Plot f(x) with a label and orange color.
plt.plot(xVals, fPrimeVals, label="f'(x)", color="blue", linestyle="--")  # Plot f'(x) with a dashed blue line.
plt.title("Function and Its Derivative")  # Add a title to the plot.
plt.xlabel("x")  # Label the x-axis.
plt.ylabel("f(x) and f'(x)")  # Label the y-axis.
plt.grid()  # Add a grid to the plot for better readability.
plt.legend()  # Add a legend to identify the curves.
# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_01_Lab_Exercise_1_Differentiation.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
