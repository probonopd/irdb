from os import walk, path, getcwd
from re import sub

currentPath = getcwd()

output = open("index", mode="w")
outputInCodes = open("codes/index", mode="w")

prefix = ""

for root, dirs, files in walk(currentPath):
    for file in files:
        if file.endswith("csv"):
            relPath = path.relpath(path.join(root, file), getcwd())
            relPath = sub(r'\\', '/', relPath) #turn backward slashes into forwar dones
            output.write(relPath + "\n")
            outputInCodes.write(relPath[6:] + "\n") #wacky solution to wacky code but removes first 6 characters
output.close()
outputInCodes.close()