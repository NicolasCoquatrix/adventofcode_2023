numbers = ["0","1","2","3","4","5","6","7","8","9"]
final = 0
map = []
for line in range (140) :
    map += [[]]
    text = input ("")
    for character in range (len(text)) :
        map[line] += [text[character]]
for line in range (len(map)) :
    for character in range (len(map[line])) :
        part_number = False
        increment = 0
        number = ""
        while map[line][character+increment] in numbers :
            number += map[line][character+increment]
            map[line][character+increment] = "."
            # Bas
            if line != 139 :
                if map[line+1][character+increment] not in numbers and map[line+1][character+increment] != "." :
                    part_number = True
            # Haut
            if line != 0 :
                if map[line-1][character+increment] not in numbers and map[line-1][character+increment] != "." :
                    part_number = True
            # Droite
            if character+increment < len(map[line])-1 :
                if map[line][character+increment+1] not in numbers and map[line][character+increment+1] != "." :
                    part_number = True
            # Gauche
            if character+increment != 0 :
                if map[line][character+increment-1] not in numbers and map[line][character+increment-1] != "." :
                    part_number = True
            # Bas droit
            if line != 139 and character+increment < len(map[line])-1 :
                if map[line+1][character+increment+1] not in numbers and map[line+1][character+increment+1] != "." :
                    part_number = True
            # Bas gauche
            if line != 139 and character+increment != 0 :
                if map[line+1][character+increment-1] not in numbers and map[line+1][character+increment-1] != "." :
                    part_number = True
            # Haut droit
            if line != 0 and character+increment < len(map[line])-1 :
                if map[line-1][character+increment+1] not in numbers and map[line-1][character+increment+1] != "." :
                    part_number = True
            # Haut gauche
            if line != 0 and character+increment != 0 :
                if map[line-1][character+increment-1] not in numbers and map[line-1][character+increment-1] != "." :
                    part_number = True
            if character+increment < len(map[line])-1 :
                increment += 1
            else :
                break
        if part_number == True :
            final += int(number)
print(f"\n• FINAL = {final} •\n\n\n")

