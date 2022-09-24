with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("../../Desktop/my_file.txt", "a") as file:
    file.write("\nNew Text")