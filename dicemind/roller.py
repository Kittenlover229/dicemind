from typing import Callable, NamedTuple, List
from lark import Visitor, Tree
from random import randint
from decimal import Decimal


class Dice(NamedTuple):
    amount: int
    power: int


class Roller(Visitor):
    def __init__(self, roll: Callable[[Dice, Tree], List[Decimal]]):
        self.roll = roll

    def dice(self, expr):
        die = Dice(expr.meta.amount, expr.meta.power)
        expr.meta.rolls = self.roll(die, expr)


DEFAULT_ROLLER = Roller(
    lambda d, _: [Decimal(randint(1, d.power)) for _ in range(d.amount)]
)


def roll(tree: Tree):
    DEFAULT_ROLLER.visit(tree)
