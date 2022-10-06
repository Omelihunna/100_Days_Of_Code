with open("file.txt", "r") as data:
    file = [i.strip("\n") for i in data.readlines()]
    print(file)

for