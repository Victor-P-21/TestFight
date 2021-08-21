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
    Выдаёт случайное целое число в заданном промежутке.'''
    return randrange(R_min, R_max)
    
#---Class---
class Character:
    hp = 100
    def __init__(self, ChName, power=1):
        self.name = ChName
        self.strikePower = power
        print('Level %d %s entered arena!' % (self.strikePower, self.name))
        
    def printHP(self):
        print ('%s health points dropped to %d !' % (self.name, self.hp if self.hp > 0 else 0)) # осторожно, 2 условие - тренарный оператор
        
    def attack(self):
        print ('\t%s attacked' % self.name)
        return (RandomNumber() * self.strikePower)
        
    def hit(self, hitpower):
        self.hp = self.hp - hitpower
        self.printHP()
        
    # def __del__(self):
        # print('класс ' + self.name + ' удалён')

#---Main---
Hero1 = Character('Barbarian', RandomNumber(1, 5+1))
Hero2 = Character('Skeleton', RandomNumber(1, 5+1))
print('\nFight begins!\n')

while True:
    Hero2.hit(Hero1.attack())
    Beep(1500, 25)
    if Hero2.hp < 1: break
    sleep(0.5)
    Hero1.hit(Hero2.attack())
    Beep(2000, 25)
    if Hero1.hp < 1: break
    sleep(0.5)

if Hero1.hp > 0:
    print('\n %s Wins!' % Hero1.name)
else:
    print('\n %s Wins!' % Hero2.name)

