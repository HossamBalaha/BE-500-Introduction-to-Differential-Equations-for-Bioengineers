% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Create a grid of initial conditions for the 1D system.
xVals = linspace(-15, 15, 50); % Range of x values for the 1D system.
X = xVals;

% Compute the vector field for the 1D system.
U = zeros(size(X)); % Initialize velocity component for the 1D system.
for i = 1:length(X)
    state = [X(i)]; % Unpack the state variable for the 1D system.
    derivatives = System1D(0, state); % Compute the derivative.
    U(i) = derivatives; % Store the derivative in U.
end

% Normalize the vector field for the 1D system.
magnitude = sqrt(U.^2 + 1); % Magnitude for normalization.
UNormalized = U ./ magnitude; % Normalize the horizontal component.
V = 1.0 ./ magnitude; % Normalize the vertical component.

% Plot the vector field for the 1D system.
figure;
quiver(X, zeros(size(X)), UNormalized, V, 'b'); % Plot vector field using quiver.
xlabel('x');
ylabel('dx/dt');
title('Phase Portrait for 1D System');

% Add trajectories for the 1D system.
initialConditions = [-2.5, 0.0, 2.5]; % Example initial conditions for the 1D system.
tSpan = [0, 25]; % Time span for integration for the 1D system.
tEval = linspace(tSpan(1), tSpan(2), 1000);

hold on;
for ic = initialConditions
    % Solve the system for each initial condition for the 1D system.
    [t, y] = ode45(@(t, state) System1D(t, state), tSpan, ic);
    plot(t, y, 'LineWidth', 1.5); % Plot the trajectory for the 1D system.
    plot(t(1), y(1), 'r*', 'MarkerSize', 10); % Plot the starting point as a star.
end
legend('Trajectory 1', 'Trajectory 2', 'Trajectory 3');
grid on;
saveas(gcf, 'Lecture_09_Lab_Exercise_1_Phase1D.png'); % Save the plot.
hold off;

% Create a grid of initial conditions for the 2D system.
xVals = linspace(-10, 50, 100); % Range of x values.
yVals = linspace(-10, 50, 100); % Range of y values.
[X, Y] = meshgrid(xVals, yVals); % Create a grid.

% Compute the vector field for the 2D system.
alpha = 1.0; % Parameter alpha.
beta = 0.1; % Parameter beta.
gamma = 1.0; % Parameter gamma.
delta = 0.05; % Parameter delta.
params = [alpha, beta, gamma, delta]; % Parameters for the system.
U = zeros(size(X)); V = zeros(size(Y)); % Initialize velocity components.
for i = 1:size(X, 1)
    for j = 1:size(X, 2)
        state = [X(i, j), Y(i, j)];
        derivatives = System2D(0, state, params);
        U(i, j) = derivatives(1); V(i, j) = derivatives(2);
    end
end

% Plot the vector field for the 2D system.
figure;
quiver(X, Y, U, V, 'LineWidth', 0.5, 'Color', 'b'); % Plot vector field using streamslice.
xlabel('x');
ylabel('y');
title('Phase Portrait for 2D System');

% Add trajectories for the 2D system.
initialConditions = [
    0, 0;
    10, 5;
    20, 10;
    15, 5;
    15, 15;
    ];
tSpan = [0, 25]; % Time span for integration.
tEval = linspace(tSpan(1), tSpan(2), 500);

hold on;
for k = 1:size(initialConditions, 1)
    ic = initialConditions(k, :);
    % Solve the system for each initial condition for the 2D system.
    [t, y] = ode45(@(t, state) System2D(t, state, params), tSpan, ic);
    plot(y(:, 1), y(:, 2), 'LineWidth', 1.5); % Plot the trajectory.
    plot(y(1, 1), y(1, 2), '*', 'MarkerSize', 10); % Plot the starting point as a star.
    plot(y(end, 1), y(end, 2), 'o', 'MarkerSize', 10); % Plot the end point as a circle.
end
legend('Trajectory 1', 'Trajectory 2', 'Trajectory 3', 'Trajectory 4', 'Trajectory 5');
grid on;
saveas(gcf, 'Lecture_09_Lab_Exercise_1_Phase2D.png'); % Save the plot.
hold off;


% Define the System1D function for a 1D system.
function dxdt = System1D(~, state)
x = state(1); % Unpack the state variable.
dxdt = -x * (x - 1) * (x + 1); % Derivative of x.
end

% Define the System2D function for a 2D system.
function dstate = System2D(~, state, params)
x = state(1); y = state(2); % Unpack the state variables.
alpha = params(1); beta = params(2); gamma = params(3); delta = params(4); % Unpack parameters.
dxdt = alpha * x - beta * x * y; % Derivative of x.
dydt = -gamma * y + delta * x * y; % Derivative of y.
dstate = [dxdt; dydt];
end
