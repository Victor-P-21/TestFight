class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.level = 1
        self.strength = 1
        self.dexterity = 1
        self.defend = 1
        #weapon
        self.wearpon_name = ''
        self.damage_of_weapon = 0
        self.type_of_weapon = ''
        self.attack_phrase = ''
        #Race
        self.race_name = ''

    def re_init(self):
        self.wearpon_name = ''
        self.damage_of_weapon = 0
        self.type_of_weapon = ''
        self.attack_phrase = ' look at '