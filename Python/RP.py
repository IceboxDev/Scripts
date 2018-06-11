from collections    import defaultdict
from itertools      import product

RP      = 5021
VALUES  = [375, 487, 675, 975, 1350]
POTENT  = [292, 675, 875, 1162, 1837, 3750]
RESULT  = defaultdict(list)
POOLS   = []
DEPTH   = 5

GENE = [("for "                                     +
        chr(97+i)                                   +
        " in range((RP"                             +
        (" - {} * VALUES[-{}]") * i                 +
        ") // VALUES[-"                             +
        str(i+1)                                    +
        "] + 1):\n"                                 +
        " "*((i+1)*4)).format(*[item for sublist in zip(map(chr, range(97, 97+i)), range(1,i+1)) for item in sublist]) for i in range(DEPTH)] + \
        [("POOLS.append(([range(7)] + [range((RP"   +
        (" - {} * VALUES[-{}]") * DEPTH             +
        ") // i + 1) for i in VALUES[1:-DEPTH]],("  +
        ",".join(map(chr, range(97,97+DEPTH)))      +
        ")))").format(*[item for sublist in zip(map(chr, range(97, 97+DEPTH)), range(1,DEPTH+1)) for item in sublist])]

CODE = "".join(GENE)
print(CODE)
exec(CODE)

for pool in POOLS:
    print(pool)
    for buying_choice in product(*pool[0]):
        buying_choice += pool[1][::-1]
        print(buying_choice)
        RESULT[sum(amount * price for amount, price in zip(VALUES, buying_choice))].append(buying_choice)

maximum = [max(RESULT[RP], key = lambda x: x[i])[i] for i in range(len(VALUES))]
print("Current amount of RP: %s" %RP)
print("%s Available purchase combinations" %len(RESULT[RP]))
print("With limits %s" %maximum)

for price in [i for i in range(len(VALUES)) if maximum[i]]:
    print("If you're focusing on %sRP items you can consider buying one of the following:" %VALUES[price])
    for package in [i for i in RESULT[RP] if i[price] == maximum[price]]:
        print(package)

    print()

print("Other purchases:")
print("|".join(map(lambda x: str(x)+(5-len(str(x)))*" ", [""]+POTENT)))
print("+".join(["-"*5]*7))
for other in POTENT:
    print("|".join(map(lambda x: str(x)+(5-len(str(x)))*" ", [other]+[len(RESULT[RP-other-POTENT[i]]) if other != POTENT[i] else len(RESULT[RP-other]) for i in range(len(POTENT))])))

print(RESULT[RP])