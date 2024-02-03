import random


cards = [
    {'proposition': 'P AND Q', 'difficulty': 1},
    {'proposition': 'P OR Q', 'difficulty': 2},
    {'proposition': 'NOT P', 'difficulty': 3},
    {'proposition': 'Modus Ponens', 'difficulty': 4},
    {'proposition': 'Conjuction', 'difficulty': 5},
    
]

def play():
    points = 0
    random.shuffle(cards)
    for card in cards:
        print(f"The challenge is to guess the answer of proposition: {card['proposition']}\n")
        user = input("Enter the answer by True or False:\t").lower()
        
        if evaluate_answer(card['proposition'], user):
            points += card['difficulty']
            print(f'correct you earned {card["difficulty"]}')
        else:
            print('Incorrect, the correct was: ', evaluate_truth_answer(card['proposition']))
    print(f'\n Game over, total points: {points }')
    
def evaluate_answer(proposition, user):
    truth_value = evaluate_truth_answer(proposition)
    return user == truth_value.lower()

def evaluate_truth_answer(proposition):
    if 'AND' in proposition:
        return str(True and True)
    elif 'OR' in proposition:
        return str(True or True)
    if 'NOT' in proposition:
        return str(not True)
    if 'Modus Ponens' in proposition:
        return str(True)
    if 'Conjunction' in proposition:
        return str(True and True)
    else:
        return 'unknown'
    
play()