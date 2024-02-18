# -*- coding: utf-8 -*-
"""
[Graf algoritmi]: Zadatci za vjezbanje - 2. Zadaci s dictionaryjem - (e)

Dana je datoteka mapa-europa.net u kojoj su zapisani gradovi, avionske
linije i udaljenosti među gradovima. Spremiti u dictionary gradove i
udaljenosti na način da je ključ grad, a vrijednost lista uređenih parova
koji čine grad do kojih postoji let i udaljenost do tog grada. Pritom
voditi računa da ako postoji linija iz nekog grada u drugi grad, da postoji
i povratna linija. Napisati funkciju koja za neki grad vraća najbliži i
najdalji grad do kojeg postoji avionska linija.

@author: Anamarija Papic
"""

def read_data_to_dictionary(filename):
    d = {}
    
    with open(filename, 'r') as f:
        for line in f:
            city1, city2, distance = line.split()
            
            if city1 not in d.keys():
                d[city1] = [(city2, distance)]
            else:
                d[city1].append((city2, distance))
                
            if city2 not in d.keys():
                d[city2] = [(city1, distance)]
            else:
                d[city2].append((city1, distance))
                
    return d

def find_nearest_and_farthest(dictionary, city):
    if city not in dictionary.keys():
        raise Exception(f'No city named {city} found in dataset.')
    
    city_data = dictionary.get(city)
    cities_sorted = sorted(city_data, key=lambda x: int(x[1]))
    
    return (cities_sorted[0], cities_sorted[len(cities_sorted) - 1])
        

def main():
    d = read_data_to_dictionary('resources/mapa-europa.net')
    # print(d)
    
    try:
        print(find_nearest_and_farthest(d, 'London'))
        print(find_nearest_and_farthest(d, 'Amsterdam'))
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
