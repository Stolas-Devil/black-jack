 
import Card, games


class BJ_card(Card.Positionable_Card):
    """карты игры"""
    ACE_VALUE = 1 

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
            else:
                v = None
            return v        
class BJ_Deck(Card.Deck):
    """колода"""
    def populate(self):
        for suit in BJ_card.SUITS:
            for rank in BJ_card.RANKS:
                self.cards.append(BJ_card(rank, suit))


class BJ_Hand(Card.Hand):
    """"""
    def __init__(self, name):
        super().__init__()
        self.name = name 
    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
            return rep     
    @property
    def total(self):
        # если карта из Value = None
        # то все свойство None         
        for card in self.cards:
            if not card.value:
                return None
        # Сумируем оки каждый туз = 1
        # определяем наличие туза у игрока              
        t = 0 
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_card.ACE_VALUE:
                contains_ace = True
        # если сумма с тузом < 11
        # то туз = 11     
        if contains_ace and t <= 11:
            # прибавляем тоько 10 
            # потомучто 1 уже прибавили 
            t += 10
        return t    
    def is_busted(self):
        return self.total > 21    

class BJ_Player(BJ_Hand):
    """игрок"""
    def is_hitting(self):
        response = games.ack_yes_no("\n" + self.name +", будете брать еще карты?")
        return response == "y"
    def bust(self):
        print(self.name, "перебрал(а).")
        self.lose()
    
    def lose(self):
        print(self.name, "LOSE")

    def win(self):
        print(self.name, "WIN")

    def push(self):
        print(self.name, "push")

class BJ_Dealer(BJ_Hand):
    """дилер"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрал.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()         

class BJ_Game:
    """игра"""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        
        self.dealer = BJ_Dealer("Дилер")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp           
     
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()


    def play(self):
        if self.deck < 54:
            self.deck.populate()
            self.deck.shuffle()

        # раздача по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        # дилер показывет 2 карты
        for player in self.players:
            print(player)
        print(self.dealer)  
        # роздача дополнительных карт
        for player in self.players:
            self.__additional_cards(player)
        # 1 карта дилера розкрываеться 
        self.dealer.flip_first_card()                 
        if not self.still_playing:
            # все игроки перебрали
            # покажем только карты дилера
            print(self.dealer)
        else:
            # росдача дополнительнительных карт дилеру
            print(self.dealer)
            self.__additional_cards(self.dealer)  
            if self.dealer.is_busted():
                # выигрывают все кто остался в игре
                for player in self.still_playing:
                    player.win()
            else:
                # сравниваем суммы очков у дилера
                # и у игроков в игре 
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        # удаление всех карт
        for player in self.players:
            player.clear()
        self.dealer.clear()  

def main():
    print("\t\tДобро попожаловать в блек-джек!\n")
    names = []
    number = games.ask_number("Сколько игроков?(1-7):", low = 1, high = 7)
    for i in range(number):
        name = input("ВВедите имя игрока" + str(i + 1) + " :")
        names.append(name)
    print()
    game = BJ_Game(names)
    again=None 
    while again !="n": 
        game.play() 
        again=games.ask_yes_no("\nХотите сыграть ещё раз")     

main()
