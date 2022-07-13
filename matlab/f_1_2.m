%% numerical results
vx = zeros(1000,1);
vy = zeros(1000,1);
nx = zeros(1000,1);
ny = zeros(1000,1);
pi = 3.14159265358979;
dt = 0.1;
% dt = 0.05;
% dt = 0.15;

% alpha = 1/6 pi
alpha = 1/6;
vx(1) = 90 * cospi(alpha);
vy(1) = 90 * sinpi(alpha);
g = 9.8;
for i = 2:1:1000
     vx(i) = vx(i-1) * (1-dt);
     vy(i) = vy(i-1) * (1-dt) - g * dt;
     nx(i) = nx(i-1) + vx(i-1) * dt;
     ny(i) = ny(i-1) + vy(i-1) * dt;
end

%% Analytical results

ax = zeros(1000,1);
ay = zeros(1000,1);
for i = 1:1:1000
     ax(i) = vx(1) * (1-exp(-dt * i));
     ay(i) = (vy(1) + g) * (1-exp(-dt * i)) - g * dt * i;
end

%% plotting

t = 0:dt:dt * 999;
% scatter(dt * i, sqrt(nx(i)^2 + ny(i)^2) - sqrt(ax(i)^2 + ay(i)^2),1, 'blue', 'filled');
xlabel("Time (s)");
ylabel("Numerical Error (m)");
title("Error Caused by Numerical Method");
plot(t, sqrt(nx.^2 + ny.^2) - sqrt(ax.^2 + ay.^2));
hold on