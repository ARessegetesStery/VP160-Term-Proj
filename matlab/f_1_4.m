%% numerical results
vx = zeros(1000,1);
vy = zeros(1000,1);
x = zeros(1000,1);
y = zeros(1000,1);
pi = 3.14159265358979;
dt = 0.1;
% dt = 0.05;
% dt = 0.15;
t = 0:dt:dt * 999;


% alpha = 1/6 pi
alpha = 1/6;
vx(1) = 90 * cospi(alpha);
vy(1) = 90 * sinpi(alpha);
g = 9.8;
for k = 0.5:0.25:1.5
    for i = 2:1:1000
        vx(i) = vx(i-1) * (1 - k * dt);
        vy(i) = vy(i-1) * (1 - k * dt) - g * dt;
        x(i) = x(i-1) + vx(i-1) * dt;
        y(i) = y(i-1) + vy(i-1) * dt;
    end
    % plot(x, y);
    plot(t, sqrt(vx.^2 + vy.^2));
    hold on;
end

