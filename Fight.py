#!/usr/bin/env python
'''Это просто (не)слегка расширенная версия подбрасывания монетки, не обращайте внимания.
    ... Да какая уже нахрен монетка...
    Жосткий эмулятор секса с наждачкой без презерватива'''
# ---Imports---
from colorama import Fore, Back, Style, init
from random import randrange
from time import sleep
from winsound import Beep
# ---Global---
distance_between_Characters = 0                             #! чо? в глобе???
Hero = "*"                                                  #! чо бля? в глобе??? это???
# ---Func---
def RandomNumber(R_min=1, R_max=10+1):
    '''Функция RandomNumber
    Выдаёт случайное целое число в заданном промежутке или от 1 до 10, требует random.randrange'''
    return randrange(R_min, R_max+1)

def Text_Colour(colour='RED', text='No Data'):              #! допилил и заменил все нахер
    '''Функция Text_Colour
    Окрашивает текст в один из цветов на выбор, требует colorama.Fore, colorama.Style, colorama.init
    Цвета: BLACK, BLUE, CYAN, GREEN, MAGENTA, RED, WHitE, YELLOW,
        LIGHTBLACK_EX, LIGHTBLUE_EX, LIGHTCYAN_EX, LIGHTGREEN_EX,
        LIGHTMAGENTA_EX, LIGHTRED_EX, LIGHTWHitE_EX, LIGHTYELLOW_EX'''
    return getattr(Fore, colour) + text + Style.RESET_ALL

def Range_input(inputText, inpFrom='A', inpTo='z'):           #! я надеюсь мне не надо обяснять зачем она? и какого её писал я а не ты?
    '''Функция Range_input
    Позволяет вводить только числа из заданного диапазона, с пользовательским приглашением ввода
    Поддерживает целые числа, дробные чила, буквы
    Пример: Range_input('Input from 1 to 3 ', 1, 3)
    '''
    while True:
        if type(inpFrom) == type(1):
            try: data = int(input(inputText))
            except: continue
            if data >= inpFrom and data <= inpTo: return data
                
        elif type(inpFrom) == type(1.0):
            try: data = float(input(inputText))
            except: continue
            if data >= inpFrom and data <= inpTo: return data
                
        elif type(inpFrom) == type('A'):
            try: data = input(inputText)[0]
            except: continue
            if data >= inpFrom[0] and data <= inpTo[0]: return data

def Chanse_Сheck(chance):                                   #! либо описывай либо давай нормальные названия, я изменил название
    if randrange(1, 100+1) <= chance: return True           #! ладно блин, удобно для бинарных
    else: return False

def Move_Chooser(fromWho=1, toWho=1):       # в разработке
    print('1. Move towards enemy' if abs(fightArena.enemyPosition-fightArena.playerPosition) != 1 else '1. Move towards enemy (Enemy blocking way)')     # тупо проще редактировать ряд
    print('2. Move from enemy')
    print('3. Hit enemy')
    print('4. Try to sneak past enemy')
    choice = Range_input('Your choice: ', 1, 4)
    
    if choice == 1:     fightArena.Move(1,'Player')
    elif choice == 2:   fightArena.Move(-1,'Player')
    elif choice == 3:   Hero2.Hit(Hero1.Attack())
    elif choice == 4:   fightArena.Move(0,'Player') # пока не реализована функция сёба (тупо ставит на ячейку +2 или произвольную)

def NPC_Logic(fromWho=1, toWho=1):       # в разработке
    if abs(fightArena.enemyPosition-fightArena.playerPosition) != 1:
        print(Hero2.name, 'moved')
        fightArena.Move(1,'Enemy')
    else:
        Hero1.Hit(Hero2.Attack())

# ---Class---
class Arena:
    arena = []
    arenaFight = []
    playerPosition = 1
    enemyPosition = 1
    
    def __init__(self):
        # генератор функция начальной арены
        Arena = ['|']   #! внутрянняя, как хочу так и называю!
        for x in range(RandomNumber(3,10)): Arena.append('_')
        Arena.append('|')
        self.arena = Arena
        self.enemyPosition = len(Arena)-2 # переворот персов если надо
        print(''.join(self.arena)) #? Удалить нахрен?
    
    def Arena_Show(self):
        self.arenaFight = self.arena.copy()                                         # делаает копию начальной арены     #? надо ли хранить в классе? на вывод действий без шага?
        self.arenaFight[self.playerPosition] = Text_Colour(colour='GREEN', text='*')# расставляет оппонентов
        self.arenaFight[self.enemyPosition] = Text_Colour(colour='RED', text='*')
        print(''.join(self.arenaFight))
    
    def Move(self, step, who):  #? унифицировать больше?
        if who == 'Player': # хто ходит?
            character = self.playerPosition
            opponent = self.enemyPosition
        else:
            character = self.enemyPosition
            opponent = self.playerPosition
        
        if opponent - character < 0:    # Куды смотрим?
            if character - step > 0 and character - step < len(self.arena)-1: #нормалный ход
                if character - step <= opponent: #впечатался во врага
                    self.Arena_Show()
                    return print(Hero2.name, 'blocking way')
                if who == 'Player': self.playerPosition = character - step #вывод по участникам в случае успеха
                else: self.enemyPosition = character - step
                self.Arena_Show()
            else:
                self.Arena_Show()
                return print(Hero1.name, 'hit the wall, wall did not moved')
        else:
            if character + step > 0 and character + step < len(self.arena)-1: #нормалный ход
                if character + step >= opponent: #впечатался во врага
                    self.Arena_Show()
                    return print(Hero2.name, 'blocking way')
                if who == 'Player': self.playerPosition = character + step #вывод по участникам в случае успеха
                else: self.enemyPosition = character + step
                self.Arena_Show()
            else:
                self.Arena_Show()
                return print(Hero1.name, 'hit the wall, wall did not moved')

class Character:
    hp = 100

    def __init__(self, сhName, colour, power=1, startPosition=1, HeroType="Bot"):
        self.name = сhName
        self.strikePower = power
        self.colour = colour
        self.strikeSound = 250 * power + 1250
        self.position = startPosition   # ф топку
        self.HeroType = HeroType        # ф топку
        self.distanceToEnemy = 2        # ф ад накуй
        print('Level %d %s entered arena!' % (self.strikePower, Text_Colour(self.colour, self.name)))

    def PrintHP(self):
        print('%s health points dropped to %s !' % (Text_Colour(self.colour, self.name), self.hp if self.hp > 0 else Text_Colour('YELLOW', '0')))
        sleep(0.5)

    def Attack(self):
        print(Text_Colour(self.colour, '\n\t%s Attacked' % self.name))
        Beep(self.strikeSound, 25)
        return (RandomNumber() * self.strikePower)

    def Hit(self, Hitpower):
        self.hp = self.hp - Hitpower
        self.PrintHP()

    def actiont(self):              #! больше чтоб я такой хуйни не видел! чукча писатель блин
        #           --- Управление персонажем ---   #! и класс после себя почисть
        if self.HeroType == "Player":
            if self.distanceToEnemy > 1 and (self.position > 1 and self.position < len(arena) - 2):
                Choose_action = int(input("\nActions:\n1. Move to the right\n2. Move to the left\n3. Stand still\nChoose action:"))
                if Choose_action == 1:
                    arena[self.position] = "_"
                    self.position += 1
                    arena[self.position] = Text_Colour('GREEN', Hero)
                elif Choose_action == 2:
                    arena[self.position] = "_"
                    self.position -= 1
                    arena[self.position] = Text_Colour('GREEN', Hero)
                elif Choose_action == 3:
                    print(Text_Colour('GREEN', "\nYou wait patiently\n"))
                self.distanceToEnemy = abs(Hero2.position - self.position)
            elif self.distanceToEnemy > 1 and self.position == len(arena) - 2:
                Choose_action = int(input("\nActions:\n1. Move to the left\n2. Stand still\nChoose action:\n"))
                if Choose_action == 1:
                    arena[self.position] = "_"
                    self.position -= 1
                    arena[self.position] = Text_Colour('GREEN', Hero)
                elif Choose_action == 2:
                    print(Text_Colour('GREEN', "\nYou wait patiently\n"))
                self.distanceToEnemy = abs(Hero2.position - self.position)
            elif self.distanceToEnemy > 1 and self.position == 1:
                Choose_action = int(input("\nActions:\n1. Move to the right\n2. Stand still\nChoose action:"))
                if Choose_action == 1:
                    arena[self.position] = "_"
                    self.position += 1
                    arena[self.position] = Text_Colour('GREEN', Hero)
                elif Choose_action == 2:
                    print(Text_Colour('GREEN', "\nYou wait patiently\n"))
                self.distanceToEnemy = abs(Hero2.position - self.position)
            elif self.distanceToEnemy == 1 and self.position < Hero2.position and self.position > 1:
                Choose_action = int(input("\nActions:\n1. Move to the left\n2. Hit " + Hero2.name + " \n3. Push past the " + Hero2.name + " (40%)\nChoose action:"))
                if Choose_action == 1:
                    arena[self.position] = "_"
                    self.position -= 1
                    self.distanceToEnemy = abs(Hero2.position - self.position)
                    arena[self.position] = Text_Colour('GREEN', Hero)
                if Choose_action == 2:
                    Hero2.Hit(self.Attack())
                if Choose_action == 3:
                    sucsess = Chanse_Сheck(40)
                    if sucsess == True:
                        arena[self.position] = "_"
                        self.position += 2
                        arena[self.position] = Text_Colour('GREEN', Hero)
            elif self.distanceToEnemy == 1 and self.position > Hero2.position and self.position > 1:
                Choose_action = int(input("\nActions:\n1. Move to the right\n2. Hit " + Hero2.name + " \n3. Push past the " + Hero2.name + " (40%)\nChoose action:"))
                if Choose_action == 1:
                    arena[self.position] = "_"
                    self.position += 1
                    self.distanceToEnemy = abs(Hero2.position - self.position)
                    arena[self.position] = Text_Colour('GREEN', Hero)
                if Choose_action == 2:
                    Hero2.Hit(self.Attack())
                if Choose_action == 3:
                    sucsess = Chanse_Сheck(40)
                    if sucsess == True:
                        arena[self.position] = "_"
                        self.position -= 2
                        arena[self.position] = Text_Colour('GREEN', Hero)
            elif (self.distanceToEnemy == 1 and self.position < Hero2.position and self.position == 1) or (self.distanceToEnemy == 1 and self.position > Hero2.position and self.position == len(
                    arena) - 2):
                Choose_action = int(input("\nActions:\n1. Hit " + Hero2.name + " \n2. Push past the " + Hero2.name + " (40%)\nChoose action:"))
                if Choose_action == 1:
                    Hero2.Hit(self.Attack())
                if Choose_action == 2:
                    sucsess = Chanse_Сheck(40)
                    if sucsess == True:
                        arena[self.position] = "_"
                        self.position += 2
                        arena[self.position] = Text_Colour('GREEN', Hero)
            self.distanceToEnemy = abs(Hero2.position - self.position)
            Hero2.distanceToEnemy = abs(self.position - Hero2.position)



#           --- Логика бота(Hero2) ---
        if self.HeroType == "Bot":
            if self.distanceToEnemy > 1 and (self.position > 1 and self.position < len(arena) - 2):
                if Hero1.position < self.position:
                    arena[self.position] = "_"
                    self.position -= 1
                    self.distanceToEnemy = abs(self.position - Hero1.position)
                    arena[self.position] = Text_Colour('RED', Hero)
                else:
                    arena[self.position] = "_"
                    self.position += 1
                    self.distanceToEnemy = abs(Hero1.position - self.position)
                    arena[self.position] = Text_Colour('RED', Hero)
            elif self.distanceToEnemy > 1 and self.position == len(arena) - 2:
                arena[self.position] = "_"
                self.position -= 1
                self.distanceToEnemy = abs(Hero1.position - self.position)
                arena[self.position] = Text_Colour('RED', Hero)
            elif self.distanceToEnemy > 1 and self.position == 1:
                arena[self.position] = "_"
                self.position += 1
                self.distanceToEnemy = abs(Hero1.position - self.position)
                arena[self.position] = Text_Colour('RED', Hero)
            elif self.distanceToEnemy == 1:
                Hero1.Hit(self.Attack())
            self.distanceToEnemy = abs(self.position - Hero1.position)
            Hero1.distanceToEnemy = abs(self.position - Hero1.position)

    def __del__(self):
        print(self.name, 'left arena' if self.hp > 0 else Text_Colour('LIGHTBLACK_EX', 'body was removed from arena'))

# ---Main---
init()
retry = 'Y'

while retry == 'Y':
    fightArena=Arena()

    Heroes = [["Barbarian", 1, 5], ["Skeleton", 1, 5]]  # Список персонажей
    ChooseChar = int(input(
        "Characters:\n 1.Barbarian\n 2.Skeleton\n 3.Random\nChose your Hero: ")) - 1  # (Choose_Character) Выбор персонажа  #! катит!
    print()
    
    if ChooseChar == 2:
        ChoseChar = RandomNumber(1, 3) - 1
    Hero1 = Character(Heroes[ChooseChar][0], 'GREEN', RandomNumber(Heroes[ChooseChar][1], Heroes[ChooseChar][2]), 1, "Player")  # я про то каким образом функция принимающая и выдающая инты выберает перса
    Hero2 = Character('Skeleton', 'RED', RandomNumber(1, 5))
    # Hero1.distanceToEnemy = abs(Hero2.position - Hero1.position)      #! сам понял что с этим делать?
    # Hero2.distanceToEnemy = abs(Hero1.position - Hero2.position)
    # arena[Hero1.position] = Text_Colour('GREEN', Hero)
    # arena[Hero2.position] = Text_Colour('RED', Hero)
    print('\nFight begins!\n')
    fightArena.Arena_Show()

    # print(*arena)     #! а теперь попробуй обяснить что такое звёздочка перед переменной и почему так делать здесь нельзя

    while True:
        
        Move_Chooser()
        if Hero2.hp < 1: break
        NPC_Logic()
        if Hero1.hp < 1: break

    if Hero1.hp > 0: print(Text_Colour('GREEN', '\n\t%s Wins!\n' % Hero1.name))
    else: print(Text_Colour('RED', '\n\t%s Wins!\n' % Hero2.name))

    del Hero1
    del Hero2
    del fightArena

    retry = input('\nNew fight? (Y/N) ').upper()

# ---
