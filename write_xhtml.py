from xml.etree.ElementTree import Element
from json import load
from document import *

with open('name2tag.json', 'r', encoding='utf8') as f:
    NAME2TAG = load(f)


def create_head(title='', css_path=''):
    head = Element('head')
    if title:
        element = Element('title', text=title)
        head.append(element)
    if css_path:
        element = Element('link', {'rel': "stylesheet", 'type': 'text/css', 'href': css_path})
        head.append(element)
    mathjax = Element('script', {'src': 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js', 'async': 'async'})
    head.append(mathjax)
    element = Element('meta', {'name': 'viewport', 'content':' width=device-width'})
    head.append(element)
    return head


def one_node(node):
    if type(node) is Environment:
        element = Element(NAME2TAG[node.environment_name]['tag'], {'class': node.environment_name})
    elif type(node) is Section:
        element = Element('section')
    else:
        raise TypeError('invalid node')
    return element



def convert(doc: Document, css_path=''):
    root = Element('html', {'xmlns': 'http://www.w3.org/1999/xhtml'})
    head = create_head(doc.title.title, css_path)
    body = Element('body')
