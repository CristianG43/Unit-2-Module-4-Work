from main import destinations, adventure


def test_destinations_valid():
    result = destinations("Midgard")
    assert result is not None

def test_destinations_invalid():
    result = destinations("Invalid")
    assert result is None

def test_adventure_valid():
    result = adventure("Midgard")
    assert result == True

def test_adventure_invalid():
    result = adventure("Invalid")
    assert result == False
