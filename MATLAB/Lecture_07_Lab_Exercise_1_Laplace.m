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
syms t s a b c d real;

% Example 1: Laplace Transform of f(t) = t * exp(-2*t).
f1 = t * exp(-2 * t);
F1 = laplace(f1, t, s);

% Display result.
disp('=== Laplace Transform of f(t) = t * exp(-2*t) ===')
disp(['f(t) = ', char(f1)]);
disp(['F(s) = ', char(F1)]);
disp('');

% Example 2: Laplace Transform of f(t) = exp(-2t) * sin(3t).
f2 = exp(-2 * t) * sin(3 * t);
F2 = laplace(f2, t, s);

% Display result.
disp('=== Laplace Transform of f(t) = exp(-2t)*sin(3t) ===')
disp(['f(t) = ', char(f2)]);
disp(['F(s) = ', char(F2)]);
disp('');

% Example 3: Laplace Transform of f(t) = 1 - exp(-a*t)*(b*sin(c*t) +
% d*cos(c*t)).
f3 = 1 - exp(-a*t) * (b*sin(c*t) + d*cos(c*t));
F3 = laplace(f3, t, s);

% Display result.
disp('=== Laplace Transform of f(t) = 1 - exp(-a*t)*(b*sin(c*t) + d*cos(c*t)) ===')
disp(['f(t) = ', char(f3)]);
disp(['F(s) = ', char(F3)]);