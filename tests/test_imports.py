def test_imports():
    from src.bot import main

    assert main


def test_package_version():
    import src

    assert src.__version__
