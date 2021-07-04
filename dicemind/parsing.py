from lark import Tree, Lark
from os import path

parser = Lark(
    open(
        path.join(path.dirname(__file__), "grammars", "dice.lark")
    ).read(),
    ambiguity="resolve",
)


def parse(string: str) -> Tree:
    return parser.parse(string)
