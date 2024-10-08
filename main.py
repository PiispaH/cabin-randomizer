import sys

from hytti_arvonta.cabins import cabins


def main(n_cabins: int, names: list):
    try:
        result = cabins(n_cabins, names)
    except ValueError as e:
        print(f"An problem occurred: {e.args[0]}")
    for line in result:
        print(line)

if __name__ == "__main__":
    n_cabins = int(sys.argv[1])
    names = sys.argv[2:]
    main(n_cabins, names)
