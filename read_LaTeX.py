from document import *

def choice(parsers):
    def p(text):
        for parser in parsers:
            res = parser(text)
            if res is not None:
                return res
        return None
    return p 

def parse_node(text):
    return choice([parse_document, parse_section, parse_freetext])(text)

def parse_nodes(text):
    children = []
    while text:
        res = parse_node(text)
        if res is None:
            return None

        node, text = res
        children.append(node)

    return children, text

def parse_freetext(text):
    if text.startswith('\\'):
        text = text[1:] # fixme

    splitted = text.split('\\', 1)
    if len(splitted) == 2:
        return FreeText(splitted[0]), '\\' + splitted[1]

    splitted = text.split('}', 1)
    if len(splitted) == 2:
        return FreeText(splitted[0]), splitted[1]
    
    return FreeText(text), ""
    

def parse_section(text):
    text = text.strip()
    if not text.startswith('\\section{'):
        return None

    splitted = text.split('\\section{', 1)
    if len(splitted) != 2:
        return None
    
    splitted = splitted[1].split('}', 1)
    if len(splitted) != 2:
        return None
    
    res = parse_nodes(splitted[0])
    if res is None:
        return None
    
    nodes, _ = res

    return Section(nodes, 'section'), splitted[1]

def parse_document(text: str) -> (Document, str):
    text = text.strip()
    if not text.startswith('\\begin{document}'):
        return None
    splitted = text.split('\\begin{document}', 1)
    if len(splitted) != 2:
        return None

    splitted = splitted[1].split('\\end{document}', 1)
    if len(splitted) != 2:
        return None
    
    text = splitted[0].strip()
    
    res = parse_nodes(text)
    if res is None:
        return None
    
    children, text = res

    return Document(None, children), text
    
