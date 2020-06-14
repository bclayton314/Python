

#BlackJack

#importing necessary functions
from random import randint #allows us to get a random number
#from IPython.display import clear_output

#create the blackjack class, which will hold all game methods and attributes
class Blackjack():
	def __init__(self):
		self.deck = []	#set to an empty list
		self.suits = ("Spades", "Hearts", "Diamonds", "Clubs")
		self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

#create a method that creates a deck of 52 cards, each card should be a tuple with a value and suit
	def makeDeck(self):
		for suit in self.suits:
			for value in self.values:
				self.deck.append((value, suit))	# ex: (7, "Hearts")

#method to pop a card from deck using a random index value
	def pullCard(self):
		return self.deck.pop (randint(0, len(self.deck) - 1))

#create a class for the dealer and player objects
class Player():
	def __init__(self, name):
		self.name = name
		self.hand = []

#take in a tuple and append it to the hand
	def addCard(self, card):
		self.hand.append(card)

#if not dealer's turn then only show one of his cards, otherwise show all
	def showHand(self, dealer_start = True):
		print("\n{}".format(self.name))
		print("==========")
		for i in range(len(self.hand)):
			if self.name == "Dealer" and i == 0 and dealer_start:
				print("- of -")
			else:
				card = self.hand[i]
				print("{} of {}".format(card[0], card[1]))

game = Blackjack()
game.makeDeck()
name = input("What is your name?")
player = Player(name)
dealer = Player("Dealer")

#add two cards to the dealer and player hand
for i in range(2):
	player.addCard(game.pullCard())
	dealer.addCard(game.pullCard())

#show both hands using method
player.showHand()
dealer.showHand()












