file = open("teams.txt", "r")

outfile = "West Ham"  "\n"
for line in range(8):
  if line % 2 == 0:
    outfile += file.readline()
  else:
    file.readline()

file = open("teams.txt", "w")
file.write(outfile)

file.close()

