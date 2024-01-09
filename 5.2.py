import os #os.system("cls")
import time #time.sleep()

# Création de la base de données
advent_input = ""
statut = -1
subsection_line = -1
numbers = ["0","1","2","3","4","5","6","7","8","9"]
database = [[],[],[],[],[],[],[],[]]
seeds_range = -1
first_seed_range = True
while advent_input != "stop" :
    # Saisie d'une ligne
    advent_input = input("")
    if advent_input != "stop" :

        # Création d'une sous-section
        if subsection_line >= 0 and statut > 0 :
            database[statut] += [[]]

        # Transformation de la ligne, chaîne de caractère en liste
        advent_input_list = []
        for character in range (len(advent_input)) :
            advent_input_list += [advent_input[character]]
        
        # Identification des nombres et des sections
        for character in range (len(advent_input_list)) :
            # Identification des sections
            if advent_input_list[character] == ":" :
                statut += 1
                subsection_line = -1
            
            # Écriture des nombres
            character_increment = 0
            number = ""
            while advent_input_list[character+character_increment] in numbers :
                number += advent_input_list[character+character_increment]
                advent_input_list[character+character_increment] = "X"
                if character+character_increment != len(advent_input_list)-1 :
                    character_increment += 1
                else :
                    break
            
            # Ajout des nombres dans les sections
            if number != "" :
                if statut == 0 :
                    if first_seed_range == True :
                        database[0] += [[]]
                        seeds_range += 1
                        database[0][seeds_range] += [int(number)]
                        first_seed_range = False
                    else :
                        database[0][seeds_range] += [int(number)]
                        first_seed_range = True
                elif statut > 0 :
                    database[statut][subsection_line] += [int(number)]

    # Nouvelle ligne de sous-section
    subsection_line += 1

# Suppression des sections en trop
for section in range (1, len(database)-1):
    for i in range (2) :
        del(database[section][len(database[section])-1])

# Calcul du pourcentage pour l'affichage du chargement 
total_seed = 0
for seed_range in range (len(database[0])) :
    total_seed += database[0][seed_range][1]

# Convertions
counter = 99999
final = -1
actuel_seed = 0
for seed_range in range (len(database[0])) :
    additional_seed = database[0][seed_range][0]
    while additional_seed < database[0][seed_range][0]+database[0][seed_range][1] :
        actuel_seed += 1
        # Graine vers Sol (seed-to-soil)
        soil = additional_seed
        for line in range (len(database[1])) :
            if database[1][line][1] <= additional_seed <= database[1][line][1]+database[1][line][2]-1 :
                soil = additional_seed - database[1][line][1]
                soil = database[1][line][0] + soil
        additional_seed +=1

        # Sol vers Engrais (soil-to-fertilizer)
        fertilizer = soil
        for line in range (len(database[2])) :
            if database[2][line][1] <= soil <= database[2][line][1]+database[2][line][2]-1 :
                fertilizer = soil - database[2][line][1]
                fertilizer = database[2][line][0] + fertilizer

        # Engrais vers Eau (fertilizer-to-water)
        water = fertilizer
        for line in range (len(database[3])) :
            if database[3][line][1] <= fertilizer<= database[3][line][1]+database[3][line][2]-1 :
                water = fertilizer - database[3][line][1]
                water = database[3][line][0] + water

        # Eau vers Lumière (water-to-light)
        light = water
        for line in range (len(database[4])) :
            if database[4][line][1] <= water<= database[4][line][1]+database[4][line][2]-1 :
                light = water - database[4][line][1]
                light = database[4][line][0] + light

        # Lumière vers Température (light-to-temperature)
        temperature = light
        for line in range (len(database[5])) :
            if database[5][line][1] <= light<= database[5][line][1]+database[5][line][2]-1 :
                temperature = light - database[5][line][1]
                temperature = database[5][line][0] + temperature

        # Température vers Humidité (temperature-to-humidity)
        humidity = temperature
        for line in range (len(database[6])) :
            if database[6][line][1] <= temperature<= database[6][line][1]+database[6][line][2]-1 :
                humidity = temperature - database[6][line][1]
                humidity = database[6][line][0] + humidity

        # Humidité vers Emplacement (humidity-to-location)
        location = humidity
        for line in range (len(database[7])) :
            if database[7][line][1] <= humidity<= database[7][line][1]+database[7][line][2]-1 :
                location = humidity - database[7][line][1]
                location = database[7][line][0] + location

        # Calcul de l'emplacement le plus proche
        if final == -1 or location < final :
            final = location
        
        # Affichage de l'avancement
        counter += 1
        if counter == 100000 :
            os.system("cls")
            print(f"• CHARGEMENT : {round(actuel_seed*100/total_seed,1)}/100 •")
            counter = 0

os.system("cls")
print(f"\n\nDATABASE = {database}\n\n")
print(f"• FINAL = {final} •\n\n\n")




        
