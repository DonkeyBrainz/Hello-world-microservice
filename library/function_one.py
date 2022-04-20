import wikipedia

def wiki(name = "War", length = 1):
    """This is a wiki fetcher"""
    my_wiki =wikipedia.summary(name,length)
    return my_wiki
def search_wiki(name):
    """Search the wiki for names"""
    results = wikipedia.search(name)
    return results