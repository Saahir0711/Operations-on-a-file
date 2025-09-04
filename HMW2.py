with open("Codingal.txt", "r") as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()

import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

os.rmdir("sample")

outputFile = open("UpadatedFile.txt", "w")

inputFile = open("Repeated.txt", "r")

lines_seen_so_far = set()
print("Elimintating duplicate lines...")

for line in inputFile:

    if line not in lines_seen_so_far:

        outputFile.write(line)

        lines_seen_so_far.add(line)

inputFile.close()
outputFile.close()

with open("Codingal.txt") as fp:
    data1 = fp.read()

with open("sample_doc.txt") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2
print("Merging two files...")
with open ("MergedFile.txt", "w") as fp:
    fp.write(data1)