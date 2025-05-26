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
syms x y(x) C1

% Define the initial condition.
x0 = 0;
y0 = 1;

% Define the separable equation as a symbolic differential equation.
separableEquation = diff(y, x) == x * y;

% Solve the separable equation analytically using dsolve.
analyticalSolution = dsolve(separableEquation);

% Print the general analytical solution.
disp('Analytical General Solution:');
disp(analyticalSolution);

% Apply the initial condition to solve for the constant C1.
initialCondition = subs(analyticalSolution, x, x0) == y0;
constValue = solve(initialCondition, C1);

% Print the value of the constant.
disp('Value of Constant:');
disp(constValue);

% Substitute the value of C1 back into the analytical solution.
specificSolution = subs(analyticalSolution, C1, constValue);

% Print the specific analytical solution with the initial condition
% applied.
disp('Analytical Specific Solution:');
disp(specificSolution);

% Generate 100 points between 0 and 2 for the analytical solution.
xAnalytical = linspace(0, 2, 100);
yAnalytical = double(subs(specificSolution, x, xAnalytical));

% Solve the ODE numerically over the interval [0, 2] using ode45.
f = @(x, y) x .* y; % Define the separable equation as a function.
% Initial condition y(0) = 1.
[xNumerical, yNumerical] = ode45(f, [0, 2], 1); 

% Plot the numerical solution as red dots.
plot(xNumerical, yNumerical, 'ro', 'MarkerSize', 4, 'DisplayName', 'Numerical Solution');

% Hold the plot and overlay the analytical solution as a blue line.
hold on;
plot(xAnalytical, yAnalytical, 'b-', 'LineWidth', 1.5, 'DisplayName', 'Analytical Solution');

% Label the axes and add a title.
xlabel('x');
ylabel('y');
title('Solving Separable Equation: Analytical vs. Numerical');

% Add a legend to distinguish between solutions.
legend('show');

% Add a grid to the plot for better readability.
grid on;

% Save the plot as a PNG file with high resolution.
saveas(gcf, 'Lecture_03_Lab_Exercise_1_Separable.png');
