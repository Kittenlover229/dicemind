from .parsing import parse

if __name__ == "__main__":
    while query := input("> "):
        print(parse(query).pretty())
