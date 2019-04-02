from bs4 import BeautifulSoup

def match_class(target):#Encontramos la clase con el identificador indicado.
    def do_match(tag):
        classes = tag.get('class', [])
        return all(c in classes for c in target)
    return do_match