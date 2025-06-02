% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: June 2nd, 2025
% Last Modification Date: June 2nd, 2025
% Permissions and Citation: Refer to the README file.

% Define natural frequency (1 Hz).
omega0 = 2 * pi;

% Define initial displacement and velocity.
y0 = [1.0, 0.0];

% Define time span for simulation.
tSpan = [0, 20];

% Generate time vector for plotting.
tEval = linspace(tSpan(1), tSpan(2), 1000);

% Define colors for plotting.
colors = {'black', 'blue', 'red', 'magenta', 'cyan'};

% Set parameters for each oscillation type.
valuesDict = {};
valuesDict.Undamped = struct('Gamma', 0.0, 'F0', 0.0, 'OmegaF', 0.0);
valuesDict.Underdamped = struct('Gamma', 0.5, 'F0', 0.0, 'OmegaF', 0.0);
valuesDict.CriticallyDamped = struct('Gamma', 2*pi, 'F0', 0.0, 'OmegaF', 0.0);
valuesDict.Overdamped = struct('Gamma', 3*pi, 'F0', 0.0, 'OmegaF', 0.0);
valuesDict.ForcedOscillation = struct('Gamma', 0.5, 'F0', 1.0, 'OmegaF', 2*pi);

% ==============================================================
% ========= Analytical Solutions for the Oscillations ==========
% ==============================================================

% Analytical solution for undamped oscillation.
A = y0(1);  % Initial displacement.
B = y0(2) / omega0;  % Initial velocity scaled by natural frequency.
xUndamped = A * cos(omega0 * tEval) + B * sin(omega0 * tEval);

% Analytical solution for underdamped oscillation.
omegad = sqrt(omega0^2 - valuesDict.Underdamped.Gamma^2);
A = y0(1);
B = y0(2) / omegad;
xUnderdamped = exp(-valuesDict.Underdamped.Gamma * tEval) .* ...
    (A * cos(omegad * tEval) + B * sin(omegad * tEval));

% Analytical solution for critically damped oscillation.
A = y0(1);
B = y0(2) / valuesDict.CriticallyDamped.Gamma;
xCritically = (A + B * tEval) .* ...
    exp(-valuesDict.CriticallyDamped.Gamma * tEval);

% Analytical solution for overdamped oscillation.
r1 = -valuesDict.Overdamped.Gamma + ...
    sqrt(valuesDict.Overdamped.Gamma^2 - omega0^2);
r2 = -valuesDict.Overdamped.Gamma - ...
    sqrt(valuesDict.Overdamped.Gamma^2 - omega0^2);
A = y0(1);
B = y0(2) / (r2 - r1);
xOverdamped = A * exp(r1 * tEval) + B * exp(r2 * tEval);

% ==============================================================
% ========== Numerical Solutions for the Oscillations ==========
% ==============================================================

% Solve ODEs numerically for all cases.
solutions = cell(1, length(fieldnames(valuesDict)));
keys = string(fieldnames(valuesDict));
for i = 1:length(fieldnames(valuesDict))
    key = keys(i);
    params = valuesDict.(key);

    % Solve IVP.
    [tNumerical, xNumerical] = ode45(@(t, y) HeartOscillations(t, y, omega0, ...
        params.Gamma, params.F0, params.OmegaF), ...
        tSpan, y0);

    % Store solution.
    solutions{i} = struct('t', tNumerical, 'y', xNumerical);
end

% ==============================================================
% ======================= Plot Results =========================
% ==============================================================

figure('Position', [10, 10, 2000, 800]);  % Create figure window.

% Subplot 1: Analytical Solutions.
subplot(1, 2, 1);
plot(tEval, xUndamped, 'Color', colors{1}, 'LineWidth', 1.5);
hold on;
plot(tEval, xUnderdamped, 'Color', colors{2}, 'LineWidth', 1.5);
plot(tEval, xCritically, 'Color', colors{3}, 'LineWidth', 1.5);
plot(tEval, xOverdamped, 'Color', colors{4}, 'LineWidth', 1.5);
hold off;

xlabel('Time (t)');
ylabel('Displacement x(t)');
title('Oscillations of the Heart (Analytical Solution)');
legend({'Undamped', 'Underdamped', 'Critically Damped', 'Overdamped'});
grid on;
set(gca, 'FontSize', 12);

% Subplot 2: Numerical Solutions.
subplot(1, 2, 2);
for i = 1:length(solutions)
    key = keys(i);
    plot(solutions{i}.t, solutions{i}.y(:,1), 'Color', colors{i}, 'LineWidth', 1.5);
    hold on;
end
hold off;

xlabel('Time (t)');
ylabel('Displacement x(t)');
title('Oscillations of the Heart (Numerical Solutions)');
legend(fieldnames(valuesDict));
grid on;

% Save the plot as a PNG file.
saveas(gcf, 'Lecture_04_Lab_Exercise_3_Heart.png');


function dydt = HeartOscillations(t, y, omega0, gamma, F0, omegaF)
% Defines the system of ordinary differential equations (ODEs) for heart oscillations.
%
% Parameters:
% t (float): Time variable.
% y (vector): State variables [x, v].
% omega0 (float): Natural angular frequency.
% gamma (float): Damping coefficient.
% F0 (float): Amplitude of external forcing.
% omegaF (float): Frequency of external forcing.
%
% Returns:
% dydt (vector): Derivatives [dx/dt, dv/dt].

x = y(1); % Displacement.
v = y(2); % Velocity.

dxdt = v; % Derivative of displacement is velocity.

dvdt = -2 * gamma * v - omega0^2 * x + F0 * cos(omegaF * t);  % Acceleration.

dydt = [dxdt; dvdt]; % Return derivatives.
end