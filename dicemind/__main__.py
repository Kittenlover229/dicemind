from .parsing import parse, optimize
from .roller import roll
from .interpreter import Interpreter
from .stringifier import PlaintextStringifier
from .inliner import Inliner, DEFAULT_INLINE_TABLE

interpreter = Interpreter()
stringifier = PlaintextStringifier()
inliner = Inliner(DEFAULT_INLINE_TABLE)

if __name__ == "__main__":
    while query := input("> "):
        try:
            parsed = parse(query)

            # Inline any macros
            inlined = inliner.transform(parsed)

            print(inlined.pretty())

            # Create a new optimized tree
            optimal = optimize(inlined)
            # For every dice in the tree
            roll(optimal)

            for (string, result) in zip(
                stringifier.visit(optimal),
                interpreter.evaluate(optimal),
            ):
                if result:
                    print(f"{string} = {result}")
                else:
                    print(string)
        except BaseException as err:
            print(err)
