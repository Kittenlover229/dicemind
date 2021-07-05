from lark import Tree, Token, Transformer, Discard
from abc import ABC, abstractmethod
from typing import Optional, Dict


class AbstractInlineTable(ABC):
    @abstractmethod
    def get(self, name: str) -> Optional[Tree]:
        ...

    @abstractmethod
    def put(self, name: str, tree: Tree):
        ...


class DictInlineTable(AbstractInlineTable):
    def __init__(self, dictionary: Dict[str, Tree]):
        self.table = dictionary

    def get(
        self, name: str, meta: Optional[object] = None
    ) -> Optional[Tree]:
        del meta
        return self.table.get(name)

    def put(self, name: str, tree: Tree, meta: Optional[object] = None):
        del meta
        self.table[name] = tree


DEFAULT_INLINE_TABLE = DictInlineTable(
    {"one": Tree("number", [Token("NUMBER", "1")])}
)


class Inliner(Transformer):
    def __init__(self, inline_table: AbstractInlineTable):
        self.inline_table = inline_table

    def binding(self, children):
        # TODO: mutate inliner state
        raise Discard()

    def var(self, children):
        varname = children[0].value
        return Tree("paren", [self.inline_table.get(varname)])
