

cities_handle = open('Cities3.txt')

for city in cities_handle:
    clean_city = city.strip()
    print(clean_city)

cities_handle.close()
