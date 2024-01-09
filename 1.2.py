numbers = ["0","1","2","3","4","5","6","7","8","9"]
number = ""
final = 0
for line in range (1000) : 
    text = input("").lower()
    for character in range (len(text)) : 
        if text[character] in numbers :
            number = text[character]
            break
        if character < len(text)-1 and text[character] == "o" :
            if text[character+1] == "n" :
                if text[character+2] == "e" :
                    number = "1"
                    break
        if character < len(text)-1 and text[character] == "t" :
            if text[character+1] == "w" :
                if text[character+2] == "o" :
                    number = "2"
                    break
        if character < len(text)-3 and text[character] == "t" :
            if text[character+1] == "h" :
                if text[character+2] == "r" :
                    if text[character+3] == "e" :
                        if text[character+4] == "e" :
                            number = "3"
                            break
        if character < len(text)-2 and text[character] == "f" :
            if text[character+1] == "o" :
                if text[character+2] == "u" :
                    if text[character+3] == "r" :
                        number = "4"
                        break
        if character < len(text)-2 and text[character] == "f" :
            if text[character+1] == "i" :
                if text[character+2] == "v" :
                    if text[character+3] == "e" :
                        number = "5"
                        break
        if character < len(text)-1 and text[character] == "s" :
            if text[character+1] == "i" :
                if text[character+2] == "x" :
                    number = "6"
                    break
        if character < len(text)-3 and text[character] == "s" :
            if text[character+1] == "e" :
                if text[character+2] == "v" :
                    if text[character+3] == "e" :
                        if text[character+4] == "n" :
                            number = "7"
                            break
        if character < len(text)-3 and text[character] == "e" :
            if text[character+1] == "i" :
                if text[character+2] == "g" :
                    if text[character+3] == "h" :
                        if text[character+4] == "t" :
                            number = "8"
                            break
        if character < len(text)-2 and text[character] == "n" :
            if text[character+1] == "i" :
                if text[character+2] == "n" :
                    if text[character+3] == "e" :
                        number = "9"
                        break
    for character in range (len(text)-1, -1, -1) : 
        if text[character] in numbers :
            number = number + text[character]
            break
        if character < len(text)-1 and text[character] == "o" :
            if text[character+1] == "n" :
                if text[character+2] == "e" :
                    number = number + "1"
                    break
        if character < len(text)-1 and text[character] == "t" :
            if text[character+1] == "w" :
                if text[character+2] == "o" :
                    number = number + "2"
                    break
        if character < len(text)-3 and text[character] == "t" :
            if text[character+1] == "h" :
                if text[character+2] == "r" :
                    if text[character+3] == "e" :
                        if text[character+4] == "e" :
                            number = number + "3"
                            break
        if character < len(text)-2 and text[character] == "f" :
            if text[character+1] == "o" :
                if text[character+2] == "u" :
                    if text[character+3] == "r" :
                        number = number + "4"
                        break
        if character < len(text)-2 and text[character] == "f" :
            if text[character+1] == "i" :
                if text[character+2] == "v" :
                    if text[character+3] == "e" :
                        number = number + "5"
                        break
        if character < len(text)-1 and text[character] == "s" :
            if text[character+1] == "i" :
                if text[character+2] == "x" :
                    number = number + "6"
                    break
        if character < len(text)-3 and text[character] == "s" :
            if text[character+1] == "e" :
                if text[character+2] == "v" :
                    if text[character+3] == "e" :
                        if text[character+4] == "n" :
                            number = number + "7"
                            break
        if character < len(text)-3 and text[character] == "e" :
            if text[character+1] == "i" :
                if text[character+2] == "g" :
                    if text[character+3] == "h" :
                        if text[character+4] == "t" :
                            number = number + "8"
                            break
        if character < len(text)-2 and text[character] == "n" :
            if text[character+1] == "i" :
                if text[character+2] == "n" :
                    if text[character+3] == "e" :
                        number = number + "9"
                        break
    final += int(number)
    print(f"Nombre = {number}, Final = {final}")
print(f"\n• FINAL = {final} •\n\n\n")
