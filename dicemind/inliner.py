from abc import ABC, abstractmethod
from typing import Optional, Dict
from lark import Tree, Token


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
