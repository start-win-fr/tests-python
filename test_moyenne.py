import pytest

from outils import moyenne

@pytest.mark.parametrize("nombres, attendu", [
    ([10, 12, 14], 12),
    ([5], 5),
    ([0, 20], 10),
    ([12.5, 13.5], 13)
])
def test_moyenne(nombres, attendu):
    assert moyenne(nombres) == attendu

