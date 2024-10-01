from xml.etree.ElementTree import Element
from json import load
from document import *

with open('name2tag.json', 'r', encoding='utf8') as f:
    NAME2TAG = load(f)


def create_head(css_path=''):
    head = Element('head')
    if css_path:
        element = Element('link', {'rel': "stylesheet", 'type': 'text/css', 'href': css_path})
        head.append(element)
    mathjax = Element('script', {'src': 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js', 'async': 'async'})
    head.append(mathjax)
    element = Element('meta', {'name': 'viewport', 'content':' width=device-width'})
    head.append(element)
    return head


def one_node(node):
    element = Element(NAME2TAG[node.name]['tag'], {'class': node.name})
    last = element
    for child in node.children:
        if type(child) is Environment
            child = one_node(child)
        elif type
    return element



def convert(doc: Document, css_path=''):
    root = Element('html', {'xmlns': 'http://www.w3.org/1999/xhtml'})
    head = create_head(css_path)
    body = Element('body')
