#!/usr/bin/env python
'''Это просто слегка расширенная версия подбрасывания монетки, не обращайте внимания.'''
#---Imports---
from random import randrange
from time import sleep
from winsound import Beep
#---Global---

#---Func---
def RandomNumber(R_min=1, R_max=10+1):
    '''Функция RandomNumber
    Выдаёт случайное целое число в заданном промежутке или от 1 до 10.'''
    return randrange(R_min, R_max)
    
#---Class---
class Character:
    hp = 100
    def __init__(self, ChName, power=1):
        self.name = ChName
        self.strikePower = power
        self.strikeSound = 250 * power + 1250
        print('Level %d %s entered arena!' % (self.strikePower, self.name))
        
    def printHP(self):
        print ('%s health points dropped to %d !' % (self.name, self.hp if self.hp > 0 else 0)) # второе условие это тренарный оператор
        sleep(0.5)
        
    def attack(self):
        print ('\t%s attacked' % self.name)
        Beep(self.strikeSound, 25)
        return (RandomNumber() * self.strikePower)
        
    def hit(self, hitpower):
        self.hp = self.hp - hitpower
        self.printHP()
        
    def __del__(self):
        print(self.name, 'left arena' if self.hp > 0 else 'body was removed from arena')

#---Main---
retry = 'Y'
while retry == 'Y':
    
    Hero1 = Character('Barbarian', RandomNumber(1, 5+1))
    Hero2 = Character('Skeleton', RandomNumber(1, 5+1))
    print('\nFight begins!\n')

    while True:
        Hero2.hit(Hero1.attack())
        if Hero2.hp < 1: break
        Hero1.hit(Hero2.attack())
        if Hero1.hp < 1: break

    if Hero1.hp > 0:
        print('\n\t%s Wins!\n' % Hero1.name)
    else:
        print('\n\t%s Wins!\n' % Hero2.name)

    del Hero1
    del Hero2

    retry = input('\nNew fight? (Y/N) ').upper()
    
#---
