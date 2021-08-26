#!/usr/bin/env python
'''Это просто слегка расширенная версия подбрасывания монетки, не обращайте внимания.'''
#---Imports---
import colorama #Нужен для colorama.init(), иначе ругается, что coloram-ы нет в импортах
from colorama import Fore, Back, Style #Без этой строчки выдаёт ошибку, мол Fore не задан
from random import randrange
from time import sleep
from winsound import Beep

#---Global---
colorama.init() #Без этой строчки выводит текст стандартного форматирования("\033 [031", или как-то так) -
                # - и при этом не меняет цвет текста, собственно почему встроенным методом не получилось воспользоваться
#---Func---
colorama.init()     #! ээ? выкинь ка нах в майн (лучше) или глобал это как бы всего то инициализатор раскраски а не твоя функция
def RandomNumber(R_min=1, R_max=10+1):
    '''Функция RandomNumber
    Выдаёт случайное целое число в заданном промежутке или от 1 до 10.'''
    return randrange(R_min, R_max)

#------------- Ф-ции смены цвета текста -------------

def Out_RED(text):
    text = Fore.RED + text + Style.RESET_ALL
    return text

def Out_GREEN(text):
    text = Fore.GREEN + text + Style.RESET_ALL
    return text

#----------------------------------------------------

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
        
    def attack(self, color="Red"): #Тут print пофиксил как придумал, пока что-то по-другому сделать фантазии не хватило
        Out = Out_RED('\t%s attacked' % self.name)
        if color == "GREEN":
            Out = Out_GREEN('\t%s attacked' % self.name)
        print(Out)
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
    ChoseChar = int(input("Characters:\n1.Barbarian\n2.Skeleton\n3.Random\nChose your Hero:")) - 1 #(Chose_Character) Выбор персонажа
    print()
    if ChoseChar == 2:
        ChoseChar = RandomNumber(1, 3) - 1
    Hero1 = Character(Heros[ChoseChar][0], RandomNumber(Heros[ChoseChar][1], Heros[ChoseChar][2]))
    Hero2 = Character('Skeleton', RandomNumber(1, 5+1))
    print('\nFight begins!\n')

    while True:
        Hero2.hit(Hero1.attack("GREEN"))
        if Hero2.hp < 1: break
        Hero1.hit(Hero2.attack())
        if Hero1.hp < 1: break

    if Hero1.hp > 0:
        print(Out_GREEN('\n\t%s Wins!\n' % Hero1.name))
    else:
        print(Out_RED('\n\t%s Wins!\n' % Hero2.name))

    del Hero1
    del Hero2

    retry = input('\nNew fight? (Y/N) ').upper()
    
#----
