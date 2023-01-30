import random

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
        self.is_rare = rare
        self.is_clean = clean
        self.heads = True

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.value = (self.original_value * 1.25) if self.is_rare else self.original_value
        self.color = (self.clean_color) if self.is_clean else self.rusty_color

    def __str__(self):
        return '£{} Coin'.format(int(self.original_value)) if self.original_value >= 1.00 else '{}p Coin'.format(int(self.original_value * 100))

    def rust(self):
        self.color = self.rusty_color
    
    def clean(self):
        self.color = self.clean_color
    
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    
    def __del__(self):
        print('Coin spent!')


class One_Pence(Coin):
    def __init__(self):
        data = {
            'original_value': 0.01,
            'clean_color': 'bronze',
            'rusty_color': 'brownish',
            'num_edges': 1,
            'diameter': 20.3,
            'thickness': 1.52,
            'mass': 3.56
        }
        super().__init__(**data)

class Two_Pence(Coin):
    def __init__(self):
        data = {
            'original_value': 0.02,
            'clean_color': 'bronze',
            'rusty_color': 'brownish',
            'num_edges': 1,
            'diameter': 25.9,
            'thickness': 1.85,
            'mass': 7.12
        }
        super().__init__(**data)

class Five_Pence(Coin):
    def __init__(self):
        data = {
            'original_value': 0.05,
            'clean_color': 'silver',
            'rusty_color': None,
            'num_edges': 1,
            'diameter': 18.0,
            'thickness': 1.77,
            'mass': 3.25
        }
        super().__init__(**data)

    def rust(self):
        self.clean()

class Ten_Pence(Coin):
    def __init__(self):
        data = {
            'original_value': 0.10,
            'clean_color': 'silver',
            'rusty_color': None,
            'num_edges': 1,
            'diameter': 24.5,
            'thickness': 1.85,
            'mass': 6.50
        }
        super().__init__(**data)
    
    def rust(self):
        self.clean()

class Twenty_Pence(Coin):
    def __init__(self):
        data = {
            'original_value': 0.20,
            'clean_color': 'silver',
            'rusty_color': None,
            'num_edges': 7,
            'diameter': 21.4,
            'thickness': 1.7,
            'mass': 5.00
        }
        super().__init__(**data)
    
    def rust(self):
        self.clean()

class Fifty_Pence(Coin):
    def __init__(self):
        data = {
            'original_value': 0.50,
            'clean_color': 'silver',
            'rusty_color': None,
            'num_edges': 7,
            'diameter': 27.3,
            'thickness': 1.78,
            'mass': 8.00
        }
        super().__init__(**data)
    
    def rust(self):
        self.clean()

class One_Pound(Coin):
    def __init__(self):
        data = {
            'original_value': 1.00,
            'clean_color': 'gold',
            'rusty_color': 'greenish',
            'num_edges': 1,
            'diameter': 22.5,
            'thickness': 3.15,
            'mass': 9.5
        }
        super().__init__(**data)

class Two_Pound(Coin):
    def __init__(self):
        data = {
            'original_value': 2.00,
            'clean_color': 'gold & silver',
            'rusty_color': 'greenish',
            'num_edges': 1,
            'diameter': 28.4,
            'thickness': 2.50,
            'mass': 12.00
        }
        super().__init__(**data)

coins = [
    One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(), 
    Twenty_Pence(), Fifty_Pence(), One_Pound(), Two_Pound()]

for coin in coins:
    arguements = [
        coin, coin.color, coin.value, coin.diameter, coin.thickness, 
        coin.num_edges, coin.mass
        ]
    string = '{} - Color: {}, value: {}, diameter(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}'.format(*arguements)
    print(string)