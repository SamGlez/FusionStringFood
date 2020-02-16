
selection = input("Please enter the string you want to convert into Michelin Star Fusion Food:\n")
currentMax = ""
record =""

for char in selection:
    if (currentMax == ''):
        currentMax = char
    elif (currentMax[-1] <= char):
        currentMax += char
    elif (currentMax[-1] > char):
        if (len(record) < len(currentMax)):
            r = currentMax
            currentMax = char
        else:
            currentMax = char
if (len(currentMax) > len(record)):
    record = currentMax


    print("Your Michelin Star Fusion Food aka the longest string in alphabetical order is: " + record)

