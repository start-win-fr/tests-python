import pytest

from outils import est_pair, est_premier, est_majeur, est_palindrome

def test_est_pair():
    assert est_pair(4) # On attend que le resultat soit vrai
    assert not est_pair(7) # On attend que le resultat ne soit pas vrai (donc faux)
    assert est_pair(8)

def test_est_premier():
    assert est_premier(2)
    assert est_premier(97)
    assert not est_premier(1)
    assert not est_premier(9)

def test_est_majeur():
    assert est_majeur(18)


@pytest.mark.parametrize("mot", ["kayak", "radar", "Kayak", "a", "", "Esope reste ici et se repose"])
def test_palindromes(mot):
    assert est_palindrome(mot)

# Fait la meme chose qu'au dessus, mais c'est plus long et moins propre
# def test_palindromes2():
#     assert est_palindrome("kayak")
#     assert est_palindrome("radar")
#     assert est_palindrome("Kayak")
#     assert est_palindrome("a")
#     assert est_palindrome("")
#     assert est_palindrome("Esope reste ici et se repose")

@pytest.mark.parametrize("mot", ["python", "kayaks", "ab", "oui", 'toto'])
def test_pas_palindrome(mot):
    assert not est_palindrome(mot)