from .parsing import parse, optimize
from .roller import roll
from .interpreter import Interpreter

interpreter = Interpreter()

if __name__ == "__main__":
    while query := input("> "):
        # Create a new optimized tree
        optimal = optimize(parse(query))
        # For every dice in the tree
        roll(optimal)

        print(optimal.pretty())
        print(interpreter.visit(optimal)[0])
