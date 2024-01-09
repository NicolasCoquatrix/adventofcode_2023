import os #os.system("cls")
import time #time.sleep()

input_hand = ""
hands = [[],[],[],[],[],[],[]]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
while input_hand != "stop" :
    input_hand = input()
    if input_hand != "stop" :
        hand = ""
        bid = ""
        for hand_calculation in range (5) :
            hand += input_hand[hand_calculation]
        for bid_calculation in range (6, len(input_hand)) :
            bid += input_hand[bid_calculation]
        five_of_a_kind = False
        four_of_a_kind = False
        full_house = False
        three_of_a_kind = False
        two_pair = False
        one_pair = False
        for checked_card in range (len(hand)) :
            similar_card = 0
            for card in range (len(hand)) :
                if hand[checked_card] == hand[card] :
                    similar_card += 1
            if similar_card == 2 :
                one_pair = True
            elif similar_card == 2 and one_pair == True :
                two_pair = True
            elif similar_card == 3 :
                three_of_a_kind = True
            elif similar_card == 4 : 
                four_of_a_kind = True
            elif similar_card == 5 :
                five_of_a_kind = True
        if five_of_a_kind == True :
            hands[0] += [[hand,bid]]
        elif four_of_a_kind == True :
            hands[1] += [[hand,bid]]
        elif three_of_a_kind == True and two_pair == True :
            hands[2] += [[hand,bid]]
        elif three_of_a_kind == True :
            hands[3] += [[hand,bid]]
        elif two_pair == True :
            hands[4] += [[hand,bid]]
        elif four_of_a_kind == True :
            hands[5] += [[hand,bid]]
        else :
            hands[6] += [[hand,bid]]
        
print(hands)
strength = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]

# for type in range (len(hands)) :
#   while len(hands[type]) != 0 :
#     cards_verification = [hands[type]]
#     for line in range (len(cards_verification)) :
#       if cards_verification[line][0] == 