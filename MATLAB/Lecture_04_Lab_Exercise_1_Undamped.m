% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Set the parameters.
omega0 = 2 * pi; % Natural frequency (1 Hz, radians per second).
A = 1.0; % Amplitude of oscillation.

% Generate 1000 time points for high-resolution plotting.
t = linspace(0, 5, 1000);

% Calculate displacement x(t) for two cases of phase/amplitude B.
% Case 1: B = 0.0 (no phase shift).
B1 = 0.0;
x1 = A * cos(omega0 * t) + B1 * sin(omega0 * t);

% Case 2: B = 1.0 (with phase shift).
B2 = 1.0;
x2 = A * cos(omega0 * t) + B2 * sin(omega0 * t);

% Plotting.
figure;  % Create a new figure.
plot(t, x1, 'b', 'LineWidth', 1.5); 
hold on;
plot(t, x2, 'r--', 'LineWidth', 1.5);

title('Undamped Oscillation');
xlabel('Time (t)');
ylabel('Displacement x(t)');
legend({'B = 0.0', 'B = 1.0'});
grid on;
axis tight; % Adjust axis limits to fit data tightly.
hold off;

% Save the plot as a PNG file for lecture materials.
saveas(gcf, 'Lecture_04_Lab_Exercise_1_Undamped.png');