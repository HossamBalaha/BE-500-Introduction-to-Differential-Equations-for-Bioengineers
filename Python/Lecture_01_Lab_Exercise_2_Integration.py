# Import necessary libraries for numerical computations and plotting.
import numpy as np  # Library for numerical operations.
import matplotlib.pyplot as plt  # Library for creating plots.
from scipy.integrate import quad  # Function for numerical integration.


# Define the function f(x) = e^(-x^2).
def f(x):
  return np.exp(-x ** 2)  # Return the value of the Gaussian function at x.


# Compute the definite integral of f(x) from 0 to 1 using quad().
result, _ = quad(f, 0, 1)  # Use quad() to compute the integral and store the result.
print("Integral from 0 to 1:", result)  # Print the computed integral value.

# Generate x values for plotting over the range [0, 1] with 500 points.
xVals = np.linspace(0, 1, 500)  # Create an array of 500 evenly spaced values between 0 and 1.

# Evaluate the function f(x) at each point in xVals.
yVals = f(xVals)  # Compute the y-values of the function f(x) for visualization.

# Plot the function and shade the area under the curve.
plt.figure(figsize=(10, 6))  # Create a new figure with a specified size.
plt.plot(xVals, yVals, label="f(x) = e^(-x^2)", color="blue")  # Plot f(x) with a label and blue color.

# Shade the area under the curve between x = 0 and x = 1.
plt.fill_between(xVals, yVals, color="lightblue", alpha=0.5)  # Fill the area under the curve with light blue color.

# Add reference lines at x=0 and y=0 for better visualization.
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Add a horizontal line at y=0.
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Add a vertical line at x=0.
plt.axvline(1, color="black", linewidth=0.8, linestyle="--")  # Add a vertical line at x=1.

# Add title, axis labels, grid, and legend to the plot.
plt.title("Area Under the Curve: Integral of f(x) = e^(-x^2) from 0 to 1.")  # Add a title to the plot.
plt.xlabel("x")  # Label the x-axis.
plt.ylabel("f(x)")  # Label the y-axis.
plt.grid()  # Add a grid to the plot for better readability.
plt.legend()  # Add a legend to identify the curve.

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_01_Lab_Exercise_2_Integration.png", dpi=300, bbox_inches="tight")
plt.show()  # Display the plot.
