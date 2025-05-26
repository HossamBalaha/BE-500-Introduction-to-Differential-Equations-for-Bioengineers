% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: May 26th, 2025
% Last Modification Date: May 26th, 2025
% Permissions and Citation: Refer to the README file.

% Import necessary libraries (Symbolic Math Toolbox and ODE solver).
syms t C(t) C1

% Define parameters for the drug simulation.
k = 0.5; % Elimination rate constant
C0 = 10; % Initial drug concentration

% Define the initial condition.
t0 = 0;

% Define the drug concentration equation as a symbolic differential equation.
drugEquation = diff(C, t) == - k * C;

% Solve the drug equation analytically using dsolve.
analyticalSolution = dsolve(drugEquation);

% Print the general analytical solution.
disp('Analytical General Solution:');
disp(analyticalSolution);

% Apply the initial condition to solve for the constant C1.
initialCondition = subs(analyticalSolution, t, t0) == C0;
constValue = solve(initialCondition, C1);

% Print the value of the constant.
disp('Value of Constant:');
disp(constValue);

% Substitute the value of C1 back into the analytical solution.
specificSolution = subs(analyticalSolution, C1, constValue);

% Print the specific analytical solution with the initial condition applied.
disp('Analytical Specific Solution:');
disp(specificSolution);

% Generate 100 points between 0 and 20 for the analytical solution.
tAnalytical = linspace(0, 20, 100);
CAnalytical = double(subs(specificSolution, t, tAnalytical));

% Solve the ODE numerically over the interval [0, 20] using ode45.
f = @(t, C) - k * C; % Define the drug concentration equation as a function.
% Initial condition C(0) = C0.
[tNumerical, CNumerical] = ode45(f, [0, 20], C0); 

% Plot the numerical solution as red dots.
plot(tNumerical, CNumerical, 'ro', 'MarkerSize', 4, 'DisplayName', 'Numerical Solution');

% Hold the plot and overlay the analytical solution as a blue line.
hold on;
plot(tAnalytical, CAnalytical, 'b-', 'LineWidth', 1.5, 'DisplayName', 'Analytical Solution');

% Label the axes and add a title.
xlabel('Time (t)');
ylabel('Drug Concentration (C)');
title('Drug Concentration Simulation: Analytical vs. Numerical');

% Add a legend to distinguish between solutions.
legend('show');

% Add a grid to the plot for better readability.
grid on;

% Save the plot as a PNG file with high resolution.
saveas(gcf, 'Lecture_03_Lab_Exercise_3_Drug.png');
