import math

# class Elf:
#     def __init__(self, name, calorie_total, snack_list):
#         self.name = "Elf" + str(iterator)
#         self.calorie_total = 0
#         self.snack_list = []    
#     def get_calorie_total(self):
#         return self.get_calorie_total
#     def get_snack_list(self):
#         return self.get_snack_list

snacklist = []
with open("advent1.txt", 'r') as openfile:  #read the file
    text = openfile.read()                  #read the file
    sum_calories = 0 #initialize calorie sum
    calorie_champ = 0
    calorie_2nd = 0
    calorie_3rd = 0
    for line in text.splitlines():
        if line == "":
            snacklist.append(int(sum_calories))
            sum_calories = 0
        else:
            sum_calories += int(line)
sortedsnacks = sorted(snacklist)

print("The elf carrying the most calories is carrying " + str(sortedsnacks[-1]))
print("The elf carrying the 2nd most calories is carrying " + str(sortedsnacks[-2]))
print("The elf carrying the 3rd most calories is carrying " + str(sortedsnacks[-3]))
calorie_trio = sortedsnacks[-1] + sortedsnacks[-2] + sortedsnacks[-3]
print("That calorie sum = " + str(calorie_trio))