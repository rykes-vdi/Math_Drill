# Ilyasse Brik / ilyassebrik1@outlook.com / 2024-06-05 / drill.py / v1
# Un exerciseur de résolution d'équations mathématiques simples


# Importer la bibliothèque "random" pour ajouter de l'aléatoire au script,
# importer la fonction "system" de la bibliothèque "os" pour pouvoir vider l'écran et
# importer la fonction "sleep" de la bibliothèque "time" pour pouvoir arrêter
# momentanément l'éxécution du script
import random
from os import system
from time import sleep


# Déclarer la variable op_valides
global op_valides
# Déterminer un "tuple" comportant les opérateurs valides
op_valides = ("+", "-", "*", "/")


def set_var():

    global op
    global si_op_valide
    global a
    global b
    global a_min
    global a_max
    global b_min
    global b_max

    si_op_valide = True

    while si_op_valide:
        # Inviter l'utilisateur à taper l'opérateur désiré
        op = input('''Selectionner l'opérateur:
addition -> +
soustraction -> -
multiplication -> *
division -> /
>>> ''')
        # Vérifier si l'opérateur choisi par l'utilisateur est valide
        if op in op_valides:
            break
        else:
            print("Opérateur inconnu!")


    system("cls")
    a_min = int(input('''Tapez chiffre minimum pour premeier terme:
>>> '''))
    system("cls")
    a_max = int(input('''Tapez chiffre maximum pour premeier terme:
>>> '''))

    system("cls")
    b_min = int(input('''Tapez chiffre minimum pour deuxième terme:
>>> '''))
    system("cls")
    b_max = int(input('''Tapez chiffre maximum pour deuxième terme:
>>> '''))
    


def shuffle():

    global a
    global b
    global c
    global a_min
    global a_max
    global b_min
    global b_max
    
    # Attribuer des valeurs aléatoires comprises entre a_min, a_max, b_min et b_max aux variables a et b
    a = random.randint(a_min, a_max)
    b = random.randint(b_min, b_max)

    # Déterminer la valeur de c tout dépendant de l'opération choisie par l'utilisateur
    if op == op_valides[0]:
        c = a + b
    elif op == op_valides[1]:
        c = a - b
    elif op == op_valides[2]:
        c = a * b
    elif op == op_valides[3]:
        c = a / b


def show():
    # Déterminer le symbole de l'opérateur
    symbole = "?"
    if op == op_valides[0]:
        symbole = "+"
    elif op == op_valides[1]:
        symbole = "-"
    elif op == op_valides[2]:
        symbole = "x"
    elif op == op_valides[3]:
        symbole = "/"
    # Afficher l'équation à l'utilisateur et en demander la réponse
    global c_inp
    system("cls")
    c_inp = int(input(f"{a} {symbole} {b} = "))


def verify():
    system("cls")
    if c_inp == c:
        print("OK!")
        sleep(1)
    elif c_inp != c:
        print("RETRY!")
        sleep(1)

# Boucle principale
set_var()
while True:
    shuffle()
    show()
    verify()
