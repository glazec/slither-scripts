from slither import Slither
from slither.utils.colors import blue, green, magenta, yellow
import collections
import sys


slither = Slither('./arithmatic/test/TestContract.sol')
text=''
for c in slither.contracts:
    text+=c.name+'\n'
    for f in c.functions:
        text+='   '+f.name+'\n'
        for n in f.nodes:
            if '*' in str(n.expression) or '+' in str(n.expression) or '-' in str(n.expression) or '/' in str(n.expression):
                text+='       '+str(n.expression)+'\n'
print(text)