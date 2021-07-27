
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Hearts', 'Spades', 'Diamonds', 'Clubs'] # Herz, Pik, Karo, Kreuz


@dataclass(order=True)
class Card:
    sort_index: int = field(init=False, repr=False)
    value: int
    rank: str
    suit: str
    trump: bool

    def __post_init__(self):
        self.sort_index = self.value
        if self.trump:
            self.sort_index += len(RANKS)

    def __str__(self):
        return f'{self.suit}-{self.rank}'

    def __repr__(self):
        return f'{self.suit}-{self.rank}'

    def val(self):
        if RANKS.index(self.rank) <= 7:
            # return int(self.rank)
            return 0
        elif self.rank == "10":
            return 10
        elif RANKS.index(self.rank) <= 11:
            return RANKS.index(self.rank)-7
        else:
            return 11
        
        
@dataclass
class Deck:
    cards: list[Card]

    def shuffle(self):
        random.shuffle(self.cards)

    def get(self):
        return self.cards.pop(0)

    def size(self):
        return len(self.cards)
    
    
def make_french_deck(trump="Hearts"):
    return Deck([Card(i, r, s, (s==trump)) for s in SUITS for i, r in enumerate(RANKS)])