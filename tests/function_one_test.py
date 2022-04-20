from lib.function_one import wiki
from lib.function_one import search_wiki

def test_wiki():
    assert "War" in wiki()
def test_search():
    assert "Presidency of Barack Obama" in search_wiki('Barack Obama')
    