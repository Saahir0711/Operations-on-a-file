file = open("Codingal.txt", "r")
print(file.read(8))
file.close()

file = open("Codingal.txt", "r")
print(file.readline())
file.close()

file = open("Codingal.txt", "r")
print(file.readlines())
file.close()

file = open("Codingal.txt", "r")
for line in file:
    print (line)
file.close()

for line in file.readlines():

    if not(line.startswith("Coding")):

        print(line)


file.close()