from slither import Slither
from slither.utils.colors import blue, green, magenta, yellow
import collections
import sys

def run(filename):
    """Executes script"""

    # Init Slither
    slither = Slither(filename)
    if not len(slither.contracts):
        print(f"Error: Slither could not find any contracts")
        exit(-1)

    text = ""
    for c in slither.contracts:
            text += blue(f"\n+ Contract {c.name}\n")

            collect = collections.defaultdict(list)

            collect[c.name].append(c.modifiers)
            text +="\n"+'\n'.join([m.name for m in c.modifiers])+"\n"
    print(text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python modifier.py <contract.sol>')
        exit(-1)

    FILE_NAME = sys.argv[1]
    run(FILE_NAME)
