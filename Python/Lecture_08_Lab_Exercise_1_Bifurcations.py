"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Initial Creation Date: July 2nd, 2025
# Last Modification Date: July 9th, 2025
# Permissions and Citation: Refer to the README file.
"""

# THIS CODE IS USED FOR VISUALIZATIONS ONLY
# FOR THE LECTURE PURPOSES. YOU DON'T HAVE
# TO RUN IT OR STUDY IT AT THIS MOMENT.

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def SaddleNodeBifurcation():
  """
  Function to plot the saddle-node bifurcation diagram.
  """

  def dxdt(x, r):
    """
    Function to compute the derivative dx/dt for the saddle-node bifurcation.
    """
    return r + x ** 2

  # Define the range of r values for the bifurcation diagram.
  rValues = np.linspace(-1, 1, 1000)
  equilibria = []

  # Loop through different values of r to find equilibria.
  for r in rValues:
    # Use fsolve to find roots of dx/dt = 0.
    roots = fsolve(
      dxdt,  # Function to find roots of dx/dt = 0.
      [-1, 1],  # Initial guesses for the roots.
      args=(r,),  # Additional arguments to pass to dxdt.
    )
    for root in roots:
      # Check if the root is valid.
      if (np.isclose(dxdt(root, r), 0)):
        equilibria.append((r, root))

  # Convert equilibria to a numpy array for easier plotting.
  equilibria = np.array(equilibria)
  stable = equilibria[equilibria[:, 1] < 0]  # Stable branch (below x=0).
  unstable = equilibria[equilibria[:, 1] >= 0]  # Unstable branch (above x=0).

  # Define the range of r values for the phase space plot.
  rValues = np.linspace(-1, 1, 10)
  xSpan = np.linspace(-1, 1, 400)
  phasePlots = []
  # Loop through different values of r to compute dx/dt for the phase space plot.
  for r in rValues:
    output = dxdt(xSpan, r)  # Compute dx/dt for each x.
    phasePlots.append((xSpan, output))

  # Plot the bifurcation diagram.
  plt.figure(figsize=(10, 6))
  plt.subplot(1, 2, 1)
  plt.plot(stable[:, 0], stable[:, 1], "b-", label="Stable", lw=2)
  plt.plot(unstable[:, 0], unstable[:, 1], "r--", label="Unstable", lw=2)
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Saddle-Node Bifurcation Diagram", fontsize=16)
  plt.xlabel("Parameter (r)", fontsize=14)
  plt.ylabel("Equilibrium Points (x)", fontsize=14)
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  # Phase space plot.
  plt.subplot(1, 2, 2)
  for xSpan, output in phasePlots:
    plt.plot(xSpan, output, lw=1, label=f"r = {output[0]:.2f}")
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Phase Space Plot (x vs. dx/dt)", fontsize=16)  # Title for the second plot.
  plt.xlabel("x", fontsize=14)  # Label the x-axis for the second plot.
  plt.ylabel("dx/dt", fontsize=14)  # Label the y-axis for the second plot.
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  plt.savefig("SaddleNodeBifurcationDiagram.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


def TranscriticalBifurcation():
  """
  Function to plot the transcritical bifurcation diagram.
  """

  def dxdt(x, r):
    """
    Function to compute the derivative dx/dt for the transcritical bifurcation.
    """
    return r * x - x ** 2

  # Define the range of r values for the bifurcation diagram.
  rValues = np.linspace(-1, 1, 250)
  equilibria = []

  # Loop through different values of r to find equilibria.
  for r in rValues:
    # Use fsolve to find roots of dx/dt = 0.
    roots = fsolve(
      dxdt,  # Function to find roots of dx/dt = 0.
      [-1, 1],  # Initial guesses for the roots.
      args=(r,),  # Additional arguments to pass to dxdt.
    )
    for root in roots:
      # Check if the root is valid.
      if (np.isclose(dxdt(root, r), 0)):
        equilibria.append((r, root))

  # Separate stable and unstable branches based on the sign of r.
  equilibria = np.array(equilibria)
  stable = []
  unstable = []

  for r, x in equilibria:
    if (r < 0):
      if (np.isclose(x, 0)):  # x = 0 is stable for r < 0.
        stable.append((r, x))
      else:  # x = r is unstable for r < 0.
        unstable.append((r, x))
    elif (r > 0):
      if (np.isclose(x, r)):  # x = r is stable for r > 0.
        stable.append((r, x))
      else:  # x = 0 is unstable for r > 0.
        unstable.append((r, x))
    else:  # At r = 0, both equilibria collide.
      unstable.append((r, x))

  stable = np.array(stable)
  unstable = np.array(unstable)

  # Define the range of r values for the phase space plot.
  rValues = np.linspace(-1, 1, 10)
  xSpan = np.linspace(-1, 1, 400)
  phasePlots = []
  # Loop through different values of r to compute dx/dt for the phase space plot.
  for r in rValues:
    output = dxdt(xSpan, r)  # Compute dx/dt for each x.
    phasePlots.append((xSpan, output))

  # Plot the bifurcation diagram.
  plt.figure(figsize=(10, 6))
  plt.subplot(1, 2, 1)
  plt.plot(stable[:, 0], stable[:, 1], "b-", label="Stable", lw=2)
  plt.plot(unstable[:, 0], unstable[:, 1], "r--", label="Unstable", lw=2)
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Transcritical Bifurcation Diagram", fontsize=16)
  plt.xlabel("Parameter (r)", fontsize=14)
  plt.ylabel("Equilibrium Points (x)", fontsize=14)
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  # Phase space plot.
  plt.subplot(1, 2, 2)
  for xSpan, output in phasePlots:
    plt.plot(xSpan, output, lw=1, label=f"r = {output[0]:.2f}")
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Phase Space Plot (x vs. dx/dt)", fontsize=16)  # Title for the second plot.
  plt.xlabel("x", fontsize=14)  # Label the x-axis for the second plot.
  plt.ylabel("dx/dt", fontsize=14)  # Label the y-axis for the second plot.
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  plt.savefig("TranscriticalBifurcationDiagram.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


def PitchforkBifurcation():
  """
  Function to plot the pitchfork bifurcation diagram.
  """

  def dxdt(x, r):
    """
    Function to compute the derivative dx/dt for the pitchfork bifurcation.
    """
    return r * x - x ** 3

  # Define the range of r values for the bifurcation diagram.
  rValues = np.linspace(-1, 1, 500)
  equilibria = []

  # Find equilibrium points for each r value.
  for r in rValues:
    roots = fsolve(dxdt, [-1, 0, 1], args=(r,))
    for root in roots:
      if (np.isclose(dxdt(root, r), 0)):  # Check if the root is valid.
        equilibria.append((r, root))

  # Separate stable and unstable branches based on the value of r.
  equilibria = np.array(equilibria)
  stable = []
  unstable = []

  for r, x in equilibria:
    if (r < 0):
      if (np.isclose(x, 0)):  # x = 0 is stable for r < 0.
        stable.append((r, x))
      else:  # Other roots (non-zero) are unstable for r < 0.
        unstable.append((r, x))
    elif (r > 0):
      if (np.isclose(x, 0)):  # x = 0 is unstable for r > 0.
        unstable.append((r, x))
      else:  # x = ±sqrt(r) are stable for r > 0.
        stable.append((r, x))
    else:  # At r = 0, the equilibrium at x = 0 is unstable.
      unstable.append((r, x))

  stable = np.array(stable)
  unstable = np.array(unstable)

  # Define the range of r values for the phase space plot.
  rValues = np.linspace(-1, 1, 10)
  xSpan = np.linspace(-1, 1, 400)
  phasePlots = []
  # Loop through different values of r to compute dx/dt for the phase space plot.
  for r in rValues:
    output = dxdt(xSpan, r)  # Compute dx/dt for each x.
    phasePlots.append((xSpan, output))

  # Plot the bifurcation diagram.
  plt.figure(figsize=(10, 6))
  plt.subplot(1, 2, 1)
  plt.plot(stable[:, 0], stable[:, 1], "b-", label="Stable", lw=2)
  plt.plot(unstable[:, 0], unstable[:, 1], "r--", label="Unstable", lw=2)
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Pitchfork Bifurcation Diagram", fontsize=16)
  plt.xlabel("Parameter (r)", fontsize=14)
  plt.ylabel("Equilibrium Points (x)", fontsize=14)
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  # Phase space plot.
  plt.subplot(1, 2, 2)
  for xSpan, output in phasePlots:
    plt.plot(xSpan, output, lw=1, label=f"r = {output[0]:.2f}")
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Phase Space Plot (x vs. dx/dt)", fontsize=16)  # Title for the second plot.
  plt.xlabel("x", fontsize=14)  # Label the x-axis for the second plot.
  plt.ylabel("dx/dt", fontsize=14)  # Label the y-axis for the second plot.
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  plt.savefig("PitchforkBifurcationDiagram.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


def HopfBifurcation():
  """
  Function to plot the Hopf bifurcation diagram.
  """

  def fitzhughNagumo(z, I, epsilon=0.08, a=0.7, b=0.8):
    """
    Function to compute the derivative dz/dt for the FitzHugh-Nagumo model.
    """
    v, w = z
    dvdt = v - (v ** 3) / 3 - w + I
    dwdt = epsilon * (v + a - b * w)
    return [dvdt, dwdt]

  # Define the range of I values for the bifurcation diagram.
  IValues = np.linspace(-2.5, 2.5, 500)
  equilibria = []

  # Find equilibrium points for each I value.
  for I in IValues:
    # Solve for steady-state solutions (dv/dt = 0, dw/dt = 0).
    sol = fsolve(fitzhughNagumo, [0, 0], args=(I,))
    if (np.allclose(fitzhughNagumo(sol, I), [0, 0])):  # Check if solution is valid.
      equilibria.append((I, sol[0]))  # Store membrane potential (v).

  # Convert equilibria to a numpy array for easier plotting.
  equilibria = np.array(equilibria)

  # Define the range of r values for the phase space plot.
  rValues = np.linspace(-2.5, 2.5, 15)
  xSpan = np.linspace(-2.5, 2.5, 15)
  phasePlots = []
  # Loop through different values of r to compute dx/dt for the phase space plot.
  for r in rValues:
    # Assuming w = 0 for simplicity.
    output = rValues - (rValues ** 3) / 3 - 0 + r
    phasePlots.append((xSpan, output))

  # Plot the bifurcation diagram.
  plt.figure(figsize=(10, 6))
  plt.subplot(1, 2, 1)
  plt.plot(equilibria[:, 0], equilibria[:, 1], "b-", label="Equilibrium", lw=2)
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Hopf Bifurcation Diagram", fontsize=16)
  plt.xlabel("Parameter (I)", fontsize=14)
  plt.ylabel("Equilibrium Membrane Potential (v)", fontsize=14)
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  # Phase space plot.
  plt.subplot(1, 2, 2)
  for xSpan, output in phasePlots:
    plt.plot(xSpan, output, lw=1, label=f"r = {output[0]:.2f}")
  plt.axhline(0, color="black", lw=0.5, ls="--")
  plt.title("Phase Space Plot (v vs. dv/dt)", fontsize=16)  # Title for the second plot.
  plt.xlabel("v", fontsize=14)  # Label the x-axis for the second plot.
  plt.ylabel("dv/dt", fontsize=14)  # Label the y-axis for the second plot.
  plt.legend()  # Add legend to the plot.
  plt.grid()  # Add grid to the plot.

  plt.savefig("HopfBifurcationDiagram.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


# SaddleNodeBifurcation()
# TranscriticalBifurcation()
# PitchforkBifurcation()
# HopfBifurcation()
