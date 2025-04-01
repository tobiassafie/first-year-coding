# Program: hw07_game.py
# Purpose: Simulates the game of War
# Author:  Tobias Safie - tks57@drexel.edu
# Date:    February 20, 2025

# Variable to accumulate cards during game
# Easier to make it separate from the function due to recursion
warPile = []

# Function to execute the game of War
def war(deck1, deck2):
    # Making the warPile variable globally accessible
    global warPile
    
    # Base cases for empty decks -- if one deck is empty, declare the opponent winner
    if not deck1: # Player 1's deck is empty
        print("Player 2 is victorious!")
        return
    elif not deck2: # Player 2's deck is empty
        print("Player 1 is victorious!")
        return
    
    # Print the current decks
    print("Player 1 Deck:", deck1)
    print("Player 2 Deck:", deck2)
    
    # Each player plays the pop card.
    # Utilizing the pop method to define the variable as the top card
    # while simultaneously removing it from the deck.
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    print(f"Battle: Player 1 played {card1}")
    print(f"Battle: Player 2 played {card2}")
    
    # Run thru the battle outcomes.
    # Normal battle outcome:
    if card1 > card2:
        print("Player 1 won this battle.")
        # Winner takes their own card first, then opponent's plus the War pile
        deck1.extend([card1, card2] + warPile)
        warPile = [] # Clear the War pile
    elif card2 > card1:
        print("Player 2 won this battle.")
        deck2.extend([card1, card2] + warPile)
        warPile = []
    else:
        # Tie -- initiate war
        print("The players tie on this battle.")
        print("War is declared.")
        
        # Add card1 + card2 to the War pile
        warPile.extend([card1, card2])
        
        # Before starting the war procedure, check if both players have >= 2 cards
        if len(deck1) < 2:
            print("Player 1 does not have enough cards for war. Player 2 wins the war.")
            deck2.extend([card1, card2])
            warPile = []
            print("Player 2 is victorious!")
            return
        elif len(deck2) < 2:
            print("Player 2 does not have enough cards for war. Player 1 wins the war.")
            deck1.extend([card1, card2])
            warPile = []
            print("Player 1 is victorious!")
            return
        
        # Actually commence the War sequence.
        # Each player places one card face down.
        card1Down = deck1.pop(0)
        card2Down = deck2.pop(0)
        print(f"War: Player 1 face down card: {card1Down}")
        print(f"War: Player 2 face down card: {card2Down}")
        warPile.extend([card1Down, card2Down])
        
        # Each player places one card face up:
        card1Up = deck1.pop(0)
        card2Up = deck2.pop(0)
        print(f"War: Player 1 face up card: {card1Up}")
        print(f"War: Player 2 face up card: {card2Up}")
        warPile.extend([card1Up, card2Up])
        
        # Compare the face-up cards
        if card1Up > card2Up:
            print("War: Player 1 won this war")
            deck1.extend(warPile)
        elif card2Up > card1Up:
            print("War: Player 2 won this war")
            deck2.extend(warPile)
            warPile = []
        else:
            # Another tie in the war -- recurse again
            print("War: Anothe tie. War is declared.")
            war(deck1, deck2)
            return
        
    # Print decks after the battle/war is resolved
    print("After Battle: Player 1 Deck contains", deck1)
    print("After Battle: Player 2 Deck contains", deck2)
        
    # Recurse
    war(deck1, deck2)

    
if __name__=="__main__":
    # Start the game
    print("Prepare for War (The Card Game).")
    
    # Read input for both players using list comprehensions.
    deck1 = [int(card) for card in input("Enter Player 1's deck (cards separated by spaces): ").split()]
    deck2 = [int(card) for card in input("Enter Player 2's deck (cards separated by spaces): ").split()]

    # Check that both decks have the same number of cards.
    if len(deck1) != len(deck2):
        print("Cannot play if decks have different numbers of cards.")
    else:
        war(deck1, deck2)