import sys
from pprint import pprint

pprint(sys.modules)

for module in sorted(sys.modules):
    print(module)
