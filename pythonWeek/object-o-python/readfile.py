file = open("teams.txt", "w")

for n in range (1, 2):
    newline = "Manchester United HotSpurs Arsenal Chelsea" + str(n) + "\n"
    file.write(newline)

file.close()

