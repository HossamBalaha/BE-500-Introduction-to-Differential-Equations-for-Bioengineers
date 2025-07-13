% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: July 12th, 2025
% Last Modification Date: July 12th, 2025
% Permissions and Citation: Refer to the README file.

clear; clc; close all;

% Parameters.
beta = 1.0; % Maximum production rate.
n = 1; % Hill coefficient.
k = 1.0; % Half-maximal effective concentration.
gamma = 0.1; % Degradation/dilution rate.
x0 = 0.5; % Initial condition for gene product concentration.
tSpan = [0, 50]; % Time span for the solution.
dt = 0.01; % Time step size.

% Solve using RK4.
f = @(x) HillEquation(x, beta, n, k, gamma);
[t, x] = RungeKutta4(f, x0, tSpan, dt);

% Compute the response of the Hill equation.
dxValues = arrayfun(@(xI) HillEquation(xI, beta, n, k, gamma), x);

% Find the equilibrium points.
equilibriumPoints = [];
for i = 0:50
    options = optimoptions('fsolve', 'Display', 'off', 'MaxIterations', 2500);
    equilibrium = fsolve(@(x) HillEquation(x, beta, n, k, gamma), i, options);
    if (length(equilibriumPoints) > 0)
        if (~all(any(abs(equilibriumPoints - equilibrium) < 1e-3)))
            equilibriumPoints = [equilibriumPoints; equilibrium];
        end
    elseif (length(equilibrium))
        equilibriumPoints = [equilibriumPoints; equilibrium];
    end
end

% Print the equilibrium points.
disp('Equilibrium Points:');
disp(equilibriumPoints');

% Check stability of equilibria.
stability = {};
for eq = equilibriumPoints'
    J = HillEquationDerivative(eq, beta, n, k, gamma);
    if J < 0
        stability{end+1} = {eq, 'Stable'};
    elseif J > 0
        stability{end+1} = {eq, 'Unstable'};
    else
        stability{end+1} = {eq, 'Neutral'};
    end
end

% Print stability of equilibria.
disp('Stability of Equilibria:');
for k = 1:length(stability)
    disp(['Equilibrium Point: ', mat2str(stability{k}{1}), ', Stability: ', stability{k}{2}]);
end

% Plot results.
figure;

% Solution plot.
subplot(2, 2, 1);
plot(t, x, 'LineWidth', 2);
xlabel('Time (t)', 'FontSize', 12);
ylabel('Concentration (x)', 'FontSize', 12);
title(sprintf('Solution of Hill Equation Using RK4 (n = %d and k = %.1f)', n, k), 'FontSize', 14);
legend('Gene Product Concentration');
grid on;

% Derivatives plot.
subplot(2, 2, 2);
plot(t, dxValues, 'LineWidth', 2);
xlabel('Time (t)', 'FontSize', 12);
ylabel('Hill Equation Response (dx/dt)', 'FontSize', 12);
title(sprintf('Response of Hill Equation Over Time (n = %d and k = %.1f)', n, k), 'FontSize', 14);
legend('Hill Equation Response');
grid on;

% Bifurcation diagram for varying k.
n = 1; % Set n to 1 for the bifurcation diagram.
kValues = linspace(0.1, 15, 500); % Range of k values.
stable = []; unstable = [];
for kValue = kValues
    eqPoints = [];
    for i = 0:50
        options = optimoptions('fsolve', 'Display', 'off', 'MaxIterations', 2500);
        equilibrium = fsolve(@(x) HillEquation(x, beta, n, kValue, gamma), i, options);
        if (length(eqPoints) > 0)
            if (~all(any(abs(eqPoints - equilibrium) < 1e-3)))
                eqPoints = [eqPoints; equilibrium];
            end
        elseif (length(equilibrium))
            eqPoints = [eqPoints; equilibrium];
        end
    end
    for eq = eqPoints'
        derivativeAtEq = HillEquationDerivative(eq, beta, n, kValue, gamma);
        if derivativeAtEq < 0
            stable = [stable; [kValue, eq]];
        elseif derivativeAtEq > 0
            unstable = [unstable; [kValue, eq]];
        end
    end
end

% Plot the bifurcation diagram.
subplot(2, 2, 3);
scatter(stable(:, 1), stable(:, 2), 20, 'b', 'filled');
hold on;
scatter(unstable(:, 1), unstable(:, 2), 20, 'r', 'x');
xlabel('Parameter (k)', 'FontSize', 12);
ylabel('Equilibrium Points (x)', 'FontSize', 12);
title('Bifurcation Diagram of Hill Equation (n = 1)', 'FontSize', 14);
legend('Stable Points', 'Unstable Points');
grid on;

% Bifurcation diagram for varying n.
k = 1.0; % Set k to 1 for the bifurcation diagram.
nValues = 1:10; % Range of n values.
stableN = []; unstableN = [];
for nValue = nValues
    eqPoints = [];
    for i = 0:50
        options = optimoptions('fsolve', 'Display', 'off', 'MaxIterations', 2500);
        equilibrium = fsolve(@(x) HillEquation(x, beta, nValue, k, gamma), i, options);
        if (length(eqPoints) > 0)
            if (~all(any(abs(eqPoints - equilibrium) < 1e-3)))
                eqPoints = [eqPoints; equilibrium];
            end
        elseif (length(equilibrium))
            eqPoints = [eqPoints; equilibrium];
        end
    end
    for eq = eqPoints'
        derivativeAtEq = HillEquationDerivative(eq, beta, nValue, k, gamma);
        if derivativeAtEq < 0
            stableN = [stableN; [nValue, eq]];
        elseif derivativeAtEq > 0
            unstableN = [unstableN; [nValue, eq]];
        end
    end
end

% Plot the bifurcation diagram for n.
subplot(2, 2, 4);
scatter(stableN(:, 1), stableN(:, 2), 20, 'b', 'filled');
hold on;
scatter(unstableN(:, 1), unstableN(:, 2), 20, 'r', 'x');
xlabel('Parameter (n)', 'FontSize', 12);
ylabel('Equilibrium Points (x)', 'FontSize', 12);
title('Bifurcation Diagram of Hill Equation (k = 1)', 'FontSize', 14);
legend('Stable Points', 'Unstable Points');
grid on;

% Save the figure.
saveas(gcf, 'Lecture_10_Lab_Exercise_1_Hill.png');

% Define the Hill equation function.
function result = HillEquation(x, beta, n, k, gamma)
result = (beta * (x.^n) ./ (k.^n + x.^n)) - (gamma * x);
end

% Define the derivative of the Hill equation.
function result = HillEquationDerivative(x, beta, n, k, gamma)
num = beta * (x.^n);
numDerivative = beta * n * (x.^(n-1));
den = k^n + x.^n;
denDerivative = n * (x.^(n-1));
result = ((numDerivative .* den - num .* denDerivative) ./ (den.^2)) - gamma;
end

% Implement the Runge-Kutta 4th order method for solving ODEs.
function [t, x] = RungeKutta4(f, x0, tSpan, dt)
t = tSpan(1):dt:tSpan(2); % Time vector.
x = zeros(size(t)); % Initialize solution array.
x(1) = x0; % Set initial condition.

for i = 2:length(t)
    k1 = f(x(i-1)) * dt;
    k2 = f(x(i-1) + k1/2) * dt;
    k3 = f(x(i-1) + k2/2) * dt;
    k4 = f(x(i-1) + k3) * dt;
    x(i) = x(i-1) + (k1 + 2*k2 + 2*k3 + k4) / 6;
end
end