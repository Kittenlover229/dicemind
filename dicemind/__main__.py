from .parsing import parse, optimize

if __name__ == "__main__":
    while query := input("> "):
        optimal = optimize(parse(query))
        print(optimal.pretty())
