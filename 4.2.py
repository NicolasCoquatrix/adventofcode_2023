import os #os.system("cls")

numbers = ["0","1","2","3","4","5","6","7","8","9"]
cards = []
for line in range (218) : 
    text = input("")
    card = []
    for character in range (len(text)) :
        card += [text[character]]
    cart_part = "start"
    cards += [[[],[],[],[]]]
    for character in range (len(card)) :
        if card[character] == ":" :
            cart_part = "win_part"
        elif card[character] == "|" :
            cart_part = "game_part"
        character_increment = 0
        number = ""
        while card[character+character_increment] in numbers :
            number += card[character+character_increment]
            card[character+character_increment] = "X"
            if character+character_increment != len(card)-1 :
                character_increment += 1
            else :
                break
        if number != "" :
            if cart_part == "start" :
                cards[line][0] += [number]
            elif cart_part == "win_part" :
                cards[line][1] += [number]
            elif cart_part == "game_part" :
                cards[line][2] += [number]
    cards[line][3] += [1]

final = 0
for line in range (len(cards)) :
    for copy in range (cards[line][3][0]) :
        final += 1
        os.system("cls")
        print(f"• CHARGEMENT : {line}/{len(cards)} •")
        line_increment = 1
        for number in range (len(cards[line][2])) :
            if cards[line][2][number] in cards[line][1] :
                cards[line+line_increment][3][0] += 1
                line_increment += 1


print(f"• FINAL = {final} •")