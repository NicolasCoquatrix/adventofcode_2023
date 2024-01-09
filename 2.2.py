final = 0
for line in range (100) :
    text = input("")
    max_red = 0
    for character in range (len(text)) : 
        if character < len(text)-1 and text[character] == "r" :
            if text[character+1] == "e" :
                if text[character+2] == "d" :
                    red = text[character-2]
                    if text[character-3] != " " :
                        red = text[character-3] + red
                    red = int(red)
                    if red > max_red :
                        max_red = red
    max_green = 0
    for character in range (len(text)) : 
        if character < len(text)-3 and text[character] == "g" :
            if text[character+1] == "r" :
                if text[character+2] == "e" :
                    if text[character+3] == "e" :
                        if text[character+4] == "n" :
                            green = text[character-2]
                            if text[character-3] != " " :
                                green = text[character-3] + green
                            green = int(green)
                            if green > max_green :
                                max_green = green
    max_blue = 0
    for character in range (len(text)) : 
        if character < len(text)-2 and text[character] == "b" :
            if text[character+1] == "l" :
                if text[character+2] == "u" :
                    if text[character+3] == "e" :
                        blue = text[character-2]
                        if text[character-3] != " " :
                            blue = text[character-3] + blue
                        blue = int(blue)
                        if blue > max_blue :
                            max_blue = blue
    final += max_red * max_green * max_blue

    print(f"Rouge = {max_red}, Vert = {max_green}, Bleu = {max_blue}, Final = {final}")
print(f"\n• FINAL = {final} •\n\n\n")