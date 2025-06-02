'''
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: June 2nd, 2025
# Last Modification Date: June 2nd, 2025
# Permissions and Citation: Refer to the README file.
'''

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

# Underdamped:
# omega0 = 2 * np.pi  # Set the natural frequency (1 Hz, in radians per second).
# gamma = 0.1  # Set the damping coefficient (for example, 0.1).

# Underdamped (2):
# omega0 = 2 * np.pi  # Set the natural frequency (1 Hz, in radians per second).
# gamma = 1.25  # Set the damping coefficient (for example, 0.1).

# Critically damped:
# omega0 = 0.25 * np.pi  # Set the natural frequency (1 Hz, in radians per second).
# gamma = 0.25 * np.pi  # Set the damping coefficient (for example, 0.1).

# Overdamped:
# omega0 = 0.25 * np.pi  # Set the natural frequency (1 Hz, in radians per second).
# gamma = 1.25  # Set the damping coefficient (for example, 0.1).

omega0 = 0.25 * np.pi  # Set the natural frequency (1 Hz, in radians per second).
gamma = 0.25 * np.pi  # Set the damping coefficient (for example, 0.1).
zeta = gamma / omega0  # Calculate the damping ratio.
A = 1.0  # Set the amplitude of oscillation.
B = 0.5  # Set the second amplitude (for phase shift).

# Generate 1000 time points from 0 to 25 seconds.
t = np.linspace(0, 25, 1000)

print("Parameters:")
print(f"Natural Frequency (omega0): {np.round(omega0, 4)} rad/s")
print(f"Damping Coefficient (gamma): {np.round(gamma, 4)}")
print(f"Damping Ratio (zeta): {np.round(zeta, 4)}")
print(f"Amplitude (A): {A}")
print(f"Phase Shift Amplitude (B): {B}")

if (zeta < 1):  # Check if the system is underdamped.
  print("\nUnderdamped Oscillation")
  print("Solution: x(t) = exp(-gamma * t) * (A * cos(omegad * t) + B * sin(omegad * t))")
  print("where omegad = sqrt(omega0^2 - gamma^2) is the damped natural frequency.")
  print("where A and B are constants determined by initial conditions.")
  omegad = np.sqrt(omega0 ** 2 - gamma ** 2)  # Calculate the damped natural frequency.
  # Calculate the displacement for underdamped oscillation.
  x = np.exp(-gamma * t) * (A * np.cos(omegad * t) + B * np.sin(omegad * t))
elif (zeta == 1):  # Check if the system is critically damped.
  print("\nCritically Damped Oscillation")
  print("Solution: x(t) = (A + B * t) * exp(-gamma * t)")
  print("where A and B are constants determined by initial conditions.")
  # Calculate the displacement for critically damped oscillation.
  x = (A + B * t) * np.exp(-gamma * t)
else:  # The system is overdamped.
  print("\nOverdamped Oscillation")
  print("Solution: x(t) = A * exp(r1 * t) + B * exp(r2 * t)")
  print("where r1 and r2 are the roots of the characteristic equation and are real, distinct, and negative.")
  print("where r1 = -gamma + sqrt(gamma^2 - omega0^2) and r2 = -gamma - sqrt(gamma^2 - omega0^2).")
  print("where A and B are constants determined by initial conditions.")
  r1 = -gamma + np.sqrt(gamma ** 2 - omega0 ** 2)  # First root.
  r2 = -gamma - np.sqrt(gamma ** 2 - omega0 ** 2)  # Second root.
  # Calculate the displacement for overdamped oscillation.
  x = A * np.exp(r1 * t) + B * np.exp(r2 * t)

plt.figure(figsize=(10, 5))  # Create a figure with a specified size.
plt.plot(t, x, label="Displacement x(t)", color="blue")  # Plot the displacement with label and color.
plt.title("Damped Oscillation")  # Set the plot title.
plt.xlabel("Time (t)")  # Label the x-axis as time.
plt.ylabel("Displacement x(t)")  # Label the y-axis as displacement.
plt.grid(True)  # Enable the grid for better readability.
plt.legend()  # Show the legend on the plot.
plt.tight_layout()  # Adjust the layout to prevent overlap of labels and titles.

# Save the plot as a PNG file with high resolution.
plt.savefig("Lecture_04_Lab_Exercise_2_Damped.png", dpi=300, bbox_inches="tight")

# Display the plot.
plt.show()
