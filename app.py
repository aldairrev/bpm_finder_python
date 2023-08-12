import time

starttime = time.time()
lasttime = starttime
value = ""

beats = []

input("Type Q and press ENTER to stop.\nPress ENTER for each beat.")

def Average(lst):   
    return sum(lst) / len(lst)

while value.lower() != "q":
    if len(beats) < 4:
        print(f"{4 - len(beats)} more...", end = " ")

    lasttime = time.time()

    value = input()
    if value.lower() != "q":
        beats.append(round((time.time() - lasttime), 3))
        if len(beats) > 3:
            bpm = Average(beats)
            print("Bpm " + str(int(round(60/bpm, 0))))
            print("Bpm precise " + str(round(60/bpm, 3)))
            print("Beats " + str(len(beats)), end = " ")

# for i in range(1, len(beats)):
#     print (f"Beat {i}: { str(beats[i])} ms" )

print("#" * 20)
print("*" * 10)
print("Bpm " + str(int(round(60/bpm, 0))))
print("*" * 10)
print(f"Beat ms max: {str(max(beats))}")
print(f"Beat ms min: {str(min(beats))}")
print(f"Beat ms average: {str(round(Average(beats), 3))}")
print("#" * 20, " ")
