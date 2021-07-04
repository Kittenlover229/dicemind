from typing import Callable, NamedTuple, List
from lark import Visitor, Tree
from random import randint


class Dice(NamedTuple):
    amount: int
    power: int


class Roller(Visitor):
    def __init__(self, roll: Callable[[Dice, Tree], List[int]]):
        self.roll = roll

    def dice(self, expr):
        die = Dice(expr.meta.amount, expr.meta.power)
        expr.meta.rolls = self.roll(die, expr)


DEFAULT_ROLLER = Roller(
    lambda d, _: [randint(1, d.power) for _ in range(d.amount)]
)


def roll(tree: Tree):
    DEFAULT_ROLLER.visit(tree)
