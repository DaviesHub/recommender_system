movies_dic = {}
fhand = open("movies.txt", "r")
for line in fhand:
    line = line.split(":")
    print(line)
