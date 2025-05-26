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
syms t P(t) C1

% Define parameters for the logistic growth model.
r = 0.5; % Growth rate.
K = 100; % Carrying capacity.
P0 = 10; % Initial population size.

% Define the initial condition.
t0 = 0;

% Define the logistic growth equation as a symbolic differential equation.
logisticEquation = diff(P, t) == r * P * (1.0 - P / K);

% Solve the logistic equation analytically using dsolve.
analyticalSolution = dsolve(logisticEquation);
analyticalSolution = analyticalSolution(1);

% Print the general analytical solution.
disp('Analytical General Solution:');
disp(analyticalSolution);

% Apply the initial condition to solve for the constant C1.
initialCondition = subs(analyticalSolution, t, t0) == P0;
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
PAnalytical = double(subs(specificSolution, t, tAnalytical));

% Solve the ODE numerically over the interval [0, 20] using ode45.
f = @(t, P) r * P .* (1 - P / K); % Define the logistic growth equation as a function.
% Initial condition P(0) = P0.
[tNumerical, PNumerical] = ode45(f, [0, 20], P0); 

% Plot the numerical solution as red dots.
plot(tNumerical, PNumerical, 'ro', 'MarkerSize', 4, 'DisplayName', 'Numerical Solution');

% Hold the plot and overlay the analytical solution as a blue line.
hold on;
plot(tAnalytical, PAnalytical, 'b-', 'LineWidth', 1.5, 'DisplayName', 'Analytical Solution');

% Label the axes and add a title.
xlabel('Time (t)');
ylabel('Population Size (P)');
title('Logistic Growth Model: Analytical vs. Numerical');

% Add a legend to distinguish between solutions.
legend('show');

% Add a grid to the plot for better readability.
grid on;

% Save the plot as a PNG file with high resolution.
saveas(gcf, 'Lecture_03_Lab_Exercise_2_Growth.png');
