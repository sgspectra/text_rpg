#!/usr/bin/python3

from random import *

# Function to print the directions of the game
def directions():
    print('-' * 60)
    print('Commands:')
    print('go [direction]')
    print('get [item]')
    print('quit')
    print('-' * 60)


def status():
    print('-' * 60)
    print('Health: ' + ('+ ' * player['health']))
    print('You are in the ' + currentRoom)
    print('Inventory: ' + str(inventory))
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('-' * 60)


def encounter():
    enemy = rooms[currentRoom]['mob']
    print('You have encountered a ' + str(enemy) + '!')
    enemyHealth = baddies[enemy]['health']
    enemyAttack = baddies[enemy]['attack']
    if random() < baddies[enemy]['rng']:
        player['health'] = player['health'] - enemyAttack
        print('You have been hit for ' + str(enemyAttack) + ' damage!')
    print('Enemy Health: ' + ('+ ' * enemyHealth))
    status()


rooms = {
    'Hall':{
        'south': 'Kitchen',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'mob':'Bat'
    }
}

baddies = {
    'Bat':{
        'health': 1,
        'attack': 1,
        'rng': .1
    }
}

player = {
    'health': 3
}

# Print directions
directions()
# Set beginning location
currentRoom = 'Hall'
# Set beginning inventory
inventory = []
# Print beginning status
status()

while 1:
    # Get the players move
    move = ''
    while move == '':
        move = input('>')
    move = move.lower().split()

    # If quit is typed break
    if move[0] == 'quit':
        print('Quitting...')
        break

    # If go is typed
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            status()
        else:
            print('You cannot move in that direction.')

    # If get is typed
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            del rooms[currentRoom]['item']
            status()
        else:
            print("Item does not exist.")

    # Check if there is a mob in current room
    # and resolve the encounter
    if 'mob' in rooms[currentRoom]:
        encounter()
