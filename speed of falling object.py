import math

print('Welcome to the velocity calculator. Please enter the following: \n')

m = float(input('mass (in kg): '))
g = float(input('acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter: '))
t = float(input('time (in seconds)'))
p = float(input('density of fluid (1.3 kg/m^3 for air, 1000kg/m^3 for water): '))
A = float(input('cross section area of projectile (in square meters): '))
C = float(input('drag constant/coefficient (0.5 for sphere, 1.1 for cylinder): '))


c = (1 / 2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))


print() 
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")