from collections import defaultdict
import itertools
RP      : int = 2097

SKINS   : dict = {295  : False,
                  260  : True,    # 520  Skins 50%
                  375  : True,    # 750  Skins 50%
                  487  : True,    # 975  Skins 50%
                  675  : True,    # 1350 Skins 50%
                  975  : True,    # 1350 Skins 35%
                  1350 : True,    # 1820 Skins 35%
                  }

PRICES  : list = sorted([price for price in SKINS if SKINS[price]], reverse=True)
RESULT  : defaultdict = defaultdict(list)
POTENT  = [292, 390, 875]


def options(pool: list = [], index: int = 0, price: int = 0) -> None:

    if index + 1 != len(PRICES):
        for amount in range((RP - price) // PRICES[index] + 1):
            options(pool + [amount], index + 1, price + PRICES[index]*amount)

    else:
        for amount in range((RP - price) // PRICES[index] + 1):
            RESULT[price + PRICES[index]*amount].append(tuple((pool + [amount])[::-1]))


options()
maximum = [max(RESULT[RP], key = lambda x: x[i])[i] for i in range(len(PRICES))]
print("Current amount of RP: %s" %RP)
print("%s Available purchase combinations" %len(RESULT[RP]))
print("With limits %s" %maximum)

for price in [i for i in range(len(PRICES)) if maximum[i]]:
    print("If you're focusing on %sRP items you can consider buying one of the following:" %PRICES[::-1][price])
    for package in [i for i in RESULT[RP] if i[price] == maximum[price]]:
        print(package)

    print()

print("Other purchases:")
print("|".join(map(lambda x: str(x)+(5-len(str(x)))*" ", [""]+POTENT)))
print("+".join(["-"*5]*7))
for other in POTENT:
    print("|".join(map(lambda x: str(x)+(5-len(str(x)))*" ", [other]+[len(RESULT[RP-other-POTENT[i]]) if other != POTENT[i] else len(RESULT[RP-other]) for i in range(len(POTENT))])))

possibl = []
for i in [a for b in [itertools.combinations(POTENT, r=q) for q in range(1, len(POTENT))] for a in b]:
    if RESULT[RP-sum(i)]:
        for a in RESULT[RP-sum(i)]:
            possibl.append((i, a))

possibl.sort(key = lambda x: x[1][1])
print(possibl)

for x in possibl:
    if x[1][0]+ x[1][1] == 1:
        print(x)
