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

% Underdamped:
% omega0 = 2 * pi; % Set the natural frequency (1 Hz, in radians per second).
% gamma = 0.1; % Set the damping coefficient (for example, 0.1).

% Underdamped (2):
% omega0 = 2 * pi; % Set the natural frequency (1 Hz, in radians per second).
% gamma = 1.25; % Set the damping coefficient (for example, 0.1).

% Critically damped:
% omega0 = 0.25 * pi; % Set the natural frequency (1 Hz, in radians per second).
% gamma = 0.25 * pi; % Set the damping coefficient (for example, 0.1).

% Overdamped:
% omega0 = 0.25 * pi; % Set the natural frequency (1 Hz, in radians per second).
% gamma = 1.25; % Set the damping coefficient (for example, 0.1).

% Define system parameters.
omega0 = 0.25 * pi; % Set the natural frequency (1 Hz, in radians per second).
gamma = 0.25 * pi; % Set the damping coefficient.
zeta = gamma / omega0; % Calculate the damping ratio.
A = 1.0; % Set the amplitude of oscillation.
B = 0.5; % Set the second amplitude (for phase shift).

% Generate 1000 time points from 0 to 25 seconds.
t = linspace(0, 25, 1000);

% Display system parameters.
fprintf('Parameters:\n');
fprintf('Natural Frequency (omega0): %.4f rad/s\n', omega0);
fprintf('Damping Coefficient (gamma): %.4f\n', gamma);
fprintf('Damping Ratio (zeta): %.4f\n', zeta);
fprintf('Amplitude (A): %.1f\n', A);
fprintf('Phase Shift Amplitude (B): %.1f\n', B);

% Underdamped case: zeta < 1.
if zeta < 1
    fprintf('\nUnderdamped Oscillation\n');
    fprintf('Solution: x(t) = exp(-gamma * t) * (A * cos(omegad * t) + B * sin(omegad * t))\n');
    fprintf('where omegad = sqrt(omega0^2 - gamma^2) is the damped natural frequency.\n');
    fprintf('where A and B are constants determined by initial conditions.\n');

    omegad = sqrt(omega0^2 - gamma^2); % Calculate the damped natural frequency.
    x = exp(-gamma * t) .* (A * cos(omegad * t) + B * sin(omegad * t)); % Compute displacement.

% Critically damped case: zeta == 1.
elseif zeta == 1
    fprintf('\nCritically Damped Oscillation\n');
    fprintf('Solution: x(t) = (A + B * t) * exp(-gamma * t)\n');
    fprintf('where A and B are constants determined by initial conditions.\n');

    x = (A + B * t) .* exp(-gamma * t); % Compute displacement.

% Overdamped case: zeta > 1.
else
    fprintf('\nOverdamped Oscillation\n');
    fprintf('Solution: x(t) = A * exp(r1 * t) + B * exp(r2 * t)\n');
    fprintf('where r1 and r2 are the roots of the characteristic equation and are real, distinct, and negative.\n');
    fprintf('where r1 = -gamma + sqrt(gamma^2 - omega0^2) and r2 = -gamma - sqrt(gamma^2 - omega0^2).\n');
    fprintf('where A and B are constants determined by initial conditions.\n');

    r1 = -gamma + sqrt(gamma^2 - omega0^2); % First root.
    r2 = -gamma - sqrt(gamma^2 - omega0^2); % Second root.
    x = A * exp(r1 * t) + B * exp(r2 * t); % Compute displacement.
end

% Plotting section.
figure; % Create a new figure.
plot(t, x, 'b', 'LineWidth', 1.5); % Plot displacement vs. time.
title('Damped Oscillation'); % Set the plot title.
xlabel('Time (t)'); % Label the x-axis as time.
ylabel('Displacement x(t)'); % Label the y-axis as displacement.
grid on; % Enable grid for better readability.
legend('Displacement x(t)', 'Location', 'Best'); % Show legend.
set(gca, 'FontSize', 12); % Set font size for axis labels.
axis tight; % Adjust axis limits to fit data tightly.

% Save the plot as a PNG file.
saveas(gcf, 'Lecture_04_Lab_Exercise_2_Damped.png');
