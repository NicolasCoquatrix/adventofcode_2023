import os #os.system("cls")
import time #time.sleep()

race_data = [[61,430,0],[67,1036,0],[75,1307,0],[71,1150,0]]

for race in range (len(race_data)) :
    win_possibility = 0
    for seconde in range (race_data[race][0]-1) :
        distance = (race_data[race][0] - seconde) * seconde
        if distance > race_data[race][1] :
            race_data[race][2] += 1

final = 1
for race in range (len(race_data)) :
    final *= race_data[race][2]
        
os.system("cls")
print(f"• FINAL = {final} •\n\n\n")