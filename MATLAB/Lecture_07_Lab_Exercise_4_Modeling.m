% ===========================================================================
%         ╦ ╦┌─┐┌─┐┌─┐┌─┐┌┬┐  ╔╦╗┌─┐┌─┐┌┬┐┬ ┬  ╔╗ ┌─┐┬  ┌─┐┬ ┬┌─┐
%         ╠═╣│ │└─┐└─┐├─┤│││  ║║║├─┤│ ┬ ││└┬┘  ╠╩╗├─┤│  ├─┤├─┤├─┤
%         ╩ ╩└─┘└─┘└─┘┴ ┴┴ ┴  ╩ ╩┴ ┴└─┘─┴┘ ┴   ╚═╝┴ ┴┴─┘┴ ┴┴ ┴┴ ┴
% ===========================================================================
%
% Author: Hossam Magdy Balaha
% Permissions and Citation: Refer to the README file.

% Define symbolic variables.
syms t s x(t) X

% Set up the parameters.
x0 = 2;
v0 = -1;

% Define the derivatives.
dxdt = diff(x, t);
d2xdt2 = diff(x, t, 2);
disp(['dX/dt: ', char(dxdt)]);
disp(['d2X/dt2: ', char(d2xdt2)]);

% Define the differential equation.
ode = d2xdt2 + 2*dxdt + 5*x == 0;
disp(['Differential Equation: ', char(ode)]);

% Apply Laplace transform to both sides of the equation.
laplaceEqu = laplace(ode, t, s);
disp(['Laplace Transform: ', char(laplaceEqu)]);

% Substitute initial conditions into the Laplace domain equation.
% Replace laplace(x(t)) with X(s).
laplaceEqu = subs(laplaceEqu, laplace(x, t, s), X);
laplaceEqu = subs(laplaceEqu, x(0), x0);
laplaceEqu = subs(laplaceEqu, subs(diff(x, t), t, 0), v0);

% Solve algebraically for X(s).
solutionXs = solve(laplaceEqu, X);
disp(['Laplace Transform with initial condition: ', char(solutionCs)]);

% Apply inverse Laplace transform to return to time domain.
solutionXt = ilaplace(solutionXs, s, t);
disp(['X(t): ', char(solutionXt)]);

% Simplify the expression.
solutionXt = simplify(solutionXt);
disp(['Simplified X(t): ', char(solutionXt)]);