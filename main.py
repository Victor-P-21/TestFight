import time, random, pygame
from  weapon import Weapon
from hero import Hero
from config import weapon, races

global player           #Use in HeroInit func
global weapon_of_player #Use in WeaponInit func
global NPC              #Use in NPCInit func
global weapon_of_NPC    #Use in WeaponInit func

def Fight_print():
    print('Battle start in...\n3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('Fight!\n'.upper())
    time.sleep(1)

def Attack (attacking, victim):
    if attacking.type_of_weapon == 'melee':
        damage = attacking.damage_of_weapon + attacking.strength - victim.defend
    else:
        damage = attacking.damage_of_weapon + attacking.dexterity - victim.defend
    if damage < 0:
        damage = 1
    victim.hp -= damage
    print("The " + attacking.name + attacking.attack_phrase + victim.name + " and " + victim.name + " left " + str(victim.hp) + "HP")

def RaceInit(race, object_type = 'NPC'):
    if object_type == 'NPC':
        NPC.race_name = races[int(race) - 1][0]
        NPC.strength = races[int(race) - 1][1]['strength']
    else:
        player.race_name = races[int(race) - 1][0]
        player.strength = races[int(race) - 1][1]['strength']

def WeaponInit(weapon_set, object_type = 'NPC'):
    if object_type == 'NPC':
        global weapon_of_NPC
        weapon_of_NPC = Weapon(NPC,
                               weapon[int(weapon_set) - 1][0],
                               int(weapon[int(weapon_set) - 1][1]['damage']),
                               weapon[int(weapon_set) - 1][1]['attack_phrase'],
                               weapon[int(weapon_set) - 1][1]['type_of_weapon'])
    else:
        global weapon_of_player
        weapon_of_player = Weapon(player,
                                  weapon[int(weapon_set) - 1][0],
                                  int(weapon[int(weapon_set) - 1][1]['damage']),
                                  weapon[int(weapon_set) - 1][1]['attack_phrase'],
                                  weapon[int(weapon_set) - 1][1]['type_of_weapon'])

def HeroInit():
    global player
    player = Hero(input('Set name for your Hero: '))
    race_set = input('Take your race:\n' + '\n'.join(['[%s]'%(races.index(i) + 1) + i[0] for i in races]) + '\nNumber of race:')
    RaceInit(race_set, 'player')
    weapon_set = input('Take your weapon:\n' + '\n'.join(['[%s]'%(weapon.index(i) + 1) + i[0] for i in weapon]) + '\nNumber of weapon:')
    WeaponInit(weapon_set, 'player')
    print('')

def NPCInit():
    global NPC
    NPC = Hero('Steve')
    RaceInit(random.randrange(1, len(races) + 1))
    WeaponInit(random.randrange(1, len(weapon) + 1))
    print('')

main = 'y'

while main == 'y':

    print("Let's begin Mortal Combat")
    time.sleep(1)

    HeroInit()
    time.sleep(1)
    NPCInit()
    time.sleep(1)

    winer = ''

    Fight_print()

    while True:
        Attack(player, NPC)
        if NPC.hp <= 0:
            winer = player.name
            player.hp = 100
            print("The " + winer + " has won💫")
            del NPC
            NPCInit()
            Fight_print()
        Attack(NPC, player)
        if player.hp <= 0:
            winer = NPC.name
            print("The " + winer + " has won💀")
            break
        time.sleep(0.5)

    del player
    del NPC

    main = input('\nOne more time?(y/n): ')
