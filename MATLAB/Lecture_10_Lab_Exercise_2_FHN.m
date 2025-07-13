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
epsilon = 0.08; % Time scale separation.
a = 0.7; % Parameter for recovery variable.
b = 0.8; % Parameter for recovery variable.
I = 0.5; % External stimulus.
z0 = [1.0, 0.1]; % Initial conditions (v0, w0).
tSpan = [0, 100]; % Time span for the solution.
dt = 0.01; % Time step size.

% Solve using RK4.
f = @(z) FitzHughNagumo(z, epsilon, a, b, I);
[t, z] = RungeKutta4TwoDimensional(f, z0, tSpan, dt);

% Compute the response of the FitzHugh-Nagumo system.
dzValues = arrayfun(@(i) FitzHughNagumo(z(i, :), epsilon, a, b, I), 1:size(z, 1), 'UniformOutput', false);
dzValues = cell2mat(dzValues);

% Find equilibrium points.
equilibriumPoints = [];
for i = 0:50
    for j = 0:50
        % Solve for equilibrium points using fsolve.
        options = optimoptions('fsolve', 'Display', 'off', 'MaxIterations', 2500);
        equilibrium = fsolve(@(z) FitzHughNagumo(z, epsilon, a, b, I), [i, j], options);
        if (length(equilibriumPoints) > 0)
            if (~all(any(abs(equilibriumPoints - equilibrium) < 1e-5)))
                equilibriumPoints = [equilibriumPoints; equilibrium];
            end
        elseif (length(equilibrium))
            equilibriumPoints = [equilibriumPoints; equilibrium];
        end
    end
end

% Print equilibrium points.
disp('Equilibrium Points:');
disp(equilibriumPoints);


% Check stability of equilibria.
stability = {};
for k = 1:size(equilibriumPoints, 1)
    eq = equilibriumPoints(k, :);
    J = FitzHughNagumoDerivative(eq, epsilon, a, b, I);
    eigenvalues = eig(J); % Compute eigenvalues of the Jacobian.
    if all(real(eigenvalues) < 0)
        stability{end+1} = {eq, 'Stable'};
    elseif all(real(eigenvalues) == 0) && any(imag(eigenvalues) ~= 0)
        stability{end+1} = {eq, 'Periodic Behavior'};
    elseif any(real(eigenvalues) > 0)
        stability{end+1} = {eq, 'Unstable'};
    else
        stability{end+1} = {eq, 'Saddle Point (or Neutral)'};
    end
end

% Print stability of equilibria.
disp('Stability of Equilibria:');
for k = 1:length(stability)
    disp(['Equilibrium Point: ', mat2str(stability{k}{1}), ', Stability: ', stability{k}{2}]);
end

% Plot results.
figure;

% Solution of FitzHugh-Nagumo System Using RK4.
subplot(2, 2, 1);
plot(t, z(:, 1), 'LineWidth', 2); hold on;
plot(t, z(:, 2), 'LineWidth', 2);
xlabel('Time (t)', 'FontSize', 12);
ylabel('State Variables', 'FontSize', 12);
title('Solution of FitzHugh-Nagumo System Using RK4', 'FontSize', 14);
legend('v', 'w');
grid on;

% Response of FitzHugh-Nagumo System Over Time.
subplot(2, 2, 2);
plot(t, dzValues(1, :), 'LineWidth', 2); hold on;
plot(t, dzValues(2, :), 'LineWidth', 2);
xlabel('Time (t)', 'FontSize', 12);
ylabel('FitzHugh-Nagumo System Response', 'FontSize', 12);
title('Response of FitzHugh-Nagumo System Over Time', 'FontSize', 14);
legend('dv/dt', 'dw/dt');
grid on;

% Phase Portrait and Vector Field.
subplot(2, 2, 3);
N = 100; % Number of points in the grid for vector field.
xVals = linspace(-5, 5, N);
yVals = linspace(-5, 5, N);
[X, Y] = meshgrid(xVals, yVals);
U = zeros(size(X));
V = zeros(size(Y));

for i = 1:size(X, 1)
    for j = 1:size(X, 2)
        state = [X(i, j), Y(i, j)];
        derivatives = FitzHughNagumo(state, epsilon, a, b, I);
        U(i, j) = derivatives(1);
        V(i, j) = derivatives(2);
    end
end

% Solve the system for each initial condition.
initialConditions = [
    [1.0, 0.0];  % Initial condition 1.
    [2.0, 1.0];  % Initial condition 2.
    [3.0, 2.0];  % Initial condition 3.
    ];

for k = 1:size(initialConditions, 1)
    initCond = initialConditions(k, :);
    options = odeset('RelTol', 1e-6, 'AbsTol', 1e-6); % Set solver tolerances.
    [tSol, zSol] = ode45(@(t, z) FitzHughNagumo(z, epsilon, a, b, I), [0, 100], initCond, options);

    % Plot the trajectory.
    plot(zSol(:, 1), zSol(:, 2), 'LineWidth', 2); hold on;

    % Plot the starting point as a star.
    plot(zSol(1, 1), zSol(1, 2), 'r*', 'MarkerSize', 10); hold on;

    % Plot the end point as a circle.
    plot(zSol(end, 1), zSol(end, 2), 'go', 'MarkerSize', 10); hold on;
end

% Scatter equilibrium points.
scatter(equilibriumPoints(:, 1), equilibriumPoints(:, 2), 10, 'magenta', 'filled');


hold on;
quiver(X, Y, U, V, 'LineWidth', 0.5, 'Color', 'b');
xlabel('v', 'FontSize', 12);
ylabel('w', 'FontSize', 12);
title('Phase Portrait of FitzHugh-Nagumo System', 'FontSize', 14);
legend('Trajectory', 'Start Point', 'End Point', 'Equilibrium Points');
grid on;

% Bifurcation Diagram.
subplot(2, 2, 4);
extValues = linspace(0.0, 2.5, 10);
stable = [];
unstable = [];

for extValue = extValues
    eqPoints = [];
    for i = 0:50
        for j = 0:50
            options = optimoptions('fsolve', 'Display', 'off', 'MaxIterations', 2500);
            equilibrium = fsolve(@(z) FitzHughNagumo(z, epsilon, a, b, extValue), [i, j], options);
            if (length(eqPoints) > 0)
                if (~all(any(abs(eqPoints - equilibrium) < 1e-5)))
                    eqPoints = [eqPoints; equilibrium];
                end
            elseif (length(equilibrium))
                eqPoints = [eqPoints; equilibrium];
            end
        end
    end

    for k = 1:size(eqPoints, 1)
        eq = eqPoints(k, :);
        J = FitzHughNagumoDerivative(eq, epsilon, a, b, extValue);
        eigenvalues = eig(J);
        if all(real(eigenvalues) < 0)
            stable = [stable; extValue, eq];
        elseif any(real(eigenvalues) > 0)
            unstable = [unstable; extValue, eq];
        end
    end
end

scatter3(stable(1, :), stable(2, :), stable(3, :), 20, 'b', 'filled');
hold on;
scatter3(unstable(1, :), unstable(2, :), unstable(3, :), 20, 'r', 'x');
xlabel('Parameter (I)', 'FontSize', 12);
ylabel('v', 'FontSize', 12);
zlabel('w', 'FontSize', 12);
title('Bifurcation Diagram by Varying I', 'FontSize', 14);
legend('Stable Points', 'Unstable Points');
grid on;

saveas(gcf, 'Lecture_10_Lab_Exercise_2_FHN.png');

% FitzHugh-Nagumo Model for Neuron Dynamics.
function dz = FitzHughNagumo(z, epsilon, a, b, I)
v = z(1); % Membrane potential.
w = z(2); % Recovery variable.
dvdt = v - v^3 / 3 - w + I;
dwdt = epsilon * (v + a - b * w);
dz = [dvdt; dwdt];
end

% Derivative of the FitzHugh-Nagumo Model for Neuron Dynamics.
function J = FitzHughNagumoDerivative(z, epsilon, a, b, I)
v = z(1);
w = z(2);
J = [
    1 - v^2, -1;       % Derivative of dv/dt with respect to v and w.
    epsilon, -epsilon * b % Derivative of dw/dt with respect to v and w.
    ];
end

% Runge-Kutta 4th order method for solving ODEs.
function [t, z] = RungeKutta4TwoDimensional(f, z0, tSpan, dt)
t = tSpan(1):dt:tSpan(2);
z = [z0];

for i = 2:length(t)
    oldZ = z(i-1, :)';
    k1 = f(oldZ) * dt;
    k2 = f(oldZ + k1 / 2) * dt;
    k3 = f(oldZ + k2 / 2) * dt;
    k4 = f(oldZ + k3) * dt;
    result = oldZ + (k1 + 2*k2 + 2*k3 + k4) / 6;
    z = [z; result'];
end
end