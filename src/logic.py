import wikipedia


def wiki(name="War Goddess", length=1):
    """Wikipedia fetcher"""
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def wiki_search(name: str):
    """Name Search In Wikipedia"""
    names = wikipedia.search(name)
    return names
