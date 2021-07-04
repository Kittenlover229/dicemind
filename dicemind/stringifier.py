from decimal import Decimal
from lark.visitors import Interpreter as LarkInterpreter
from lark import Tree


class PlaintextStringifier(LarkInterpreter):
    def add(self, tree) -> str:
        first, second, *_ = self.visit_children(tree)
        return f"{first} + {second}"

    def sub(self, tree) -> str:
        first, second, *_ = self.visit_children(tree)
        return f"{first} - {second}"

    def mul(self, tree) -> str:
        first, second, *_ = self.visit_children(tree)
        return f"{first} * {second}"

    def div(self, tree) -> str:
        first, second, *_ = self.visit_children(tree)
        return f"{first} / {second}"

    def neg(self, tree) -> str:
        return f"-{self.visit_children(tree)[0]}"

    def dice(self, tree) -> str:
        return f"{tree.meta.amount if tree.meta.amount > 1 else ''}d{tree.meta.power} [ {','.join([str(x) for x in tree.meta.rolls])} ]"

    def number(self, token) -> str:
        return token.children[0].value

    def paren(self, tree) -> str:
        value, *_ = self.visit_children(tree)
        return f"({value})"
