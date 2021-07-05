from lark import Tree, Lark, Transformer, Token
from lark.tree import Meta
from os import path

parser = Lark(
    open(
        path.join(path.dirname(__file__), "grammars", "dice.lark")
    ).read(),
    ambiguity="resolve",
)


class UnaryOptimizer(Transformer):
    def neg(self, tokens):
        if tokens[0].data == "neg":
            return tokens[0].children[0]
        return Tree("neg", tokens, None)

    def pos(self, tokens):
        return tokens[0]


UNARY_OPTIMIZER = UnaryOptimizer(visit_tokens=True)


class DiceFieldInjector(Transformer):
    def dice(self, children):
        metadata = Meta()
        metadata.empty = False

        assert len(children) == 2
        assert children[0].data == "dice_amount"
        assert children[1].data == "dice_power"

        if children[0].children:
            metadata.amount = int(children[0].children[0].value)
        else:
            metadata.amount = 1

        if children[1].children:
            metadata.power = int(children[1].children[0].value)
        else:
            metadata.power = 20

        return Tree("dice", [], metadata)


DICE_FIELD_INJECTOR = DiceFieldInjector()


class DullDiceCleaner(Transformer):
    # I hate that I have to do this, but lark doesn't pass metadata to ordinary functions
    def __default__(self, data, children, meta):
        if data == "dice":
            if meta.amount == 0 or meta.power == 0:
                return Tree("number", [Token("NUMBER", "0")])
            if meta.power == 1:
                return Tree("number", [Token("NUMBER", "1")])
        return Transformer.__default__(self, data, children, meta)


DULL_DICE_CLEANER = DullDiceCleaner()


class ExpressionOpener(Transformer):
    def expr(self, children):
        return children[0]


EXPRESSION_OPENER = ExpressionOpener()

OPTIMIZER = (
    EXPRESSION_OPENER
    * UNARY_OPTIMIZER
    * DICE_FIELD_INJECTOR
    * DULL_DICE_CLEANER
)


def parse(string: str) -> Tree:
    return parser.parse(string)


def optimize(tree: Tree) -> Tree:
    return OPTIMIZER.transform(tree)
