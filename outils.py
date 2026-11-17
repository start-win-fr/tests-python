def est_pair(nombre):
    return nombre % 2 == 0
# fin de la fonction

def est_majeur(age):
    return age >= 18

def est_premier(nombre):
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