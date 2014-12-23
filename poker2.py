CS313
=====
import string, math, random

# Create the card and assign its rank and suit
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('S', 'D', 'H', 'C')


  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

# Convert to face value cards if needed
  def __str__ (self):
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit


  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)
   
# Create a standard deck of 52 cards in a list
class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append(card)

  def shuffle (self):
    random.shuffle (self.deck)

  def __len__ (self):
    return len (self.deck)

  # During the poker game, this draws one card from
  #   the top of the pile
  def deal (self):
    if len(self) == 0:
      return None
    else:
      return self.deck.pop(0)

# Execute the game and determines the winning hand
class Poker (object):
  def __init__ (self, numHands):
    self.deck = Deck()
    self.deck.shuffle ()
    self.hands = []   # List of each hand
    numCards_in_Hand = 5   # This needs to stay at 5 for
                           #   the program to work

    # Deals the hands from the deck and stores them in a list (hands)
    # The hands are lists (hand) consisting of Card objects
    for i in range (numHands):
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  # Run a poker game, then determine and output the winning hand
  def play (self):
      
    allHandResults = []   # 2-D matrix containing each hand, and their
                          #   score and hand type

    # Print out the hands and their cards
    # Record the type and overall score of each hand in allHandResults
    print()
    for i in range (len (self.hands) ):
      # Sort hand in order of decreasing rank
      sortedHand = sorted (self.hands[i], reverse = True)  
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)
      allHandResults.append(self.handResult(sortedHand))
      
    # Give the type of hand (Pair, Straight, etc.)
    print()
    for j in range (len(self.hands)):
        print("Hand " + str(j + 1) + ': ' + allHandResults[j][1])

    
    # Calculate and output the winning hand using the hand scores
    winner = "Hand 1"
    for k in range(1, len(self.hands)):
        if allHandResults[k][0] > allHandResults[k-1][0]:
            winner = "Hand " + str(k+1)

    print("\n" + winner + " wins. \n")
    
  # Returns the type and score of each hand in a list
  def handResult(self, hand):

      handType = ''
      
      if self.isRoyal(hand) > 0:
          score = self.isStraightFlush(hand)
          handType = "Royal Flush"
          
      elif self.isStraightFlush(hand) > 0:
          score = self.isStraightFlush(hand)
          handType = "Straight Flush"
          
      elif self.isFour(hand) > 0:
          score = self.isFour(hand)
          handType = "Four of a Kind"

      elif self.isFull(hand) > 0:
          score = self.isFull(hand)
          handType = "Full House"

      elif self.isFlush(hand) > 0:
          score = self.isFlush(hand)
          handType = "Flush"

      elif self.isStraight(hand) > 0:
          score = self.isStraight(hand)
          handType = "Straight"

      elif self.isThree(hand) > 0:
          score = self.isThree(hand)
          handType = "Three of a Kind"

      elif self.isTwo(hand) > 0:
          score = self.isTwo(hand)
          handType = "Two Pair"

      elif self.isOne(hand) > 0:
          score = self.isOne(hand)
          handType = "One Pair"

      else:
          score = self.isHigh(hand)
          handType = "High Card"

      result = [score, handType]
      return result
    

  # Functions isRoyal down to isHigh take each hand and determine
  #   whether the hand matches that type. If so, a numerical value
  #   called "score" is returned, which is used to compare different
  #   hands. The hand with the highest score is the winner.
  #   The score is calculated as:
  #     score = h * 13^5 + c1 * 13^4 + c2 * 13^3 + c3 * 13^2 + c4 * 13 + c5
  #     where h is determined by the hand type and the c's are card ranks
  
  def isRoyal (self, hand):
      isStraight = False
      isFlush = False
      score = 0

      # Check for a straight
      for i in range(4):
          if hand[i].rank == hand[i+1].rank + 1:
              isStraight = True
          else:
              isStraight = False
              break

      # Check for a flush           
      for j in range(4):
          if hand[j].suit == hand[j+1].suit:
              isFlush = True
          else:
              isFlush = False
              break

      # Hand must also contain an Ace
      if isFlush and isStraight and hand[0].rank == 14:  
          score += 9 * 13**5
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
        
      return score


  def isStraightFlush (self, hand):
      isStraight = False
      isFlush = False
      score = 0

      # Check for a straight
      for i in range(4):
          if hand[i].rank == hand[i+1].rank + 1:
              isStraight = True
          else:
              isStraight = False
              break

      # Check for a flush           
      for j in range(4):
          if hand[j].suit == hand[j+1].suit:
              isFlush = True
          else:
              isFlush = False
              break

      if isFlush and isStraight:
          score += 9 * 13**5
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
        
      return score


  def isFour (self, hand):
      isFour = False
      score = 0

      # Check to see if the rank of 4 cards are equal
      if hand[1].rank == hand[2].rank == hand[3].rank:
          if hand[4].rank == hand[3].rank:
              isFour = True
              notFour = hand[0].rank  # The card not in the four of a kind
              
          elif hand[0].rank == hand[1].rank:
              isFour = True
              notFour = hand[4].rank

      if isFour:
          score += 8 * 13**5
          if notFour == hand[0].rank:
              score += hand[1].rank * (13**4 + 13**3 + 13**2 + 13)
              score += hand[0].rank
          elif notFour == hand[4].rank:
              score += hand[0].rank * (13**4 + 13**3 + 13**2 + 13)
              score += hand[4].rank
    
      return score


  def isFull (self, hand):
      isFull = False
      score = 0

      # Check to see if there is 1 pair and 1 three of a kind
      if hand[0].rank == hand[1].rank:
          if hand[2].rank == hand[3].rank == hand[4].rank:
              isFull = True
              pairRank = hand[0].rank
              threeRank = hand[2].rank
          elif hand[1].rank == hand[2].rank and \
          hand[3].rank == hand[4].rank:
              isFull = True
              pairRank = hand[3].rank
              threeRank = hand[0].rank

      if isFull:
          score += (7 * 13**5) + threeRank * (13**4 + 13**3 + 13**2)
          score += pairRank * (13 + 1)

      return score


  def isFlush (self, hand):
      isFlush = False
      score = 0

      # Check if all cards have the same suit
      for i in range(4):
          if hand[i].suit == hand[i+1].suit:
              isFlush = True
          else:
              isFlush = False
              break

      if isFlush:
          score += 6 * 13**5
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
            
      return score


  def isStraight (self, hand):
      isStraight = False
      score = 0

      # Check if all cards are different by exactly one rank
      for i in range(4):
          if hand[i].rank == hand[i+1].rank + 1:
              isStraight = True
          else:
              isStraight = False
              break

      if isStraight:
          score += 5 * 13**5 
          for j in range(5):
              score += hand[j].rank * 13**(4 - j)
          
          
      return score


  def isThree (self, hand):
      isThree = False
      score = 0
      notThree = []

      # Check if three of the cards have the same rank
      for i in range(3):
          if hand[i].rank == hand[i+1].rank == hand[i+2].rank:
              threeRank = hand[i].rank
              isThree = True

      if isThree:
          for j in range(5):
              if hand[j].rank != threeRank:
                  notThree.append(hand[j].rank)  # Cards not in the
                                                 #   three of a kind
          score += (4 * 13**5) + threeRank * (13**4 + 13**3 + 13**2)
          score += (notThree[0] * 13) + notThree[1]

      return score


  def isTwo (self, hand):
      isTwoPair = False
      score = 0

      # Check the 3 cases of having two pairs. The one card not in a
      #   pair can be either the first, third, or fifth card in the
      #   sorted hand.
      if hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank:
          pair1 = hand[0].rank
          pair2 = hand[2].rank
          isTwoPair = True
          notTwoPair = hand[4].rank
      elif hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank:
          pair1 = hand[1].rank
          pair2 = hand[3].rank
          isTwoPair = True
          notTwoPair = hand[0].rank
      elif hand[0].rank == hand[1].rank and hand[3].rank == hand[4].rank:
          pair1 = hand[0].rank
          pair2 = hand[3].rank
          isTwoPair = True
          notTwoPair = hand[2].rank

      if isTwoPair:
          score += (3 * 13**5) + pair1 * (13**4 + 13**3)
          score += pair2 * (13**2 + 13) + notTwoPair
          
      return score


  def isOne (self, hand):
      isPair = False
      score = 0
      notPair = []   # list of cards that are not in the pair

      # Check to see if there is exactly one pair of matching ranks
      for i in range(4):
          if hand[i].rank == hand[i+1].rank:
              pairRank = hand[i].rank
              isPair = True

      if isPair:
          for j in range(5):
              if hand[j].rank != pairRank:
                  notPair.append(hand[j].rank)  # The cards not in the pair
          score += (2 * 13**5) + pairRank * (13**4 + 13**3)
          score += (notPair[0] * 13**2) + (notPair[1] * 13) + notPair[2]
      
      return score
      

  def isHigh (self, hand):

      # Default hand type if none of the above types are present.
      # High card calculates the best score by how highly ranked
      #   the cards are.
      score = 13**5 + (hand[0].rank * 13**4)
      score += (hand[1].rank * 13**3) + (hand[2].rank * 13**2)
      score += (hand[3].rank * 13) + hand[4].rank

      return score


def main ():
  # The user must choose between 2 and 6 hands to be dealt
  print()
  numHands = eval (input ('Enter the number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    numHands = eval( input ('Enter number of hands to play: ') )
  # Execute the game by dealing "numHands" random hands
  game = Poker (numHands)
  game.play()


main()
