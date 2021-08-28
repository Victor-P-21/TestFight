#!/usr/bin/env python
'''Это просто слегка расширенная версия подбрасывания монетки, не обращайте внимания.'''
#---Imports---
from colorama import Fore, Back, Style, init
from random import randrange
from time import sleep
from winsound import Beep

#---Global---
distance_between_Characters = 0
arena = []
Hero = "*"

#---Func---
def RandomNumber(R_min=1, R_max=10+1):
    '''Функция RandomNumber
    Выдаёт случайное целое число в заданном промежутке или от 1 до 10.'''
    return randrange(R_min, R_max)

    #---Ф-ции смены цвета текста ---
def Out_RED(text):
    return Fore.RED + text + Style.RESET_ALL
    
def Out_GREEN(text):
    return Fore.GREEN + text + Style.RESET_ALL
    
def Out_ColourSet(colour, text):
    return getattr(Fore,colour) + text + Style.RESET_ALL

def areneinit(lenghtOfArena):
    arena = ['|']
    for i in range(lenghtOfArena):
        arena += '_'
    arena += '|'
    return arena


#---Class---
class Character:
    hp = 100
    def __init__(self, ChName, colour, power=1, position = 5, HeroType = "Bot" ):
        self.name = ChName
        self.strikePower = power
        self.colour = colour
        self.strikeSound = 250 * power + 1250
        self.position = position
        self.HeroType = HeroType
        print('Level %d %s entered arena!' % (self.strikePower, Out_ColourSet(self.colour, self.name)))
        
    def printHP(self):
        print ('%s health points dropped to %s !' % (Out_ColourSet(self.colour, self.name), self.hp if self.hp > 0 else Out_ColourSet('YELLOW', '0')))
        sleep(0.5)
        
    def attack(self):
        print(Out_ColourSet(self.colour, '\n\t%s attacked' % self.name))
        
        Beep(self.strikeSound, 25)
        return (RandomNumber() * self.strikePower)
        
    def hit(self, hitpower):
        self.hp = self.hp - hitpower
        self.printHP()

    def __del__(self):
        print(self.name, 'left arena' if self.hp > 0 else Out_ColourSet('LIGHTBLACK_EX', 'body was removed from arena'))

#---Main---
init()
retry = 'Y'

while retry == 'Y':

    arena = areneinit(int(input("Print arena lenght:")))
    print(*arena)
    Heroes = [["Barbarian", 1, 5+1], ["Skeleton", 1, 5+1]] #Список персонажей
    ChooseChar = int(input("Characters:\n 1.Barbarian\n 2.Skeleton\n 3.Random\nChose your Hero: ")) - 1 #(Choose_Character) Выбор персонажа
    print()
    if ChooseChar == 2:
        ChoseChar = RandomNumber(1, 3) - 1
    Hero1 = Character(Heroes[ChooseChar][0], 'GREEN', RandomNumber(Heroes[ChooseChar][1], Heroes[ChooseChar][2]), 1, "Player")   #Это герой которого выбирает игрок, все данные берутся из списка Heros, по данному персонажу
    Hero2 = Character('Skeleton', 'RED', RandomNumber(1, 5+1), len(arena)-2)
    distance_between_Characters = abs(Hero1.position - Hero2.position)
    arena[Hero1.position] = Out_GREEN(Hero)
    arena[Hero2.position] = Out_RED(Hero)
    print('\nFight begins!\n')

    print(*arena)

    while True:
        if distance_between_Characters > 1 and (Hero1.position > 1 and Hero1.position < len(arena)-2 ):
            Choose_action = int(input("\nActions:\n1. Move to the right\n2. Move to the left\n3. Stand still\nChoose action:"))
            if Choose_action == 1:
                arena[Hero1.position] = "_"
                Hero1.position += 1
                distance_between_Characters = abs(Hero1.position - Hero2.position)
                arena[Hero1.position] = Out_GREEN(Hero)
            elif Choose_action == 2:
                arena[Hero1.position] = "_"
                Hero1.position -= 1
                distance_between_Characters = abs(Hero1.position - Hero2.position)
                arena[Hero1.position] = Out_GREEN(Hero)
            elif Choose_action == 3:
                print(Out_GREEN("\nYou wait patiently\n"))
        elif distance_between_Characters > 1 and Hero1.position == len(arena)-2:
            Choose_action = int(input("\nActions:\n1. Move to the left\n2. Stand still\nChoose action:\n"))
            if Choose_action == 1:
                arena[Hero1.position] = "_"
                Hero1.position -= 1
                distance_between_Characters = abs(Hero1.position - Hero2.position)
                arena[Hero1.position] = Out_GREEN(Hero)
            elif Choose_action == 2:
                print(Out_GREEN("\nYou wait patiently\n"))
        elif distance_between_Characters > 1 and Hero1.position == 1:
            Choose_action = int(input("\nActions:\n1. Move to the right\n2. Stand still\nChoose action:"))
            if Choose_action == 1:
                arena[Hero1.position] = "_"
                Hero1.position += 1
                distance_between_Characters = abs(Hero1.position - Hero2.position)
                arena[Hero1.position] = Out_GREEN(Hero)
            elif Choose_action == 2:
                print(Out_GREEN("\nYou wait patiently\n"))
        elif distance_between_Characters == 1 and Hero1.position < Hero2.position and Hero1.position > 1:
            Choose_action = int(input("\nActions:\n1. Move to the left\n2. Hit " + Hero2.name + " \nChoose action:"))
            if Choose_action == 1:
                arena[Hero1.position] = "_"
                Hero1.position -= 1
                distance_between_Characters = abs(Hero1.position - Hero2.position)
                arena[Hero1.position] = Out_GREEN(Hero)
            if Choose_action == 2:
                Hero2.hit(Hero1.attack())
                if Hero2.hp < 1: break
        elif distance_between_Characters == 1 and Hero1.position < Hero2.position and Hero1.position == 1:
            Choose_action = int(input("\nActions:\n1. Hit " + Hero2.name + " \nChoose action:"))
            if Choose_action == 1:
                Hero2.hit(Hero1.attack())
                if Hero2.hp < 1: break

        if distance_between_Characters > 1 and (Hero2.position > 1 and Hero2.position < len(arena)-2):
            if Hero1.position < Hero2.position:
                arena[Hero2.position] = "_"
                Hero2.position -= 1
                distance_between_Characters = abs(Hero2.position - Hero1.position)
                arena[Hero2.position] = Out_RED(Hero)
            else:
                arena[Hero2.position] = "_"
                Hero2.position += 1
                distance_between_Characters = abs(Hero1.position - Hero2.position)
                arena[Hero2.position] = Out_RED(Hero)
        elif distance_between_Characters > 1 and Hero2.position == len(arena)-2:
            arena[Hero2.position] = "_"
            Hero2.position -= 1
            distance_between_Characters = abs(Hero1.position - Hero2.position)
            arena[Hero2.position] = Out_RED(Hero)
        elif distance_between_Characters > 1 and Hero2.position == 1:
            arena[Hero2.position] = "_"
            Hero2.position += 1
            distance_between_Characters = abs(Hero1.position - Hero2.position)
            arena[Hero2.position] = Out_RED(Hero)
        elif distance_between_Characters == 1:
            Hero1.hit(Hero2.attack())
            if Hero1.hp < 1: break
        print(*arena)

    if Hero1.hp > 0:
        print(Out_GREEN('\n\t%s Wins!\n' % Hero1.name))
    else:
        print(Out_RED('\n\t%s Wins!\n' % Hero2.name))

    del Hero1
    del Hero2

    retry = input('\nNew fight? (Y/N) ').upper()
    
#----