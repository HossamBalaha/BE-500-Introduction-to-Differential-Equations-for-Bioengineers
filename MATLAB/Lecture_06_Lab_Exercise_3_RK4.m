% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: June 17th, 2025
% Last Modification Date: June 18th, 2025
% Permissions and Citation: Refer to the README file.

% Define simulation parameters.
C0 = 100;    % Initial concentration (mg/L).
k = 0.2;     % Elimination rate constant (1/hour).
h = 1;       % Time step (hours).
tSpan = [0 5];  % Time span (start, end).

% Generate numerical solutions
[tEuler, CEuler] = EulerMethod(C0, k, h, tSpan);
[tImpEuler, CImprovedEuler] = ImprovedEulerMethod(C0, k, h, tSpan);
[tRK4, CRK4] = RungeKutta4Method(C0, k, h, tSpan);

% Generate exact solution.
tExact = linspace(tSpan(1), tSpan(end), 100);
CExact = C0 * exp(-k * tExact);

% Calculate absolute error between RK4 and exact solution.
absError = abs(CRK4 - interp1(tExact, CExact, tRK4));

% Print simulation parameters.
fprintf('Parameters used in the simulation:\n');
fprintf('Initial concentration (C0): %.2f mg/L\n', C0);
fprintf('Rate constant (k): %.2f 1/h\n', k);
fprintf('Time step (h): %.2f hours\n', h);
fprintf('Time span: %.2f to %.2f hours\n\n', tSpan(1), tSpan(2));

% Display results as table.
fprintf('Time\tEuler\tImpr. Euler\tRK4\tExact\tAbs. Error\n');
for i = 1:length(tRK4)
  fprintf('%.2f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\n', ...
    tRK4(i), CEuler(i), CImprovedEuler(i), CRK4(i), ...
    interp1(tExact, CExact, tRK4(i)), absError(i));
end

% Create figure.
figure;
plot(tExact, CExact, 'r-', 'LineWidth', 1.5, 'DisplayName', 'Exact Solution');
hold on;
plot(tEuler, CEuler, 'bo-', 'DisplayName', 'Euler''s Method');
plot(tImpEuler, CImprovedEuler, 'go-', 'DisplayName', 'Improved Euler''s Method');
plot(tRK4, CRK4, 'mo-', 'DisplayName', 'Runge-Kutta 4th Order');
hold off;

% Labels and title.
xlabel('Time (hours)');
ylabel('Drug Concentration (mg/L)');
title('Numerical vs Exact Solutions for Drug Elimination.');
grid on;
legend('show');

% Save the plot as a PNG file.
saveas(gcf, 'Lecture_06_Lab_Exercise_3_RK4.png');

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

% Function: Runge-Kutta 4th Order Method.
function [t, y] = RungeKutta4Method(C0, k, h, tSpan)
t = tSpan(1):h:tSpan(2);
y = zeros(size(t));
y(1) = C0;
for i = 1:length(t)-1
  k1 = -k * y(i);
  k2 = -k * (y(i) + h/2 * k1);
  k3 = -k * (y(i) + h/2 * k2);
  k4 = -k * (y(i) + h * k3);
  y(i+1) = y(i) + (h / 6) * (k1 + 2*k2 + 2*k3 + k4);
end
end
