from xml.etree.ElementTree import Element, ElementTree
from json import load
from sys import argv
from read_LaTeX import parse_document
from document import *

with open('name2tag.json', 'r', encoding='utf8') as f:
    NAME2TAG = load(f)


def one_node(node):
    if type(node) is Environment:
        element = Element(NAME2TAG[node.environment_name]['tag'], {'class': node.environment_name})
    elif type(node) is Section:
        element = Element('section')
    elif type(node) is Document:
        element = Element('body')
    else:
        raise TypeError('invalid node')
    element.text = ''
    element.tail = ''
    return element


def scan(node):
    element = one_node(node)
    last = None
    for child in node.children:
        if type(child) in (Environment, Section):
            last = scan(child)
            element.append(last)
        elif type(child) is FreeText:
            if last is not None:
                last.tail += child.content
            else:
                element.text += child.content
    return element


def create_head(title='', css_path=''):
    head = Element('head')
    if title:
        element = Element('title')
        element.text = title
        head.append(element)
    if css_path:
        element = Element('link', {'rel': "stylesheet", 'type': 'text/css', 'href': css_path})
        head.append(element)
    mathjax = Element('script', {'src': 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js', 'async': 'async'})
    head.append(mathjax)
    element = Element('meta', {'name': 'viewport', 'content':' width=device-width'})
    head.append(element)
    return head


def convert(doc: Document, css_path=''):
    root = Element('html', {'xmlns': 'http://www.w3.org/1999/xhtml'})
    head = create_head(doc.title.title, css_path)
    body = scan(doc)
    root.extend((head, body))
    tree = ElementTree(root)
    return tree


def main():
    if len(argv) != 3:
        raise Exception

    with open(argv[1], 'r', encoding='utf8') as file:
        content = file.read()
        doc = parse_document(content)[0]
        tree = convert(doc)
        tree.write(argv[2], encoding='utf-8')

if __name__ == '__main__':
    main()
