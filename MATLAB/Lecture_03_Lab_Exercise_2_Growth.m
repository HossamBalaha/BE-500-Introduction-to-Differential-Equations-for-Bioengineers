% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Import necessary libraries (Symbolic Math Toolbox and ODE solver).
syms t P(t) C1

% Define parameters for the logistic growth model.
% r: intrinsic growth rate, K: carrying capacity, P0: initial population
r = 0.5; % Growth rate.
K = 100; % Carrying capacity.
P0 = 10; % Initial population size.

% Define the initial time for the IVP.
t0 = 0;

% Define the logistic growth equation symbolically for dsolve.
% Equation form: dP/dt = r * P * (1 - P/K)
logisticEquation = diff(P, t) == r * P * (1.0 - P / K);

% Solve the logistic equation analytically using dsolve (returns general solution).
analyticalSolution = dsolve(logisticEquation);
analyticalSolution = analyticalSolution(1);

% Print the general analytical solution for instructional clarity.
disp('Analytical General Solution:');
disp(analyticalSolution);

% Apply the initial condition symbolically to solve for the integration constant C1.
initialCondition = subs(analyticalSolution, t, t0) == P0;
constValue = solve(initialCondition, C1);

% Print value of the constant for verification.
disp('Value of Constant:');
disp(constValue);

% Substitute the constant back into the analytical solution to obtain specific solution.
specificSolution = subs(analyticalSolution, C1, constValue);

% Print the specific analytical solution with the initial condition applied.
disp('Analytical Specific Solution:');
disp(specificSolution);

% Generate a numeric grid for plotting the analytical solution between 0 and 20.
tAnalytical = linspace(0, 20, 100);
PAnalytical = double(subs(specificSolution, t, tAnalytical));

% Define the logistic equation as a function handle for numerical solver (ode45).
% Use element-wise operations to ensure vectorized evaluation if needed.
f = @(t, P) r * P .* (1.0 - P / K); % Define the logistic growth equation as a function.
% Initial condition P(0) = P0.
[tNumerical, PNumerical] = ode45(f, [0, 20], P0); 

% Plot the numerical solution as red dots to illustrate discrete solver output.
plot(tNumerical, PNumerical, 'ro', 'MarkerSize', 4, 'DisplayName', 'Numerical Solution');

% Hold the plot and overlay the analytical solution as a continuous blue line.
hold on;
plot(tAnalytical, PAnalytical, 'b-', 'LineWidth', 1.5, 'DisplayName', 'Analytical Solution');

% Add labels, title, legend and grid to make the plot self-contained.
xlabel('Time (t)');
ylabel('Population Size (P)');
title('Logistic Growth Model: Analytical vs. Numerical');
legend('show');
grid on;

% Save the plot as a PNG file with a descriptive filename for lecture materials.
saveas(gcf, 'Lecture_03_Lab_Exercise_2_Growth.png');
