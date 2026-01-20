% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Define simulation parameters.
C0 = 100;    % Initial concentration (mg/L).
k = 0.2;     % Elimination rate constant (1/hour).
h = 1;       % Time step (hours).
tSpan = [0 5];  % Time span (start, end).

% Generate numerical solutions
[tEuler, CEuler] = EulerMethod(C0, k, h, tSpan);
[tImpEuler, CImprovedEuler] = ImprovedEulerMethod(C0, k, h, tSpan);

% Generate exact solution.
tExact = linspace(tSpan(1), tSpan(end), 100);
CExact = C0 * exp(-k * tExact);

% Calculate absolute error between Improved Euler and exact solution.
absError = abs(CImprovedEuler - interp1(tExact, CExact, tEuler));

% Print simulation parameters.
fprintf('Parameters used in the simulation:\n');
fprintf('Initial concentration (C0): %.2f mg/L\n', C0);
fprintf('Rate constant (k): %.2f 1/h\n', k);
fprintf('Time step (h): %.2f hours\n', h);
fprintf('Time span: %.2f to %.2f hours\n\n', tSpan(1), tSpan(2));

% Display results as table.
fprintf('Time\tEuler\tImpr. Euler\tExact\tAbs. Error\n');
for i = 1:length(tEuler)
  fprintf('%.2f\t%.3f\t%.3f\t%.3f\t%.3f\n', ...
    tEuler(i), CEuler(i), CImprovedEuler(i), ...
    interp1(tExact, CExact, tEuler(i)), absError(i));
end

% Create figure.
figure;
plot(tExact, CExact, 'r-', 'LineWidth', 1.5, 'DisplayName', 'Exact Solution');
hold on;
plot(tEuler, CEuler, 'bo-', 'DisplayName', 'Euler''s Method');
plot(tImpEuler, CImprovedEuler, 'go-', 'DisplayName', 'Improved Euler''s Method');
hold off;

% Labels and title.
xlabel('Time (hours)');
ylabel('Drug Concentration (mg/L)');
title('Numerical vs Exact Solutions for Drug Elimination.');
grid on;
legend('show');

% Save the plot as a PNG file.
saveas(gcf, 'Lecture_06_Lab_Exercise_2_Improved.png');

% Function: Euler's Method.
function [t, y] = EulerMethod(C0, k, h, tSpan)
t = tSpan(1):h:tSpan(2);
y = zeros(size(t));
y(1) = C0;
for i = 1:length(t)-1
  y(i+1) = y(i) + h * (-k * y(i));
end
end

% Function: Improved Euler's Method (Heun's Method).
function [t, y] = ImprovedEulerMethod(C0, k, h, tSpan)
t = tSpan(1):h:tSpan(2);
y = zeros(size(t));
y(1) = C0;
for i = 1:length(t)-1
  slope1 = -k * y(i);
  yPred = y(i) + h * slope1;
  slope2 = -k * yPred;
  y(i+1) = y(i) + h * (slope1 + slope2) / 2.0;
end
end
