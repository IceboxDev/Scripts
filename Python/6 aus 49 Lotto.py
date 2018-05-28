from collections    import defaultdict
from random         import sample
from typing         import Union

# Types
EURO = Union[int, float]

# 6 aus 49
PRICE: int = 5
PICKS: int = 6
RANGE: int = 49
ITERS: int = 1000


# Winnings
def win(hits: int) -> EURO:

    prizes = {0: 0      ,
              1: 0      ,
              2: 5      ,
              3: 10.2   ,
              4: 22.3   ,
              5: 5308.4 ,
              6: 3175968, }

    return prizes[hits]

# Input
text        : str   = "Geben sie bitte ihre %s Zahl ein aus dem Zahlenbereich 1-%s:\n"
text_list   : list  = ["erste", "zweite", "dritte", "vierte", "fünfte", "sechste"]
user_input  : list  = []

while len(user_input) < PICKS:

    try:
        new_input = input(text %(text_list[len(user_input)], RANGE))
        new_input = int(new_input)

        assert 1 <= new_input <= RANGE

        if new_input in user_input:
            raise Exception

        user_input.append(new_input)
        
    except ValueError:
        print("Dies ist keine Zahl!")

    except AssertionError:
        print("Diese Zahl ist ungültig, sie liegt außerhalb des Zahlenbereichs!")

    except IndexError:
        print("text_list muss erweitert werden!")
        exit()
        
    except Exception:
        print("Keine Zahl darf doppelt vorkommen!")
    
# 1st run
interval = range(1, RANGE+1)
sampl    = sample(interval, PICKS)
hit_sum  = sum(pick in sampl for pick in user_input)
cash     = win(hit_sum)

print("Die Zahlen sind:")
print(*sampl)
print("Sie haben %s richtige Zahlen" %hit_sum)
print("Sie haben %s Euro gewonen"    %cash   )
print()

# 1000 runs
stats   = defaultdict(int)
total   = 0

for _ in range(ITERS):
    sampl   = sample(interval, PICKS)
    hit_sum = sum(pick in sampl for pick in user_input)

    stats[hit_sum] += 1
    total       += win(hit_sum)

print("Bei %s Wiederholungen, würden sie insgesamt %s Euro gewinnen" % (ITERS, round(total, 2)))
print("Durschnittlich würden sie %s Euro %s cent pro spiel gewinnen" % tuple(str(round(total/ITERS, 2)).split(".")))
print("Hier sehen sie eine statistische Zusammenfassung ihrer %s Spiele:" % ITERS)
print()
print("-"*20, "No|Anzahl |Gewinn  |", "-"*20, sep="\n")

for H in range(PICKS+1):
    S = str(stats[H])
    W = str(win(H))
    
    print(H, S.ljust(5), W.ljust(7), sep=" | ", end="|\n")
