from cards import deck

#This function determines the rank of the hand from a scale of 1-10 where 1 is high card and 10 is a straight flush
def hand_rank(hand):
    #insert ranking at the end of each if statement
    hand_values = []
    values_count = []
    hand_suits = []
    suits_count = []
    flush_cards = []



    for card in hand:
        hand_values.append(card.value)
        values_count.append(hand_values.count(card.value))
        hand_suits.append(card.suit)
        suits_count.append(hand_suits.count(card.suit))
    print("suits", hand_suits)
    print("values", hand_values)
    print("values sorted", list(set(hand_values)))
    hand_val = list(set(hand_values))



    for value in range(len(hand_val)-4):
        if hand_val[value] == hand_val[value+1]-1 ==hand_val[value+2]-2 ==hand_val[value+3]-3 ==hand_val[value+4]-4 and hand_suits.count(card.suit) ==5:
            #print("straight Flush")
            return 10




    if hand_values.count(card.value) == 4:
        quad_value = card.value
        #print("quads", quad_value)
        return 9

    if values_count.count(2) == 2 and values_count.count(3):
        #print(values_count)
        #print("full house")
        return 8

    if hand_suits.count(card.suit) ==5:
        #print("Flush")
        flush_cards.append(card.value)     
        return 7



    #print(range(len(hand_val)-4))
    for value in range(len(hand_val)-4):
        if hand_val[value] == hand_val[value+1]-1 ==hand_val[value+2]-2 ==hand_val[value+3]-3 ==hand_val[value+4]-4:
            #print("straight")
            return 6
    
    

    if hand_values.count(card.value) ==3:
        trip_value = card.value
        #print("trips", trip_value)
        return 5

    if hand_values.count(card.value) ==2:
        pair1_value = card.value
        #print("pair",pair1_value)
        return 3


    if values_count.count(2) ==2:
        #print("two_pair")
        return 4
    
    return 1


def Win_Chances(rank1,suit1,rank2,suit2,rank3,suit3,rank4,suit4):
    Deck_Counter1 = -1
    Deck_Counter2 = -1
    Deck_Counter3 = -1
    Deck_Counter4 = -1

    Our_cards = []
    Opp_cards = [] 

    for card in deck:
        Deck_Counter1 += 1
        Deck_Counter2 += 1
        Deck_Counter3 += 1
        Deck_Counter4 += 1
        
        if card.value == rank1 and card.suit == suit1:
            deck.pop(Deck_Counter1)
            Our_cards.append(card)
        if card.value == rank2 and card.suit == suit2:
            deck.pop(Deck_Counter2)
            Our_cards.append(card)
        if card.value == rank3 and card.suit == suit3:
            deck.pop(Deck_Counter3)
            Opp_cards.append(card)
        if card.value == rank4 and card.suit == suit4:
            deck.pop(Deck_Counter4)
            Opp_cards.append(card)
    
    deck.shuffle()
    #think about a way to figure out how to deal all possible 5 combination of cards without duplicates

    Possible_Combinations = []
    Possible_Outcomes_int = 0
    for card in deck:
        card1 = card
        #print(hand)
        for card in deck:
            if card != card1:
              card2 = card
              #Possible_Combinations.append(hand)
              #Possible_Outcomes_int +=1
              for card in deck:
                  if card != card1 and card2:
                      card3 = card
                      for card in deck:
                          if card != card1 and card2 and card3:
                              card4 = card
                              for card in deck:
                                 if card != card1 and card2 and card3 and card4:
                                     card5 = card
                                     board = []
                                     board.append(card1) 
                                     board.append(card2) 
                                     board.append(card3) 
                                     board.append(card4) 
                                     board.append(card5) 
                                     Possible_Combinations.append(board)
                                     Possible_Outcomes_int +=1
    Possible_Outcomes_int/= 2
    Possible_Outcomes = int(Possible_Outcomes_int)

    #determing the winning probability of each hand
    Our_wins = 0
    num_probs = 0
    
    for board in Possible_Combinations:
        Opp_hand = board + Opp_cards
        Our_hand = board + Our_cards

        Our_values = []
        for card in Our_hand:
            Our_values.append(card.value)
        Our_max = max(Our_values)
        Opp_values = []
        for card in Opp_hand:
            Opp_values.append(card.value)
        Opp_max = max(Opp_values)
        if Opp_max == Our_max:
            Our_values.pop(Our_max)
            Opp_values.pop(Opp_max)
            Our_max = max(Our_values)
            Opp_max = max(Opp_values)
            if Opp_max == Our_max:
                Our_values.pop(Our_max)
                Opp_values.pop(Opp_max)
                Our_max = max(Our_values)
                Opp_max = max(Opp_values)
                if Opp_max == Our_max:
                    Our_values.pop(Our_max)
                    Opp_values.pop(Opp_max)
                    Our_max = max(Our_values)
                    Opp_max = max(Opp_values)
                    if Opp_max == Our_max:
                        Our_values.pop(Our_max)
                        Opp_values.pop(Opp_max)
                        Our_max = max(Our_values)
                        Opp_max = max(Opp_values)

        Our_score = hand_rank(Our_hand)
        Opp_score = hand_rank(Opp_hand)
        #need something to determine what happens when the rank value is the same
        if Our_score > Opp_score:
            Our_wins += 1
        #elif Our_score == Opp_score:
            #if Our_score and Opp_score == 1:
            #    if Our_max > Opp_max:
            #        Our_wins+=1
            #    elif Opp_max == Our_max:
            #         Our_wins +=0.5

            #elif Our_score and Opp_score == 3:
            #    if our 
            #    if Our_max > Opp_max:
            #        Our_wins +=1
            #   elif Opp_max == Our_max:
            #        Our_wins +=0.5
        elif Our_score == Opp_score:
            Our_wins += 0.5

        num_probs += 1

    Our_chance = Our_wins/num_probs
    Opp_chance = abs((num_probs - Our_wins))/num_probs
    print("Our Chance:", Our_chance, "opp Chance:", Opp_chance)
    return Our_chance
    #now we need to develop a hand ranking system

Win_Chances(11,1,11,2,10,1,10,2)