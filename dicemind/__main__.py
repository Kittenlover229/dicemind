from .parsing import parse, optimize
from .roller import roll
from .interpreter import Interpreter
from .stringifier import PlaintextStringifier
from .inliner import InlineError, Inliner, DEFAULT_INLINE_TABLE
from lark import UnexpectedCharacters

interpreter = Interpreter()
stringifier = PlaintextStringifier()
inliner = Inliner(DEFAULT_INLINE_TABLE)


def main(*args, **kwargs):
    del args
    del kwargs
    while query := input("> "):
        try:
            parsed = parse(query)

            # Inline any macros
            inlined = inliner.transform(parsed)
            # Create a new optimized tree
            optimal = optimize(inlined)
            # Roll the dice!
            roll(optimal)

            strings = stringifier.stringify(optimal)
            values = interpreter.evaluate(optimal)

            for (string, result) in zip(
                strings,
                values,
            ):
                if result is not None:
                    print(f"{string} = {result}")
                else:
                    # There was a binding, no need for equal sign
                    print(string)

        except InlineError as err:
            print(err)
        except UnexpectedCharacters as err:
            print(err)
        except BaseException as err:
            raise err


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
