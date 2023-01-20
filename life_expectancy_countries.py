

with open ('life-expectancy.csv') as life_expectancy_file:


    for line in life_expectancy_file:
        parts = line.split(',')
        country = parts[0].strip()
        year = int(parts[2])
        life_expectancy = float(parts[3].strip())
        yearinput = list(map(int(input("Enter the year of interest "))))

        


         