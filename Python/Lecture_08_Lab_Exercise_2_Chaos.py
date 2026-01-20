"""
========================================================================
        ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
        ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
        ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
========================================================================
# Author: Hossam Magdy Balaha
# Permissions and Citation: Refer to the README file.
"""

# THIS CODE IS USED FOR VISUALIZATIONS ONLY
# FOR THE LECTURE PURPOSES. YOU DON'T HAVE
# TO RUN IT OR STUDY IT AT THIS MOMENT.

# Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def ChaosLorenzTypeNeuronModel():
  """
  Function to plot the Lorenz-type neuron model.

  Neural firing patterns can become chaotic under certain conditions,
  for example, during seizures or in response to external noise.
  The Lorenz system, while originally from fluid dynamics,
  has been used to model chaotic EEG signals and neural dynamics.

  This model is a chaotic system that can be used to simulate neuron dynamics.
  The equations are derived from the Lorenz system, which exhibits chaotic behavior.
  """

  def lorenz(t, y, sigma=10, beta=8 / 3, rho=28):
    """
    Function to compute the derivatives for the Lorenz-type neuron model.
    """
    x, y, z = y
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

  # Initial conditions and time span for the simulation.
  initialConditions = [0.0, 1.0, 2.0]
  tSpan = (0, 40)
  tEval = np.linspace(tSpan[0], tSpan[1], 10000)

  # Solve the ODE using solve_ivp.
  sol = solve_ivp(lorenz, tSpan, initialConditions, t_eval=tEval)

  # Plotting the results.
  plt.figure(figsize=(12, 6))
  plt.plot(sol.y[0], sol.y[1], lw=0.5)
  plt.title("Lorenz-Type Neuron Model", fontsize=16)
  plt.xlabel("x", fontsize=14)
  plt.ylabel("y", fontsize=14)
  plt.grid()  # Add grid to the plot.
  plt.savefig("ChaosLorenzTypeNeuronModel.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


def ChaosRosslerPopulationModel():
  """
  Function to plot the Rössler-type population model.

  The Rössler attractor is another chaotic system that can be used to model
  population dynamics in ecology, where populations can exhibit chaotic behavior
  due to interactions between species or environmental factors.
  """

  def rossler(t, y, a=0.2, b=0.2, c=5.7):
    """
    Function to compute the derivatives for the Rössler-type population model.
    """
    x, y, z = y
    dxdt = -y - z
    dydt = x + a * y
    dzdt = b + z * (x - c)
    return [dxdt, dydt, dzdt]

  # Initial conditions and time span for the simulation.
  initialConditions = [0.0, 0.1, 0.2]
  tSpan = (0, 100)
  tEval = np.linspace(tSpan[0], tSpan[1], 10000)

  # Solve the ODE using solve_ivp.
  sol = solve_ivp(rossler, tSpan, initialConditions, t_eval=tEval)

  # Plotting the results.
  plt.figure(figsize=(12, 6))
  plt.plot(sol.y[0], sol.y[1], lw=0.5)
  plt.title("Rössler-Type Population Model", fontsize=16)
  plt.xlabel("x", fontsize=14)
  plt.ylabel("y", fontsize=14)
  plt.grid()  # Add grid to the plot.
  plt.savefig("ChaosRosslerPopulationModel.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


def ChaosForcedVanDerPolOscillator():
  """
  Function to plot the forced Van der Pol oscillator.

  The Van der Pol oscillator is a nonlinear oscillator that can exhibit
  chaotic behavior when subjected to external forcing.
  It is often used to model oscillatory systems in biology and engineering.
  """

  def vanDerPol(t, y, mu=1.0, force=0.5, omega=0.5):
    """
    Function to compute the derivatives for the forced Van der Pol oscillator.
    """
    x, v = y
    dxdt = v
    dvdt = mu * (1 - x ** 2) * v - x + force * np.cos(omega * t)
    return [dxdt, dvdt]

  # Initial conditions and time span for the simulation.
  initialConditions = [2.5, 5.0]
  tSpan = (0, 100)
  tEval = np.linspace(tSpan[0], tSpan[1], 10000)

  # Solve the ODE using solve_ivp.
  sol = solve_ivp(vanDerPol, tSpan, initialConditions, t_eval=tEval)

  # Plotting the results.
  plt.figure(figsize=(12, 6))
  plt.plot(sol.t, sol.y[0], lw=0.5)
  plt.title("Forced Van der Pol Oscillator", fontsize=16)
  plt.xlabel("Time (t)", fontsize=14)
  plt.ylabel("Displacement (x)", fontsize=14)
  plt.grid()  # Add grid to the plot.
  plt.savefig("ChaosForcedVanDerPolOscillator.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.


def ChaosHindmarshRoseNeuronModel():
  """
  Function to plot the Hindmarsh-Rose neuron model.

  The Hindmarsh-Rose model is a well-known model for neuronal dynamics
  that can exhibit chaotic behavior under certain conditions.
  It is often used to study the dynamics of bursting neurons.
  """

  def hindmarshRose(t, y, I=-5, r=0.01, a=1.0, b=3, c=1, d=5, s=4, x0=1.6):
    """
    Function to compute the derivatives for the Hindmarsh-Rose neuron model.
    """
    x, y, z = y
    dxdt = y - a * x ** 3 + b * x ** 2 + I - z
    dydt = c - d * x ** 2 - y
    dzdt = r * (s * (x - x0) - z)
    return [dxdt, dydt, dzdt]

  # Initial conditions and time span for the simulation.
  initialConditions = [1.0, 1.0, 1.0]
  tSpan = (0, 50)
  tEval = np.linspace(tSpan[0], tSpan[1], 10000)

  # Solve the ODE using solve_ivp.
  sol = solve_ivp(hindmarshRose, tSpan, initialConditions, t_eval=tEval)

  # Plotting the results.
  plt.figure(figsize=(12, 6))
  plt.plot(sol.t, sol.y[0], lw=0.5)
  plt.title("Hindmarsh-Rose Neuron Model", fontsize=16)
  plt.xlabel("Time (t)", fontsize=14)
  plt.ylabel("Membrane Potential (x)", fontsize=14)
  plt.grid()  # Add grid to the plot.
  plt.savefig("ChaosHindmarshRoseNeuronModel.png", dpi=300, bbox_inches="tight")
  plt.show()  # Display the plot.
  plt.close()  # Close the plot to free memory.

# ChaosLorenzTypeNeuronModel()
# ChaosRosslerPopulationModel()
# ChaosForcedVanDerPolOscillator()
# ChaosHindmarshRoseNeuronModel()
