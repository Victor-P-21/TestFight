#!/usr/bin/env python
'''Это просто слегка расширенная версия подбрасывания монетки, не обращайте внимания.'''
#---Imports---
import colorama
from colorama import Fore, Back, Style
from random import randrange
from time import sleep
from winsound import Beep

#---Global---

#---Func---
colorama.init()
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
        #print ('\t%s attacked' % self.name)
        Beep(self.strikeSound, 25)
        return (RandomNumber() * self.strikePower)
        
    def hit(self, hitpower):
        self.hp = self.hp - hitpower
        self.printHP()
        
    def __del__(self):
        print(self.name, 'left arena' if self.hp > 0 else 'body was removed from arena')

#---Main---
retry = 'Y'
distance = 5

while retry == 'Y':

    Heros = [["Barbarian", 1, 5+1], ["Skeleton", 1, 5+1]] #Список персонажей
    CC = int(input("Characters:\n1.Barbarian\n2.Skeleton\n3.Random\nChose your Hero:")) - 1 #(Chose_Character) Выбор персонажа
    print()
    if CC == 2:
        CC = RandomNumber(1, 3) - 1
    Hero1 = Character(Heros[CC][0], RandomNumber(Heros[CC][1], Heros[CC][2]))
    Hero2 = Character('Skeleton', RandomNumber(1, 5+1))
    print('\nFight begins!\n')

    print(Fore.RED + '\t%s attacked' % Hero2.name + Style.RESET_ALL)

    while True:

        Hero2.hit(Hero1.attack())
        print(Fore.GREEN + '\t%s attacked' % Hero1.name + Style.RESET_ALL)
        if Hero2.hp < 1: break
        Hero1.hit(Hero2.attack())
        print(Fore.RED + '\t%s attacked' % Hero2.name + Style.RESET_ALL)
        if Hero1.hp < 1: break


    if Hero1.hp > 0:
        print(Fore.GREEN + '\n\t%s Wins!\n' % Hero1.name + Style.RESET_ALL)
    else:
        print(Fore.RED + '\n\t%s Wins!\n' % Hero2.name + Style.RESET_ALL)

    del Hero1
    del Hero2

    retry = input('\nNew fight? (Y/N) ').upper()
    
#---
