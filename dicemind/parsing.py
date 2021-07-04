from lark import Tree, Lark, Transformer, Token
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
        if tokens[0].data == "pos":
            return tokens[0].children[0]
        return Tree("pos", tokens, None)


UNARY_OPTIMIZER = UnaryOptimizer(visit_tokens=True)


def parse(string: str) -> Tree:
    return parser.parse(string)


def optimize(tree: Tree) -> Tree:
    return UNARY_OPTIMIZER.transform(tree)
