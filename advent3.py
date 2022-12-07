with open('advent3.txt', 'r') as f:
    packs = f.read().splitlines()

alphabets = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #init scoring string
priority_sum = 0 #init the priority sum
frame_iterator = 0 #for part b

# PART B

for pack in packs:
    if frame_iterator == 2: #with a complete pack of 3,
        frame_iterator = 3 #reset the frame iterator (part a)
        # print("THE TRIO:\n" + holding_tank_1 + "\n" + holding_tank_2 + "\n" + pack) #error checker
        for thing in pack: #read all the letters in the last pack
            if thing in holding_tank_2: #read all the letters in the second-to-last pack
                if thing in holding_tank_1: #read all the letters in the third-to-last pack
                    priority_sum += alphabets.index(thing) #add matching letter to priority sum
                    holding_tank_1 = "" #reset pack 1
                    holding_tank_2 = "" #reset pack 2
                    break
    if frame_iterator == 1: #read in second pack
        holding_tank_2 = str(pack)
        frame_iterator = 2
    if frame_iterator == 0: #read in first pack
        holding_tank_1 = str(pack)
        frame_iterator = 1
    if frame_iterator == 3: #reset the frame iterator (part b)
        frame_iterator = 0

 ### PART A
    # half_ = int(len(pack) / 2)
    # firsthalf = pack[0:half_]
    # lasthalf = pack[half_:]
    # for thing in firsthalf:
    #     if thing in lasthalf:
    #         print("Found it: " + thing)
    #         priority_sum += alphabets.index(thing)
    #         break

print("Priority sum: " + str(priority_sum))