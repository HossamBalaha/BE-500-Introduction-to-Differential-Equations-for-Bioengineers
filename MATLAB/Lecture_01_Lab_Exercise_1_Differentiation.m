% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: May 14th, 2025
% Last Modification Date: May 26th, 2025
% Permissions and Citation: Refer to the README file.

% Import necessary toolboxes (Symbolic Math Toolbox is required for symbolic computations).
syms x;  % Define the symbolic variable 'x'.

% Define the function f(x) = x^3 + 2x^2 - 5x + 1.
f = x^3 + 2*x^2 - 5*x + 1;

% Compute the derivative of the function f(x).
fPrime = diff(f, x);  % Differentiate f(x) with respect to x.

disp('Function:'); 
disp(f);  % Display the symbolic function.
disp('Derivative:'); 
disp(fPrime);  % Display the symbolic derivative.

% Generate x values for plotting over the range [-5, 5] with 500 points.
xVals = linspace(-5, 5, 500)';  % Create an array of 500 evenly spaced values between -5 and 5.

% Convert the symbolic functions f(x) and f'(x) into numerical functions for evaluation.
fFunc = matlabFunction(f);  % Convert f(x) to a numerical function.
fVals = fFunc(xVals);  % Evaluate f(x) at each point in xVals.

fPrimeFunc = matlabFunction(fPrime);  % Convert f'(x) to a numerical function.
fPrimeVals = fPrimeFunc(xVals);  % Evaluate f'(x) at each point in xVals.

% Plot the original function f(x) and its derivative f'(x).
figure;  % Create a new figure.
plot(xVals, fVals, 'Color', 'red', 'LineWidth', 1.5); % Plot f(x) in red.
hold on;  
plot(xVals, fPrimeVals, 'Color', 'blue', 'LineStyle', '--', 'LineWidth', 1.5);  % Plot f'(x) in blue (dashed).

% Add title, axis labels, grid, and legend.
title('Function and Its Derivative');
xlabel('x');
ylabel('f(x) and f''(x)');
grid on;
legend('f(x)', 'f''(x)', 'Location', 'Best');
hold off;  % Release the plot hold.
