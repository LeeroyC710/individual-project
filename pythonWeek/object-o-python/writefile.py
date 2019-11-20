file = open("teams.txt", "w")

for n in range (1, 2):
    newline = "Manchester United" + "\n" + "HotSpurs" + "\n" + "Arsenal" + "\n" + "Chelsea" + "\n" + str(n) + "\n"
    file.write(newline)

file.close()

