#! python3
import random
numberOfStreaks = 0
wow = 0
WOW = 0
COMBO = 0
a = []
for experimentNumber in range(1000000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    a.append(random.randint(0, 1))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if len(a) > 24:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-6] != a[-7]:
            numberOfStreaks += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11] \
                == a[-12] and a[-12] != a[-13]:
            numberOfStreaks += 1
            wow += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] == a[-13] == a[-14] == a[-15] == a[-16] == a[-17] == a[-18] and a[-18] != a[-19]:
            numberOfStreaks += 1
            WOW += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] == a[-13] == a[-14] == a[-15] == a[-16] == a[-17] == a[-18] == a[-19] == a[-20]\
                == a[-21] == a[-22] == a[-23] == a[-24] and a[-24] != a[-25]:
            numberOfStreaks += 1
            WOW += 1
            COMBO += 1
    elif len(a) > 23:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-6] != a[-7]:
            numberOfStreaks += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11] \
                == a[-12] and a[-12] != a[-13]:
            numberOfStreaks += 1
            wow += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] == a[-13] == a[-14] == a[-15] == a[-16] == a[-17] == a[-18] and a[-18] != a[-19]:
            numberOfStreaks += 1
            WOW += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] == a[-13] == a[-14] == a[-15] == a[-16] == a[-17] == a[-18] == a[-19] == a[-20]\
                == a[-21] == a[-22] == a[-23] == a[-24]:
            numberOfStreaks += 1
            WOW += 1
            COMBO += 1
    elif len(a) > 18:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-6] != a[-7]:
            numberOfStreaks += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11] \
                == a[-12] and a[-12] != a[-13]:
            numberOfStreaks += 1
            wow += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] == a[-13] == a[-14] == a[-15] == a[-16] == a[-17] == a[-18] and a[-18] != a[-19]:
            numberOfStreaks += 1
            WOW += 1
    elif len(a) > 17:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-6] != a[-7]:
            numberOfStreaks += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11] \
                == a[-12] and a[-12] != a[-13]:
            numberOfStreaks += 1
            wow += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] == a[-13] == a[-14] == a[-15] == a[-16] == a[-17] == a[-18]:
            numberOfStreaks += 1
            WOW += 1
    elif len(a) > 12:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-6] != a[-7]:
            numberOfStreaks += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12] and a[-12] != a[-13]:
            numberOfStreaks += 1
            wow += 1
    elif len(a) > 11:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-6] != a[-7]:
            numberOfStreaks += 1
        elif a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] == a[-7] == a[-8] == a[-9] == a[-10] == a[-11]\
                == a[-12]:
            numberOfStreaks += 1
            wow += 1
    elif len(a) > 6:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6] and a[-7] != a[-6]:
            numberOfStreaks += 1
    elif len(a) > 5:
        if a[-1] == a[-2] == a[-3] == a[-4] == a[-5] == a[-6]:
            numberOfStreaks += 1

print("Number Of Streaks 6 in a row: " + str(numberOfStreaks))
print("Number Of Streaks 12 in a row: " + str(wow))
print("Number Of Streaks 18 in a row: " + str(WOW))
print("Number Of Streaks 24 in a row: " + str(COMBO))
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))
