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

% Example 1: Inverse Laplace Transform of F(s) = 1 / (s + 2).
F1 = 1 / (s + 2);
f1 = ilaplace(F1, s, t);

% Display result.
disp('=== Inverse Laplace Transform of F(s) = 1/(s + 2) ===')
disp(['F(s) = ', char(F1)]);
disp(['f(t) = ', char(f1)]);
disp('');

% Example 2: Inverse Laplace Transform of F(s) = 3 / (s^2 + 9).
F2 = 3 / (s^2 + 9);
f2 = ilaplace(F2, s, t);

% Display result.
disp('=== Inverse Laplace Transform of F(s) = 3/(s^2 + 9) ===')
disp(['F(s) = ', char(F2)]);
disp(['f(t) = ', char(f2)]);
disp('');

% Example 3: Inverse Laplace Transform of F(s) = (b*s + d)/(s^2 + c^2).
F3 = (b * s + d) / (s^2 + c^2);
f3 = ilaplace(F3, s, t);

% Display result.
disp('=== Inverse Laplace Transform of F(s) = (b*s + d)/(s^2 + c^2) ===')
disp(['F(s) = ', char(F3)]);
disp(['f(t) = ', char(f3)]);
disp('');

% Example 4: Inverse Laplace Transform of F(s) = (s + 1)/(s^2 + 4*s + 5).
F4 = (s + 1) / (s^2 + 4*s + 5);
f4 = ilaplace(F4, s, t);

% Display result.
disp('=== Inverse Laplace Transform of F(s) = (s + 1)/(s^2 + 4s + 5) ===')
disp(['F(s) = ', char(F4)]);
disp(['f(t) = ', char(f4)]);