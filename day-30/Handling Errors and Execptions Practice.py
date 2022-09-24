###......Handling Errors and Execptions Practice.....###
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

###......BMI Calculator......####
height =float( input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be up to 3m")

bmi = weight / height ** 2
print(f"Your current Body Mass Index is {bmi}")