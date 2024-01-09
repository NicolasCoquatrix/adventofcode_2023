import time #time.sleep()

## DÉFINITION DES FONCTIONS ##
def plan_save(line,character,save,plan,line_comparator,axis_y,character_comparator,axis_x):
    while True :
        try :
            if line != line_comparator and character != character_comparator :
                save += [plan[line+axis_y][character+axis_x]]
                return save
        except ValueError :
            print("⚠ Erreur : plan_save ⚠")

def research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator,axis_y,character_comparator,axis_x):
    while True :
        try :
            gear_increment = 0
            number = ""
            if line != line_comparator and character != character_comparator :
                if plan[line+axis_y][character+axis_x] in numbers :
                    gear += 1
                    while plan[line+axis_y][character+axis_x+gear_increment] in numbers :
                        if character+axis_x+gear_increment != 0 :
                            gear_increment -= 1
                        else :
                            break
                    if plan[line+axis_y][character+axis_x+gear_increment] not in numbers :
                        gear_increment += 1
                    while plan[line+axis_y][character+axis_x+gear_increment] in numbers :
                        number += plan[line+axis_y][character+axis_x+gear_increment]
                        plan[line+axis_y][character+axis_x+gear_increment] = "."
                        if character+axis_x+gear_increment != len(plan[line])-1 :
                            gear_increment += 1
                        else :
                            break
                    multiplication = multiplication * int(number)
                    gear_multiplication_save = [gear,multiplication,save]
                    return gear_multiplication_save
                else :
                    return gear_multiplication_save
            else :
                return gear_multiplication_save
        except ValueError :
            print("⚠ Erreur : research ⚠")

def plan_restitution(line,character,save,plan,save_increment,line_comparator,axis_y,character_comparator,axis_x):
    while True :
        try :
            if line != line_comparator and character != character_comparator :
                plan[line+axis_y][character+axis_x] = save[save_increment]
                save_increment += 1
                return save_increment
        except ValueError :
            print("⚠ Erreur : plan_restitution ⚠")


## PROGRAMME ##
plan = []
# Création du schéma
for line in range (140) :
    plan += [[]]
    text = input ("")
    for character in range (len(text)) :
        plan[line] += [text[character]]

numbers = ["0","1","2","3","4","5","6","7","8","9"]
final = 0
# Recherche des engrenages
for line in range (len(plan)) :
    for character in range (len(plan[line])) :
        save = []
        gear = 0
        multiplication = 1
        gear_multiplication_save = []
        
        if plan[line][character] == "*" :
            line_comparator_top = 0
            axis_y_top = -1
            line_comparator_bottom = len(plan)-1
            axis_y_bottom = 1
            line_comparator_usless = -99
            axis_y_usless = 0
            character_comparator_right = len(plan[line])-1
            axis_x_right = 1
            character_comparator_left = 0
            axis_x_left = -1
            character_comparator_usless = -99
            axis_x_usless = 0

            # Sauvegarde
            save = []
            # Haut
            save = plan_save(line,character,save,plan,line_comparator_top,axis_y_top,character_comparator_usless,axis_x_usless)
            # Haut droit
            save = plan_save(line,character,save,plan,line_comparator_top,axis_y_top,character_comparator_right,axis_x_right)
            # Droite
            save = plan_save(line,character,save,plan,line_comparator_usless,axis_y_usless,character_comparator_right,axis_x_right)
            # Bas droit
            save = plan_save(line,character,save,plan,line_comparator_bottom,axis_y_bottom,character_comparator_right,axis_x_right)
            # Bas
            save = plan_save(line,character,save,plan,line_comparator_bottom,axis_y_bottom,character_comparator_usless,axis_x_usless)
            # Bas gauche
            save = plan_save(line,character,save,plan,line_comparator_bottom,axis_y_bottom,character_comparator_left,axis_x_left)
            # Gauche
            save = plan_save(line,character,save,plan,line_comparator_usless,axis_y_usless,character_comparator_left,axis_x_left)
            # Haut Gauche
            save = plan_save(line,character,save,plan,line_comparator_top,axis_y_top,character_comparator_left,axis_x_left)

            # Analyse
            # Haut
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_top,axis_y_top,character_comparator_usless,axis_x_usless)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Haut droit
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_top,axis_y_top,character_comparator_right,axis_x_right)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Droite
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_usless,axis_y_usless,character_comparator_right,axis_x_right)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Bas droit
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_bottom,axis_y_bottom,character_comparator_right,axis_x_right)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Bas
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_bottom,axis_y_bottom,character_comparator_usless,axis_x_usless)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Bas gauche
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_bottom,axis_y_bottom,character_comparator_left,axis_x_left)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Gauche
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_usless,axis_y_usless,character_comparator_left,axis_x_left)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            # Haut gauche
            gear_multiplication_save = research(line,character,save,plan,numbers,gear,multiplication,gear_multiplication_save,line_comparator_top,axis_y_top,character_comparator_left,axis_x_left)
            if len(gear_multiplication_save) == 3 :
                gear = gear_multiplication_save[0]
                multiplication = gear_multiplication_save[1]
                save = gear_multiplication_save[2]
            
            # Restitution du schéma
            save_increment = 0
            # Haut
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_top,axis_y_top,character_comparator_usless,axis_x_usless)
            # Haut droit
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_top,axis_y_top,character_comparator_right,axis_x_right)
            # Droite
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_usless,axis_y_usless,character_comparator_right,axis_x_right)
            # Bas droit
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_bottom,axis_y_bottom,character_comparator_right,axis_x_right)
            # Bas
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_bottom,axis_y_bottom,character_comparator_usless,axis_x_usless)
            # Bas gauche
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_bottom,axis_y_bottom,character_comparator_left,axis_x_left)
            # Gauche
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_usless,axis_y_usless,character_comparator_left,axis_x_left)
            # Haut Gauche
            save_increment = plan_restitution(line,character,save,plan,save_increment,line_comparator_top,axis_y_top,character_comparator_left,axis_x_left)

            # Ajout au final
            if gear >= 2 :
                final += multiplication

print(f"\n• FINAL = {final} •\n\n\n")

