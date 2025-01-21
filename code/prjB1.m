%incognita
s = tf('s');

%parametri del sistema
k = 100;
beta = 0.6;
alfa = deg2rad(30);
J = 800;

%parametri del regolatore
RR = 27946.6489566125*(7.95364424393846*s + 1) / (0.000136258885321618*s + 1);


%sistema lineare
s  = tf('s');
A = [0 1; -1/8+0.019245*pi -0.00075];
B = [0; sqrt(3)/1500];
C = [1  0];
D = [0];
GG = C*inv(s*eye(2) - A)*B + D;
%GG = 0.00067*sqrt(3)/(s^2+0.00075*s-0.0192*pi()*0.125);

LL = RR*GG;

poli = pole(LL);
disp('Poli:');
disp(poli);

zeri = zero(LL);
disp('Zeri:');
disp(zeri);


Ue = 72.1687836487032*pi;

X1e = 2*pi/3;
