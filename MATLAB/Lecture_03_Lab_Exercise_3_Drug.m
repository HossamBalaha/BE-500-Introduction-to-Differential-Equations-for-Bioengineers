% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Import necessary libraries (Symbolic Math Toolbox and ODE solver).
syms t C(t) C1

% Define parameters for the drug simulation.
% k: elimination rate constant, C0: initial concentration
k = 0.5; % Elimination rate constant
C0 = 10; % Initial drug concentration

% Define the initial time for the IVP.
t0 = 0;

% Define the drug concentration equation symbolically for dsolve.
% Equation form: dC/dt = -k * C
drugEquation = diff(C, t) == - k * C;

% Solve the drug equation analytically using dsolve (returns general solution).
analyticalSolution = dsolve(drugEquation);

% Print the general analytical solution for instructional clarity.
disp('Analytical General Solution:');
disp(analyticalSolution);

% Apply the initial condition symbolically and solve for the constant C1.
initialCondition = subs(analyticalSolution, t, t0) == C0;
constValue = solve(initialCondition, C1);

% Print the constant value for verification.
disp('Value of Constant:');
disp(constValue);

% Substitute the constant back into the analytic solution to obtain specific solution.
specificSolution = subs(analyticalSolution, C1, constValue);

% Print the specific analytical solution with the initial condition applied.
disp('Analytical Specific Solution:');
disp(specificSolution);

% Generate a numeric grid for plotting the analytical solution between 0 and 20.
tAnalytical = linspace(0, 20, 100);
CAnalytical = double(subs(specificSolution, t, tAnalytical));

% Define the drug concentration equation as a function handle for numerical solver (ode45).
% f(t, C) returns dC/dt; use this with ode45 for numeric integration.
f = @(t, C) - k * C; % Define the drug concentration equation as a function.
% Initial condition C(0) = C0.
[tNumerical, CNumerical] = ode45(f, [0, 20], C0); 

% Plot the numerical solution as red dots to illustrate discrete solver output.
plot(tNumerical, CNumerical, 'ro', 'MarkerSize', 4, 'DisplayName', 'Numerical Solution');

% Hold the plot and overlay the analytical solution as a continuous blue line.
hold on;
plot(tAnalytical, CAnalytical, 'b-', 'LineWidth', 1.5, 'DisplayName', 'Analytical Solution');

% Add labels, title, legend and grid to the plot for clarity.
xlabel('Time (t)');
ylabel('Drug Concentration (C)');
title('Drug Concentration Simulation: Analytical vs. Numerical');
legend('show');
grid on;

% Save the plot as a PNG file with a descriptive filename for lecture materials.
saveas(gcf, 'Lecture_03_Lab_Exercise_3_Drug.png');
