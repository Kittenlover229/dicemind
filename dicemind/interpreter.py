from lark.visitors import Interpreter as LarkInterpreter


class Interpreter(LarkInterpreter):
    def add(self, tree) -> int:
        return sum(self.visit_children(tree))

    def sub(self, tree) -> int:
        first, second, *_ = self.visit_children(tree)
        return first - second

    def mul(self, tree) -> int:
        first, second, *_ = self.visit_children(tree)
        return first * second

    def div(self, tree) -> int:
        first, second, *_ = self.visit_children(tree)
        return first // second

    def neg(self, tree) -> int:
        return -self.visit_children(tree)[0]

    def dice(self, tree) -> int:
        return sum(tree.meta.rolls)

    def number(self, token) -> int:
        return int(token.children[0].value)
