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
import matplotlib.pyplot as plt

# Physical parameters: natural frequency and amplitude used to build x(t).
omega0 = 2 * np.pi  # Set the natural frequency (1 Hz, in radians per second).
A = 1.0  # Set the amplitude of oscillation.

# Generate a high-resolution time vector for smooth visualization of oscillations.
t = np.linspace(0, 5, 1000)

# Compute displacement for two different phase/amplitude choices (B).
# Case 1: no phase shift (B = 0.0).
B = 0.0  # Set the second amplitude to zero (no phase shift).
x1 = A * np.cos(omega0 * t) + B * np.sin(omega0 * t)

# Case 2: with phase contribution (B = 1.0).
# Changing B alters the initial condition and shifts the waveform.
B = 1.0  # Set the second amplitude to one (phase shift).
x2 = A * np.cos(omega0 * t) + B * np.sin(omega0 * t)

# Plot the two waveforms to compare the effect of the phase term.
plt.figure(figsize=(10, 5))  # Create a figure with a specified size.
plt.plot(t, x1, label="B = 0.0", color="blue")  # Plot the first displacement with label and color.
plt.plot(t, x2, label="B = 1.0", color="orange")  # Plot the second displacement with label and color.
plt.title("Undamped Oscillation")  # Set the plot title.
plt.xlabel("Time (t)")  # Label the x-axis as time.
plt.ylabel("Displacement x(t)")  # Label the y-axis as displacement.
plt.grid(True)  # Enable the grid for better readability.
plt.legend()  # Show the legend on the plot.
plt.tight_layout()  # Adjust the layout to prevent overlap of labels and titles.

# Save the plot as a PNG file with high resolution for inclusion in lecture notes.
plt.savefig("Lecture_04_Lab_Exercise_1_Undamped.png", dpi=300, bbox_inches="tight")

# Display the plot interactively.
plt.show()
