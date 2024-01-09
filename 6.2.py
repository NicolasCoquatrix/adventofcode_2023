import os #os.system("cls")
import time #time.sleep()

race_data = [61677571,430103613071150]
final = 0
counter = 999999

win_possibility = 0
for seconde in range (race_data[0]-1) :
    distance = (race_data[0] - seconde) * seconde
    if distance > race_data[1] :
        final += 1

    # Affichage de l'avancement
    counter += 1
    if counter == 1000000 :
        os.system("cls")
        print(f"• CHARGEMENT : {round(seconde*100/race_data[0])}/100 •")
        counter = 0
 
os.system("cls")
print(f"• FINAL = {final} •\n\n\n")