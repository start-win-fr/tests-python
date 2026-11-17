import pytest

from outils import moyenne

# Deux paramètres : nombres (entrée) et attendu (résultat espéré).
# Chaque tuple de la liste est un jeu de valeurs → un test indépendant.
@pytest.mark.parametrize("nombres, attendu", [
    ([10, 12, 14], 12),   # moyenne classique de trois notes
    ([5], 5),             # un seul élément : la moyenne est lui-même
    ([0, 20], 10),        # bornes 0 et 20
    ([12.5, 13.5], 13),   # flottants : 26 / 2 = 13
])
def test_moyenne(nombres, attendu):
    # On compare le résultat de moyenne(...) à la valeur attendue
    assert moyenne(nombres) == attendu


# Bonus du cours (section 6) : vérifier qu'une erreur se produit.
# with pytest.raises(ValueError) réussit si moyenne([]) lève bien ValueError,
# et échoue si la fonction accepte la liste vide sans broncher.
# def test_moyenne_liste_vide():
#     with pytest.raises(ValueError):
#         moyenne([])
