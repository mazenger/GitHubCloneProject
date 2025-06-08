# i = 0
# j = 0
# while i <= 2:
#     j = 0 # resting the jjjjjjjjjj
#     while j <= 2:
#         print("*", end="")
#         j += 1
#     print("*")
#     i += 1
#-------------------
# i = 0
# while i <= 4:
#     j = 0
#     while j < i:
#         print("*", end="")
#         j +=1
#     print("*")
#     i += 1

i = 1

while i < 5:
    for j in range(5) :
        print(j + 1, end="")
        j += 1
    print()
    i += 1