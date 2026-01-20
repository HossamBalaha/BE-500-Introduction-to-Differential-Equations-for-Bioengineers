% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Import necessary libraries (Symbolic Math Toolbox and ODE solver).
syms x y(x) C1

% Define the initial condition for the IVP.
% x0: initial x value, y0: initial y value
x0 = 0;
y0 = 1;

% Define the separable equation as a symbolic differential equation.
% The equation has the form dy/dx = x*y which is separable and solvable analytically.
separableEquation = diff(y, x) == x * y;

% Solve the separable equation analytically using dsolve.
% dsolve returns the general solution including integration constant C1.
analyticalSolution = dsolve(separableEquation);

% Print the general analytical solution for instructional purposes.
disp('Analytical General Solution:');
disp(analyticalSolution);

% Apply the initial condition symbolically and solve for the constant C1.
initialCondition = subs(analyticalSolution, x, x0) == y0;
constValue = solve(initialCondition, C1);

% Print the value of the constant for verification.
disp('Value of Constant:');
disp(constValue);

% Substitute the value of C1 back into the analytical solution to get specific solution.
specificSolution = subs(analyticalSolution, C1, constValue);

% Print the specific analytical solution with the initial condition applied.
disp('Analytical Specific Solution:');
disp(specificSolution);

% Generate a numeric grid for plotting the analytical solution between 0 and 2.
% Using 100 points yields a smooth curve for comparison with the numerical solver.
xAnalytical = linspace(0, 2, 100);
yAnalytical = double(subs(specificSolution, x, xAnalytical));

% Define the separable equation as a function handle for numeric solver (ode45).
% f(t,y) should return dy/dt (or dy/dx) given scalar inputs; use element-wise ops.
f = @(x, y) x .* y; % Define the separable equation as a function.
% Initial condition y(0) = 1.
[xNumerical, yNumerical] = ode45(f, [0, 2], 1); 

% Plot the numerical solution as red dots to show discrete solver output.
plot(xNumerical, yNumerical, 'ro', 'MarkerSize', 4, 'DisplayName', 'Numerical Solution');

% Hold the plot and overlay the analytical solution (continuous blue line).
hold on;
plot(xAnalytical, yAnalytical, 'b-', 'LineWidth', 1.5, 'DisplayName', 'Analytical Solution');

% Label the axes and add a title to explain the figure.
xlabel('x');
ylabel('y');
title('Solving Separable Equation: Analytical vs. Numerical');

% Add a legend to distinguish between numerical and analytical solutions.
legend('show');

% Add a grid to improve readability of the plot.
grid on;

% Save the plot as a PNG file with a descriptive filename for lecture materials.
saveas(gcf, 'Lecture_03_Lab_Exercise_1_Separable.png');
