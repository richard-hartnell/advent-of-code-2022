import math

score = 0
strats = []
with open("advent2.txt", 'r') as openfile:
    text = openfile.read()
    strats = text.splitlines()
    print("Strats 1: " + strats[0])
    print("Strats end: " + strats[-2])

# for strat in strats:
#     temp_score = 0
#     if strat[2] == "X": #if rock
#         temp_score += 1
#         if strat[0] == "A": #rock ties
#             temp_score += 3
#         if strat[0] == "C": #scissors loses
#             temp_score += 6
#     if strat[2] == "Y": #if paper
#         temp_score += 2
#         if strat[0] == "B": #paper ties
#             temp_score += 3
#         if strat[0] == "A": #rock loses
#             temp_score += 6
#     if strat[2] == "Z": #if scissors
#         temp_score += 3
#         if strat[0] == "C": #scissors ties
#             temp_score += 3
#         if strat[0] == "B": #paper loses
#             temp_score += 6
#     # print("Strat: " + strat)
#     # print("Score: " + str(temp_score))
#     score += temp_score
#     # print("New score: " + str(score))

for strat in strats:
    temp_score = 0
    if strat[2] == "X": #lose!
        # temp_score += 1
        if strat[0] == "A": #sciss lose to rock
            temp_score += 3
        if strat[0] == "B": #paper lose to sciss
            temp_score += 1
        if strat[0] == "C": 
            temp_score += 2
    if strat[2] == "Y": #tie!
        # temp_score += 2
        if strat[0] == "C":
            temp_score += 6
        if strat[0] == "B":
            temp_score += 5
        if strat[0] == "A":
            temp_score += 4
    if strat[2] == "Z": #win!
        # temp_score += 3
        if strat[0] == "C":
            temp_score += 7
        if strat[0] == "B":
            temp_score += 9
        if strat[0] == "A":
            temp_score += 8
    # print("Strat: " + strat)
    # print("Score: " + str(temp_score))
    score += temp_score
    # print("New score: " + str(score))

print("Score: " + str(score))