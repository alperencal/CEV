import pandas as pd

population_of_citys = {'Eskişehir': 887475, 'İzmir': 4455294, 'Muğla': 1021773, 'İstanbul': 16034511, 'Aydın': 1134031, 'Yalova': 262234, 'Afyonkarahisar': 774179}
population = pd.Series(population_of_citys)

area_of_citys = {'Eskişehir': 13960, 'İzmir': 11891, 'Muğla': 12654, 'İstanbul': 5461, 'Aydın': 8116, 'Yalova': 798, 'Afyonkarahisar': 14016}
area = pd.Series(area_of_citys)

table = pd.DataFrame({'population': population, 'area': area})
print(table)