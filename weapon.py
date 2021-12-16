class Weapon:
    def __init__(self, owner, name = 'fists', damage = 5, attack_phrase = ' attack ', type_of_weapon = 'melee'):
        self.owner = owner
        self.last_owner = owner
        self.name = name
        self.damage = damage
        self.type_of_weapon = type_of_weapon
        self.owner.wearpon_name = self.name
        self.owner.damage_of_weapon = self.damage
        self.owner.attack_phrase = attack_phrase
        self.owner.type_of_weapon = self.type_of_weapon
        print('A ' + self.owner.race_name + ' named ' + self.owner.name + ' take the ' + self.name)

    def re_init(self, owner):
        self.owner = owner
        self.owner.wearpon_name = self.last_owner.wearpon_name
        self.owner.damage_of_weapon = self.last_owner.damage_of_weapon
        self.owner.attack_phrase = self.last_owner.attack_phrase
        self.owner.type_of_weapon = self.last_owner.type_of_weapon
        self.last_owner.re_init()
        print('A ' + self.owner.race_name + ' named ' + self.owner.name + ' take the ' + self.name)