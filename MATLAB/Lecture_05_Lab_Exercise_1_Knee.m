% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: June 10th, 2025
% Last Modification Date: June 10th, 2025
% Permissions and Citation: Refer to the README file.

% Define parameters for the knee model
m = 1.0;         % Mass of the limb (kg)
c = 0.5;         % Damping coefficient (Ns/m)
k = 4.0;         % Spring constant (N/m)
F0 = 2.0;        % Amplitude of external force
omegaF = 3.0;    % Frequency of external force

% Initial conditions
y0 = [0.1; 0.0];  % y(1) = displacement, y(2) = velocity

% Time span for simulation
tSpan = [0, 50];   % From t = 0 to t = 50 seconds
tEval = linspace(tSpan(1), tSpan(2), 2500);  % Time vector for output

% ==============================================================
% ==================== Analytical Solution =====================
% ==============================================================

% Analytical solution from earlier derivation:
partA = exp(-0.25 * tEval) .* (0.467 * cos(1.984 * tEval) - 0.107 * sin(1.984 * tEval));
partB = -0.367 * cos(3 * tEval) + 0.11 * sin(3 * tEval);
analyticalSolution = partA + partB;  % Combined analytical solution

% ==============================================================
% ===================== Numerical Solution =====================
% ==============================================================

% Define the knee model as a function
KneeModel = @(t, y) KneeODE(t, y, c, k, F0, omegaF);

% Solve the ODE numerically
[tNumerical, yNumerical] = ode45(KneeModel, tSpan, y0);

% Extract numerical displacement (first state variable)
numericalSolution = yNumerical(:, 1);

% ==============================================================
% ========================= Plotting ==========================
% ==============================================================

% Create figure
figure;
plot(tEval, analyticalSolution, 'k', 'LineWidth', 2, 'DisplayName', 'Analytical Solution');
hold on;
plot(tNumerical, numericalSolution, 'r--', 'LineWidth', 2, 'DisplayName', 'Numerical Solution');

% Labels and title
xlabel('Time (t)');
ylabel('Displacement x(t)');
title('Knee Model: Analytical vs Numerical Solution');
grid on;
legend('show');
hold off;

% ==============================================================
% =============== Optional: Save the Figure ===================
% ==============================================================

% Save the plot as a PNG file.
saveas(gcf, 'Lecture_05_Lab_Exercise_1_Knee.png');

function dydt = KneeODE(t, y, c, k, F0, omegaF)
% KneeModel: Models knee motion as a spring-mass-damper system
% Inputs:
%   t      - Time
%   y      - State vector [x; v]
%   c      - Damping coefficient
%   k      - Spring constant
%   F0     - Forcing amplitude
%   omegaF - Forcing frequency

x = y(1);  % Displacement
v = y(2);  % Velocity

dxdt = v;
dvdt = -c * v - k * x + F0 * cos(omegaF * t);

dydt = [dxdt; dvdt];
end
