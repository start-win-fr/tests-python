import pytest

from outils import est_pair, est_premier, est_majeur, est_palindrome

# Chaque fonction dont le nom commence par test_ est un test que pytest lance tout seul.
# Dedans : des assert. Si l'assert est vrai, le test passe ; sinon, pytest affiche l'échec.


def test_est_pair():
    # Cas pair : on attend True
    assert est_pair(4)
    # Cas impair : on attend False (assert not …)
    assert not est_pair(7)
    assert est_pair(8)


# T3 : parametrize avec tuples (entrée, résultat attendu).
# Chaque cas = un test à part (pytest en affichera autant que de tuples).
@pytest.mark.parametrize("nombre, resultat", [
    (0, False),      # < 2 → pas premier
    (1, False),      # < 2 → pas premier
    (2, True),       # plus petit nombre premier
    (3, True),       # premier
    (4, False),      # 2×2
    (25, False),     # 5×5 : carré d'un premier
    (49, False),     # 7×7 : carré d'un premier
    (97, True),      # grand premier
    (7919, True),    # encore plus grand
    (-7, False),     # négatif → pas premier
    (2.5, False),    # décimal non entier → False
    (7.3, False),    # décimal non entier → False
    (5.0, True),     # flottant mais valeur entière d'un premier
])
def test_est_premier(nombre, resultat):
    # On compare le booléen renvoyé à la valeur attendue du tuple
    assert est_premier(nombre) == resultat


def test_est_majeur():
    # 18 ans : limite exacte, doit être considéré majeur
    assert est_majeur(18)


# @pytest.mark.parametrize = décorateur : pytest relance le même test
# une fois par valeur de la liste. Chaque cas compte comme un test à part.
# Avantage : si "radar" échoue, on sait quand même si "kayak" passe.
@pytest.mark.parametrize("mot", ["kayak", "radar", "Kayak", "a", "", "Esope reste ici et se repose"])
def test_palindromes(mot):
    # On vérifie que chaque mot (minuscules, majuscules, espaces, vide) est un palindrome
    assert est_palindrome(mot)


# Fait la meme chose qu'au dessus, mais c'est plus long et moins propre :
# au premier assert faux, les suivants ne sont pas exécutés.
# def test_palindromes2():
#     assert est_palindrome("kayak")
#     assert est_palindrome("radar")
#     assert est_palindrome("Kayak")
#     assert est_palindrome("a")
#     assert est_palindrome("")
#     assert est_palindrome("Esope reste ici et se repose")


@pytest.mark.parametrize("mot", ["python", "kayaks", "ab", "oui", "toto"])
def test_pas_palindrome(mot):
    # Cas négatifs : ces mots ne se lisent pas pareil à l'envers
    assert not est_palindrome(mot)
