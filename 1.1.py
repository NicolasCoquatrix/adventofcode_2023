numbers = ["0","1","2","3","4","5","6","7","8","9"]
number = ""
final = 0
for line in range (1000) : 
    text = input("")
    for lettre in range (len(text)) : 
        if text[lettre] in numbers :
            number = text[lettre]
            break
    for lettre in range (len(text)-1, -1, -1) : 
        if text[lettre] in numbers :
            number = number + text[lettre]
            break
    final += int(number)
    print(f"Nombre = {number}, Final = {final}")
print(f"\n• FINAL = {final} •\n\n\n")
