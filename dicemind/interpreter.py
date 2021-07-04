from lark.visitors import Interpreter as LarkInterpreter
from decimal import Decimal


class Interpreter(LarkInterpreter):
    def add(self, tree) -> Decimal:
        return sum(self.visit_children(tree))

    def sub(self, tree) -> Decimal:
        first, second, *_ = self.visit_children(tree)
        return first - second

    def mul(self, tree) -> Decimal:
        first, second, *_ = self.visit_children(tree)
        return first * second

    def div(self, tree) -> Decimal:
        first, second, *_ = self.visit_children(tree)
        return first / second

    def neg(self, tree) -> Decimal:
        return -self.visit_children(tree)[0]

    def dice(self, tree) -> Decimal:
        return sum(tree.meta.rolls)

    def number(self, token) -> Decimal:
        return Decimal(token.children[0].value)
