from pyclbr import Class


class Card:

    def __init__(self, pNum, pColour):
        self.__Number = pNum #Integer
        self.__Colour = pColour #String

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

class Hand:

    #Cards[10] as Card
    #FirstCard as integer
    #NumberCards as integer

    def __init__(self, c1, c2, c3, c4, c5):
        self.__Cards = []
        self.__Cards.append(c1)
        self.__Cards.append(c2)
        self.__Cards.append(c3)
        self.__Cards.append(c4)
        self.__Cards.append(c5)
        self.__FirstCard = 0
        self.__NumberCards = 5

    def GetCard(self, index):
        return self.__Cards[index]

def CalculateValue(Hand):
    score = 0

    for i in range(5):
        a = Hand.GetCard(i)
        score = score + a.GetNumber()
        colour = a.GetColour()
        if colour == 'red':
            score += 5
        elif colour == 'blue':
            score += 10
        elif colour == 'yellow':
            score += 15

    return score



c1 = Card(1, 'red')
c2 = Card(2, 'red')
c3 = Card(3, 'red')
c4 = Card(4, 'red')
c5 = Card(5, 'red')
c6 = Card(1, 'blue')
c7 = Card(2, 'blue')
c8 = Card(3, 'blue')
c9 = Card(4, 'blue')
c10 = Card(5, 'blue')
c11 = Card(1, 'yellow')
c12 = Card(2, 'yellow')
c13 = Card(3, 'yellow')
c14 = Card(4, 'yellow')
c15 = Card(5, 'yellow')

Player1 = Hand(c1, c2, c3, c4, c11)
Player2 = Hand(c12, c13, c14, c15, c6)

score1 = CalculateValue(Player1)
score2 = CalculateValue(Player2)
if score1 > score2:
    print('Player 1 wins')
elif score2 == score1:
    print('Ths game is a draw')
else:
    print('Player 2 wins')
