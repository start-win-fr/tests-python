from diagnostic import analyser, categorie, taille_lisible

def test_categorie():
    assert categorie("script.py") == "python"
    assert categorie("NOTES.TXT") == "texte"
    assert categorie("Makefile") == "autre"

def test_taille_lisible():
    assert taille_lisible(512) == "512 o"
    assert taille_lisible(10240) == "10.0 Ko"

def test_analyser_compte_les_fichiers(tmp_path):
    (tmp_path / "a.py").write_text("print('a')")
    (tmp_path / "notes.txt").write_text("bonjour")
    (tmp_path / "logs").mkdir()
    (tmp_path / "logs" / "app.log").write_text("")
    stats = analyser(tmp_path)
    assert stats["total"] == 3
    assert stats["python"] == 1
    assert stats["log"] == 1
    assert stats["gros"] == []

def test_analyser_detecte_les_gros_fichiers(tmp_path):
    (tmp_path / "video.mp4").write_bytes(bytes(6 * 1024 * 1024))
    stats = analyser(tmp_path)
    assert stats["gros"] == ["video.mp4"]

def test_analyser_skip_git(tmp_path):
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "HEAD").write_text("ref: refs/heads/main")
    (tmp_path / "a.py").write_text("")

    stats = analyser(tmp_path)

    assert stats["total"] == 1


def test_est_pair_refuse_les_decimaux():
    with pytest.raises(TypeError):
        est_pair(2.5)


def test_moyenne():
    assert moyenne([10, 20]) == 15


def test_moyenne_liste_vide():
    with pytest.raises(ValueError):
        moyenne([])


# T8
def test_demander_entier(monkeypatch):
    reponses = iter(["abc", "2.5", "42"])
    monkeypatch.setattr("builtins.input", lambda question: next(reponses))
    assert demander_entier("Un nombre : ") == 42


def test_demander_entier_previent_l_utilisateur(monkeypatch, capsys):
    reponses = iter(["abc", "7"])
    monkeypatch.setattr("builtins.input", lambda question: next(reponses))
    demander_entier("Un nombre : ")
    assert "pas un nombre entier" in capsys.readouterr().out
