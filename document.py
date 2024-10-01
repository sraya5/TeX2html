from dataclasses import dataclass


class Node:
    def __init__(self, children):
        self.children = children


class Environment(Node):
    def __init__(self, name: str):
        self.name = name


@dataclass
class FreeText(Node):
    content: str


@dataclass
class Title:
    title: str
    author: str
    date: str


class Document(Environment):
    def __init__(self, title: Title):
        self.title = title


