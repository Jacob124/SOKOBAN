from random import shuffle

who = ["Jacob", "Leah", "Celesta", "Haiel", "Gloria", "Harahel", "Helia"]
give = who[:]

repeat = True
tries = 0
while repeat:
    shuffle(give)
    repeat = False
    tries += 1
    for i, g in enumerate(give):
        if who[i] == g:
            repeat = True
            break


for i in range(len(who)):
    print("%s: %s" % (who[i], give[i]))

if tries == 1:
    print(tries, "try")
else:
    print(tries, "tries")
