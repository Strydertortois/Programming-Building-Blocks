

def wind_chill_calc(air_temp, wind_speed):
    return 35.74 + 0.6215 * air_temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * air_temp * (wind_speed ** 0.16)

def celcius_to_fahrenheit(celcius_temp):
    return (celcius_temp * 1.8) + 32.00



air_temp = float(input('What is the air temp?: '))
temp_type = input('Is the temperature celcius or fahrenheit (C/F): ')

if temp_type == 'C':
    air_temp_calc = celcius_to_fahrenheit(air_temp)
else:
    air_temp_calc = air_temp

for wind_speed in range(5, 65, 5):
    chill = wind_chill_calc(air_temp_calc, wind_speed)
    print(f'At temperature {air_temp}{temp_type} and wind speed {wind_speed}, the windchill is: {round(chill, 2)}F')

    
    



