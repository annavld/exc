"""
Es gibt zwei Spieler
Jeder bekommt 7 zufällige Karten (Objekte der Klasse Farbe und der Klasse Zahl)
Aktionskarten Karten: Klasse Skip, Draw 2, Draw 4, Wild (Wunschfarbe)
Jedes Objekt hat zwei Eigenschaften (Variablen, Farbe: String, Ziffer int)
Mögliche Farben: Rot, Grün, Blau, Gelb (Klassen, Eigenschaft Farbe als String )
Mögliche Zahlen: 1-9 (Klassen, Eigenschaft Zahl als Integer)

Eine zufällige Karte liegt vor
Zufälliger Spieler beginnt
Ihm werden seine Karten angezeigt

Hat er eine Karte die entweder die gleiche Farbe und/oder die gleiche Zahl und/oder eine Aktionskarte darf er die Karte legen,

Passen mehrere Karten zu der gewünschten Zahl und Farbe so kann er sich aussuchen welche Karte er legt
Ansonsten muss er die eine passende Karte legen

Ansonsten muss er eine Karte ziehen
Zieht er eine Karte die zu den Kriterien passt, so muss er sie legen
Ansonsten ist der nächste Spieler dran

Hat einer der Spieler keine Karten mehr, so ist das Spiel vorbei

Extentions:
- Jeder Spieler sieht nur seine Karten
- Man darf eine Draw auf Draw legen
- Es gibt ein Eingabefeld, wo der Spieler UNO hinschreiben muss, sobald er genau eine Karte hat
Macht er das nicht, so zählt sein potenzieller Gewinn nicht
- Das Spiel geht mit mehr als zwei Spielern

Klasse Players, die bekommen beim geboren werden direkt state und
"""

#Eingebaute Bibliothek mit Zufallszahlen
import random 
import re
import sys

#Jedes Mal, wenn das Programm ausgeführt wird, wird ein anderer Seed (Startpunkt) verwendet, der auf dem aktuellen Zeitpunkt basiert.

class Cards:
#Self muss bei jeder Instanzmethode übergeben werden, außer sie ist statisch. 
#Self repräsentiert das aktuelle Objekt der Klasse, wir machen es optional damit es von einer statischen Methode auch aufgerufen werden kann.
    @staticmethod
    def generateCard():
#Wir müssen die Variablen mit state. aufrufen, damit sie nicht lokal sind und von anderen Methoden benutzt werden können
        states = ['red','green','blue','yellow', 'wild', 'skip', 'draw_four']
        #Choice ist eine Funktion innerhalb des Moduls random
        state = random.choice(states)
        elements = list(range(1,9))+['reverse'] + ['draw_two']
        randomElement = random.choice(elements)
        
        if state == "wild" or state=="skip" or state=="draw_four":
            print(state)
            return state, None
        else:
            if ((state == 'wild' and randomElement =='draw_two') or (state == 'skip' and randomElement=='draw_two') or (state=='draw_four' and randomElement == 'draw_two')):
                return
            print(state, end=" ")
            print(randomElement)
            return state, randomElement

#Vererbung    
class Players(Cards):
    f = 0
    PlayersList = []
    shuffleCounter = 0
    previousPlayer = None
    def __init__(self):
    #Hier wollen wir, dass die Variable username auf einem Objekt aufrufbar ist
        self.username = input("Enter username:")
        print("Hello " + self.username + ",you have following cards")
        self.CardsOfThePlayer = []
        #ShuffleCounter ist hier, weil es sonst immer wieder auf 0 gesetzt wird und nur innerhalb einer Funktion definiert werden muss :(
        self.shuffleCounter = 0
        for i in range(7):
    #Die Methode wird auf dem neugeborenen Objekt aufgerufen
            self.ACardOfThePlayer = Players.generateCard()
            #Mit Append wird etwas einer Liste hinzugefügt
            self.CardsOfThePlayer.append(self.ACardOfThePlayer)
        Players.PlayersList.append(self)
        Players.f += 1

    #start
    #Das sind Klassenvariablen.Klassenvariablen werden innerhalb der Klasse, aber außerhalb von Methoden definiert. 
    #Sie werden oft verwendet, um Daten zu speichern, die für alle Instanzen der Klasse relevant sind. 
    firstCard = None
    stateFirstCard = None
    numberFirstCard = None 
    global currentIndex 

    @staticmethod
    def shuffle(self):
            #Es soll die vorhandenen Karten leeren
            #neue generieren
            #sie mit den alten ersetzen
            self.CardsOfThePlayer.clear()
            self.CardsOfThePlayer = [card for card in self.CardsOfThePlayer if card is not None]
            for i in range(7):
                shuffledCards = Players.generateCard()
                NewCardsOfThePlayer = self.CardsOfThePlayer.append(shuffledCards)

    @staticmethod
    def generateFirstCard():
        while True:
            print("The first card is...")
            Players.firstCard = Players.generateCard()
            Players.stateFirstCard, Players.numberFirstCard = Players.firstCard    
            if ("wild" not in Players.firstCard and "skip" not in Players.firstCard):
                break
            else:
                print ("The first card can't be wild or skip. Generating new card.")          
    
    @staticmethod
    def showTheRules():
        rules = """ 
        To choose one of your cards type in its color and number. 
        Type in 'Draw' to draw an additional card or 'Pass' to skip your turn.
        You can only skip your turn, if you drew once.
        You can look at your cards by typing 'My cards' or at the top card by typing 'Top card':
        Type in 'Rules' to show these rules.
        """ 
        print (rules)

    @staticmethod
    def checkUNO():
        if len(player1.CardsOfThePlayer) == 1:
            print ("UNO for " + player1.username)
        if len(player2.CardsOfThePlayer) == 1:
            print ("UNO for "+ player2.username)

    @staticmethod
    def checkWinner():
        #funktioniert nicht
        if player1.CardsOfThePlayer == []:
            print ("Game over, " + player1.username + " won!")
            sys.exit()
        elif player2.CardsOfThePlayer == []:   
            print ("Game over, " + player2.username + " won!")
            sys.exit()

   

    @staticmethod
    def getNextPlayer():
        nextIndex = (currentIndex + 1) % len(Players.PlayersList)
        return Players.PlayersList[nextIndex]        
        '''
         iteratorDraw = False
        for player in Players.PlayersList:
            if (player.username == self.username):
                iteratorDraw = True
        if iteratorDraw:

        '''
        
    @staticmethod
    def ForcedToDraw(quantity, getNextPlayer):
        nextPlayer = getNextPlayer()
        previousIndex = (currentIndex - 1) % len(Players.PlayersList) 
        previousPlayer = Players.PlayersList[previousIndex]
        playerString = str(previousPlayer.username)        
        print("Congratulations " + nextPlayer.username + "!" + playerString + "  made you draw ") #hier sagen wer wen gezwungen hat
        for j in range(quantity):
            drawnCard = Players.generateCard()
            nextPlayer.CardsOfThePlayer.append(drawnCard)

    stateNumberInput = 0
    def play(self):
        Players.f +=1
        a = 0
        player = 0
        global nextPlayer
        print(self.username + ", it's your turn. Here are your options:")
        print(self.CardsOfThePlayer)
        while True:
            #Ein Eingabefeld
            stateNumberInput = input("Please choose one of your cards, draw or pass: ")
            if (a == 1 and stateNumberInput == "Pass" or a == 1 and stateNumberInput == "Skip"):
                break
            elif (a < 1 and stateNumberInput == "Pass"):
                print ("You have to draw a card to be able to skip your turn ;') ")
            if stateNumberInput == "My cards":
                print (self.CardsOfThePlayer)
            elif stateNumberInput == "Top card":
                print (Players.firstCard)
            elif stateNumberInput == "Rules":
                Players.showTheRules()
            elif stateNumberInput == "Shuffle":
                if (self.shuffleCounter > 0):
                        print ("You can only shuffle once at the beginning of the game")
                        break
                for self in Players.PlayersList:
                    print (self.username + ", here are your new cards:")
                    Players.shuffle(self)
                    self.shuffleCounter += 1
                    #print (self.shuffleCounter)
                Players.generateFirstCard()
                break
            #das versteh ich nicht
            elif re.match(r"(blue|yellow|red|green) reverse", stateNumberInput):
                Players.foundMatch = re.match(r"(blue|yellow|red|green) reverse", stateNumberInput)
                if Players.foundMatch in self.CardsOfThePlayer:
                    Players.foundMatch = Players.foundMatch.group(1)
                    Players.CardsOfThePlayer.remove(Players.foundMatch)
                    #so bis hier
                self.checkWinner()
                self.checkUNO()
                break                    
            elif stateNumberInput == "wild":
                chosenColor = input("Please choose the color you want: ")
                if chosenColor == "red" or chosenColor == "green" or chosenColor == "blue" or chosenColor == "yellow": 
                    Players.stateFirstCard = chosenColor 
                    Players.numberFirstCard = None
                    Players.firstCard = chosenColor, None
                    self.CardsOfThePlayer.remove(('wild', None))
                    print ("Good choice!")
                    self.checkWinner()
                    self.checkUNO()
                    break
                else:
                    print("You can't choose this color. Please choose red, green, blue or yellow.")
                """
            elif stateNumberInput == "skip":
                #funktioniert nicht wie erwartet
                stateNumberInput = "skip", None
                self.CardsOfThePlayer.remove(stateNumberInput)
                self.checkWinner()
                self.checkUNO()
                self.play()
                break
            """
            elif re.match(r"(blue|yellow|red|green) draw_two", stateNumberInput):
                #Hier ersetzen mit der Anzahl der Spieler?? Wieso?
                self.ForcedToDraw(2, self.getNextPlayer)
                break
                '''
                 iteratorDrawTwo = 0
                for player in Players.PlayersList:
                    iteratorDrawTwo += 1
                    if (iteratorDrawTwo >= 1):
                        currentPlayer = player
                        break
                print("Congratulations " + currentPlayer.username + "! " + self.username + " made you draw ")
                for j in range(2):
                    drawnCard = Players.generateCard()
                    currentPlayer.CardsOfThePlayer.append(drawnCard)
                break
                
                '''
               
                #map wandelt alle Tupel in Strings um
                #join wandelt das Array selbst in einen String um, erwartet aber dass das Array nur Strings enthält
            elif stateNumberInput == "draw_four":
                self.ForcedToDraw(4, self.getNextPlayer)
                break
                '''
                iteratorDrawFour = 0
                for player2 in Players.PlayersList:
                    iteratorDrawFour += 2
                    if (iteratorDrawFour >= 1):
                        currentPlayer2 = player2
                        break
                print("Congratulations " + currentPlayer2.username + "! " + self.username + " made you draw ")
                for k in range(4):
                    drawnCard2 = Players.generateCard()
                    currentPlayer2.CardsOfThePlayer.append(drawnCard2)
                break
                '''
            if re.search(r'\d',stateNumberInput):
                stateInput, numberInput = stateNumberInput.split()
                    # Konvertieren des Zahleninputs in einen Integer
                numberInput = int(numberInput) 
                    # Erstellen des Paars aus dem Benutzerinput
                choice = (stateInput, numberInput)
                if choice in self.CardsOfThePlayer:
                    if stateInput==Players.stateFirstCard or numberInput==Players.numberFirstCard:
                        Players.firstCard = choice
                        Players.stateFirstCard = stateInput
                        Players.numberFirstCard = numberInput
                        self.CardsOfThePlayer.remove(choice)
                        print ("Good choice!")
                        self.checkWinner()
                        self.checkUNO()
                        break
                    else:
                        print ("You can't use this card here.")
                else:
                    print ("You don't own the card you chose.")
            if stateNumberInput == "Draw" and a < 1:
                a = 1
                self.draw()
            elif stateNumberInput=="Draw" and a >= 1:
                secondchoice = input ("You can only draw one card per turn. Type in 'Back' to use one of your cards or type in 'Pass' to skip your turn: ")
                if secondchoice == "Back":
                    pass
                elif secondchoice == "Pass":
                    break

    def draw(self):
        self.ACardOfThePlayer = Players.generateCard()
        self.CardsOfThePlayer.append(self.ACardOfThePlayer)
        print ("This is the card you drew. It was now added to your cards.")   

#ende
# Man zieht eine Karte
# Die Karte wird generiert
# Man hat die Wahl: Karte benutzen oder nicht
# Wenn man die Karte nicht benutzt, dann geht das spiel weiter
# Wenn man die Karte benutzt, dann soll sich die Wahl wie stateNumberInput verhalten

player1 = Players()
player2 = Players()
currentIndex = 0
#print (Players.PlayersList)
#player1.shuffle(player1)
Players.generateFirstCard()
while True:
    Players.PlayersList[currentIndex].play()
    currentIndex = (currentIndex + 1)%len(Players.PlayersList)
    Players.checkWinner()

# Bedingung definieren
# 1. Karte muss in den eigenen Karten enthalten sein
# 2. Karte muss entweder die gleiche farbe oder die gleiche zahl oder beides aufweisen
# Das Spiel geht solange bis einer der Spieler keine Karten mehr hat
# Wenn einer der Spieler nur noch eine Karte hat, dann soll UNO ausgegeben werden
# Draw Cards als Methode
# Wenn der User Draw 1 eingibt bekommt er noch eine Karte. 
# Benutzt er diese Karte so sollen z.99-102 ausgeführt werden
# Benutzt er sie nicht, dann gehts einfach weiter

# mehrere Probleme:
#   erste Karte fixen generierung: Die Karte darf nicht wild oder Skip sein
#   die Funktionen checkWinner und checkUno kommen mehrfach vor - wie kann man das ersetzen
#   wenn man sich bei wild verschrieben hat ist man stuck 
# test