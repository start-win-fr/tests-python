def est_pair(nombre):
    return nombre % 2 == 0
# fin de la fonction

def est_majeur(age):
    return age >= 18

def est_premier(nombre):
    if not nombre.is_integer():
        return False

    if nombre < 2:
        return False
    d = 2
    while d * d <= nombre:
        if nombre % d == 0:
            return False
        d += 1
    return True

def est_palindrome(mot):
    mot = mot.lower().replace(" ", "")
    return mot == mot[::-1] # Permet de retourner une chaine de caractère à l'envers

def moyenne(nombres):
    if len(nombres) == 0:
        raise ValueError("Impossible de calculer la moyenne d'une liste vide")

    return sum(nombres) / len(nombres)

def demander_entier(question):
    # T8 : redemande tant que la saisie n'est pas un entier
    while True:
        saisie = input(question)
        try:
            return int(saisie)
        except ValueError:
            print("Ce n'est pas un nombre entier, recommencez.")
