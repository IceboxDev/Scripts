from collections    import defaultdict
from random         import sample

#6 aus 49
PICKS = 6
RANGE = 49
ITERS = 1000

#Winnings
def win(hits):

    if hits > 1:
        return 10 * 2 ** (hits - 1)

    else:
        return 0

#Input
text        = "Geben sie bitte ihre %s Zahl ein aus dem Zahlenbereich 1-%s:\n"
text_list   = ["erste", "zweite", "dritte", "vierte", "fünfte", "sechste"]
user_input  = []

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
    
#1st run
interval = range(1, RANGE+1)
sampl    = sample(interval, PICKS)
hits     = sum(pick in sampl for pick in user_input)
cash     = win(hits)

print("Die Zahlen sind:")
print(*sampl)
print("Sie haben %s richtige Zahlen" %hits)
print("Sie haben %s Euro gewonen"    %cash)
print()

#1000 runs
stats   = defaultdict(int)
total   = 0

for _ in range(ITERS):
    sampl   = sample(interval, PICKS)
    hits    = sum(pick in sampl for pick in user_input)

    stats[hits] += 1
    total       += win(hits)

print("Bei %s Wiederholungen, würden sie insgesamt %s Euro gewinnen" %(ITERS, total))
print("Durschnittlich würden sie %s Euro %s cent pro spiel gewinnen" %tuple(str(round(total/ITERS, 2)).split(".")))
print("Hier sehen sie eine statistische Zusammenfassung ihrer %s Spiele:" %ITERS)
print()
print("-"*18, "No|Anzahl |Gewinn|", "-"*18, sep = "\n")

for H in range(PICKS+1):
    S = str(stats[H])
    W = str(win(H))
    
    print(H, S + " "*(5-len(S)), W + " "*(5-len(W)), sep = " | ", end = "|\n")
