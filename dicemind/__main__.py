from .parsing import parse, optimize

if __name__ == "__main__":
    while query := input("> "):
        print(optimize(parse(query)).pretty())
