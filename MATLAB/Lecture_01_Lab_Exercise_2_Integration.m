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

% Import necessary toolboxes (Symbolic Math Toolbox is optional for symbolic integration).
syms x;  % Define the symbolic variable 'x' if needed.

% Define the function f(x) = e^(-x^2).
f = @(x) exp(-x.^2);  % Anonymous function for f(x).

% Compute the definite integral of f(x) from 0 to 1 using integral().
result = integral(f, 0, 1);  % Use integral() to compute the definite integral.
disp(['Integral from 0 to 1: ', num2str(result)]);  % Display the computed integral value.

% Generate x values for plotting over the range [0, 1] with 500 points.
xVals = linspace(0, 1, 500)';  % Create an array of 500 evenly spaced values between 0 and 1.

% Evaluate the function f(x) at each point in x_vals.
yVals = f(xVals);  % Compute the y-values of the function f(x) for visualization.

% Plot the function and shade the area under the curve.
figure;  % Create a new figure.
plot(xVals, yVals, 'b', 'LineWidth', 1.5); 
hold on;  % Plot f(x) in blue with a line width of 1.5.

% Shade the area under the curve between x = 0 and x = 1.
xFill = [0; xVals; 1];  % Concatenate x-values: start at 0, go through xVals, and end at 1.
yFill = [0; yVals; 0];  % Concatenate y-values: start at 0, go through yVals, and return to 0.
fill(xFill, yFill, 'blue', 'FaceAlpha', 0.5);  % Fill the area under the curve.

% Add reference lines at x=0 and y=0 for better visualization.
line([0, 0], get(gca, 'YLim'), 'Color', 'black', 'LineWidth', 0.8, 'LineStyle', '--');  % Vertical line at x=0.
line(get(gca, 'XLim'), [0, 0], 'Color', 'black', 'LineWidth', 0.8, 'LineStyle', '--');  % Horizontal line at y=0.
line([1, 1], get(gca, 'YLim'), 'Color', 'black', 'LineWidth', 0.8, 'LineStyle', '--');  % Vertical line at x=1.

% Add title, axis labels, grid, and legend to the plot.
title('Area Under the Curve: Integral of f(x) = e^{-x^2} from 0 to 1');
xlabel('x');
ylabel('f(x)');
grid on;
legend('f(x) = e^{-x^2}', 'Location', 'Best');

hold off;  % Release the plot hold.
