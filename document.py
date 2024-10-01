from dataclasses import dataclass


class Node:
    def __init__(self, children):
        self.children = children


class Environment(Node):
    def __init__(self, environment_name: str, children: list):
        super().__init__(children)
        self.environment_name = environment_name


@dataclass
class FreeText(Node):
    content: str


@dataclass
class Title:
    title: str
    author: str
    date: str


class Document(Environment):
    def __init__(self, title: Title, children: list):
        super().__init__("document", children)
        self.title = title

class Section(Node):
    def __init__(self, children: list, sort):
        super().__init__(children)
        self.sort = sort

