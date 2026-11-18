import pytest

from diagnostic import analyser, categorie, taille_lisible
from outils import est_pair, moyenne, demander_entier


def test_categorie():
    # Extension .py → catégorie "python"
    assert categorie("script.py") == "python"
    # Majuscules ignorées : .TXT → "texte"
    assert categorie("NOTES.TXT") == "texte"
    # Extension inconnue → "autre"
    assert categorie("Makefile") == "autre"


def test_taille_lisible():
    # Moins de 1024 octets → affichage en "o"
    assert taille_lisible(512) == "512 o"
    # À partir de 1024 → conversion en Ko avec une décimale
    assert taille_lisible(10240) == "10.0 Ko"


# tmp_path = fixture pytest : dossier temporaire neuf, nettoyé après le test.
# Schéma en 3 temps : préparer → agir → vérifier.
def test_analyser_compte_les_fichiers(tmp_path):
    # Préparer : créer des fichiers et un sous-dossier dans tmp_path
    (tmp_path / "a.py").write_text("print('a')")
    (tmp_path / "notes.txt").write_text("bonjour")
    (tmp_path / "logs").mkdir()
    (tmp_path / "logs" / "app.log").write_text("")
    # Agir
    stats = analyser(tmp_path)
    # Vérifier les compteurs
    assert stats["total"] == 3
    assert stats["python"] == 1
    assert stats["log"] == 1
    assert stats["gros"] == []


def test_analyser_detecte_les_gros_fichiers(tmp_path):
    # Fichier de 6 Mo (> LIMITE de 5 Mo) → doit apparaître dans "gros"
    (tmp_path / "video.mp4").write_bytes(bytes(6 * 1024 * 1024))
    stats = analyser(tmp_path)
    assert stats["gros"] == ["video.mp4"]


# T5 : les fichiers sous .git ne doivent pas être comptés
def test_analyser_skip_git(tmp_path):
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "HEAD").write_text("ref: refs/heads/main")
    (tmp_path / "a.py").write_text("")

    stats = analyser(tmp_path)

    # Seul a.py compte ; HEAD dans .git est ignoré
    assert stats["total"] == 1


# T4 : est_pair doit refuser un décimal (TypeError)
def test_est_pair_refuse_les_decimaux():
    with pytest.raises(TypeError):
        est_pair(2.5)


def test_moyenne():
    assert moyenne([10, 20]) == 15


# with pytest.raises : le test réussit seulement si ValueError est bien levée
def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])


# T8 : monkeypatch remplace input() par un distributeur de réponses factices.
# iter + next : "abc", puis "2.5", puis "42" — sans rien taper au clavier.
def test_demander_entier(monkeypatch):
    reponses = iter(["abc", "2.5", "42"])
    monkeypatch.setattr("builtins.input", lambda question: next(reponses))
    assert demander_entier("Un nombre : ") == 42


# capsys capture ce que print() affiche ; on vérifie le message d'erreur
def test_demander_entier_previent_l_utilisateur(monkeypatch, capsys):
    reponses = iter(["abc", "7"])
    monkeypatch.setattr("builtins.input", lambda question: next(reponses))
    demander_entier("Un nombre : ")
    assert "pas un nombre entier" in capsys.readouterr().out
