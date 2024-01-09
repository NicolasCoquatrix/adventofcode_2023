final = 0
numbers = ["0","1","2","3","4","5","6","7","8","9"]
for line in range (218) : 
    text = input("")
    card = []
    for character in range (len(text)) :
        card += [text[character]]
    win_numbers = []
    cart_part = "start"
    first_win_check = False
    points = 0
    for character in range (len(card)) :
        if card[character] == ":" :
            cart_part = "win_part"
        if cart_part == "win_part" :
            number = ""
            number_increment = 0
            while card[character+number_increment] in numbers :
                number += card[character+number_increment]
                card[character+number_increment] = "X"
                number_increment += 1
            if number != "" :
                win_numbers += [number]
        if card[character] == "|" :
            cart_part = "game_part"
        if cart_part == "game_part" :
            number = ""
            number_increment = 0
            while card[character+number_increment] in numbers :
                number += card[character+number_increment]
                card[character+number_increment] = "X"
                if character+number_increment != len(card)-1 :
                    number_increment += 1
                else :
                    break
            if number in win_numbers :
                if first_win_check == False :
                    points = 1
                    first_win_check = True
                else :
                    points = points * 2
    final += points
    
print(f"\n• FINAL = {final} •\n\n\n")
        

