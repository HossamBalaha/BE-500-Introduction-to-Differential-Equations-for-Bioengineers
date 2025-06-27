% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Initial Creation Date: June 26th, 2025
% Last Modification Date: June 26th, 2025
% Permissions and Citation: Refer to the README file.

% Define symbolic variables.
syms t s C(t) X

% Set up biological parameters.
k = 0.5;      % Elimination rate constant (per hour).
R0 = 20;      % Constant infusion rate (mg/hr).
a = 2;        % Delay time before drug infusion starts (hours).
C0 = 0;       % Initial drug concentration at t = 0 (mg/L).

% Define derivative of C(t) for use in the differential equation.
dCdt = diff(C, t);
disp(['dC/dt: ', char(dCdt)]);

% Define the forcing function R(t) as a delayed step input (Heaviside
% function).
R = R0 * heaviside(t - a);  % Drug infusion starting at t = a.

% Write the full differential equation: dC/dt + k*C = R(t).
ode = dCdt + k * C == R;
disp(['Differential Equation: ', char(ode)]);

% Apply Laplace transform to the ODE.
Cs = laplace(ode, t, s);
disp(['Laplace Transform of C(s): ', char(Cs)]);

% Substitute Laplace transform of C(t) with symbol X.
Cs = subs(Cs, laplace(C, t, s), X);

% Substitute initial condition C(0) = C0 into the transformed equation.
Cs = subs(Cs, C(0), C0);

% Solve algebraically for X(s); this gives the solution in the s-domain.
solutionCs = solve(Cs, X);
disp(['Laplace Transform of C(s) with initial condition: ', char(solutionCs)]);

% Apply inverse Laplace transform to return to time domain.
solutionCt = ilaplace(solutionCs, s, t);

% Display final time-domain solution.
disp(['Concentration of the drug C(t): ', char(solutionCt)]);