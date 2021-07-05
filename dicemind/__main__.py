from .parsing import parse, optimize
from .roller import roll
from .interpreter import Interpreter
from .stringifier import PlaintextStringifier

interpreter = Interpreter()
stringifier = PlaintextStringifier()

if __name__ == "__main__":
    while query := input("> "):
        # Create a new optimized tree
        optimal = optimize(parse(query))
        # For every dice in the tree
        roll(optimal)

        for (string, result) in zip(
            stringifier.visit(optimal), interpreter.visit(optimal)
        ):
            print(f"{string} = {result}")
