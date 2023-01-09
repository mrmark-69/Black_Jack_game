import random
from colorama import init, Fore

init(autoreset=True)


class Card:
    #  Карта, у которой есть значения
    def __init__(self, rank, card_suit):
        self.card_suit = card_suit
        self.rank = rank
        self.card = {self.rank: self.card_suit}

    def info(self):
        return {f" {self.rank} of {self.card_suit}"}
    #   - масть
    #   - ранг/принадлежность 2, 3, 4, 5, 6, 7 и так далее


class Deck:
    #  Колода создаёт у себя объекты карт
    def __init__(self):
        self.cards = []
        card_rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        card_suit = ["diamonds", "heart", "clubs", "spades"]
        for card in card_rank:
            for suit in card_suit:
                self.cards.append(Card(card, suit).card)
    # метод для перемешивания карт в колоде.
    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def info(self):
        print(self.cards)


class Player:
    default_name = "Al Francesco"

    #  Игрок, у которого есть имя и какие-то карты на руках
    def __init__(self, name=default_name):
        self.result = None
        self.cards = []
        self.name = name
    # Вывод информации об игроке, какие карты и сколько очков.
    def info(self):
        self.result = 0
        for card in self.cards:
            for rank in card.keys():
                if str(rank) in '"Jack", "Queen", "King"':
                    self.result += 10
                elif str(rank) == "Ace":
                    self.result += 11
                else:
                    self.result += int(rank)
        for card in self.cards:
            for rank in card.keys():
                if rank == "Ace":
                    if self.result > 21:
                        self.result -= 10

        cards = ''
        for card in self.cards:
            for rank, suit in card.items():
                cards += f"{rank} of {suit}, "

        print(Fore.CYAN + f"{self.name}: {cards}, number of points: {self.result}")


def black_jack(deck, player_user, player_computer):
    while True:
        deck.shuffle()
        for _ in range(2):
            player_user.cards.append(deck.cards.pop(0))
            player_computer.cards.append(deck.cards.pop(0))
        player_user.info()
        question = input(Fore.GREEN + "\nAnother card? 1 - yes, 2 - no, 3 - Exit. ")
        if question == '3':
            print(Fore.GREEN + "\nThe game is over!")
            break
        while question == '1':
            player_user.cards.append(deck.cards.pop(0))
            player_user.info()
            question = input(Fore.GREEN + "\nAnother card? 1 - yes, 2 - no ")
        else:
            deck = Deck()
            player_user.info()
            player_computer.info()
            if player_computer.result < player_user.result <= 21:
                print(Fore.GREEN + f"\n{player_user.name} Winner!\n")
            elif player_user.result < player_computer.result <= 21 or player_user.result > 21:
                print(Fore.RED + f"\n{player_computer.name} Winner!\n")
            else:
                print(Fore.LIGHTYELLOW_EX + "\nDead heat.\n")

        player_user.cards = []
        player_computer.cards = []


casino = Deck()
player = Player("Al Francesco")
dealer = Player("Casino")

black_jack(casino, player, dealer)
