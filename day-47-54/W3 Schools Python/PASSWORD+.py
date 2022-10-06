# This is a sample Python script.

import re
character_name = input("What\'s your Username? ")
password = input("What\'s your Password? ")
character_age = 19


if character_name == "Omenihu" and password == "Folake123":
    print("You\'re Welcome", character_name, ",")
    print("You are", character_age, "years old")
else:
    print("You\'re not the owner of this computer", character_name)
    print("I am sure you are not up to", character_age)

friends = ["Folake", "Frederick", "Tinuke", "Bright"]
age = [22, 43, 19, 24]
test_statement = "Why does I always feel like I am not enough or am I really not the one for you" \

print(re.search("^Why.*enough$", test_statement))
print(re.findall("am", test_statement))
print(re.split("am", test_statement))
test_statement_main = re.sub("I", "Goobs", test_statement)
#replaces I with Goobs

print(test_statement_main)
test_statement_main_two = re.sub("am", "is", test_statement_main)
#replaces is with am

print(test_statement_main_two)
test_statement_main3 = re.sub("Goobs", "he", test_statement_main_two, 1)
#replaces the first Goobs with He

print(re.sub("you", "Nancy", test_statement_main3))
friends.insert(3, "Kelly")
friends.append("Amaka")
friends.extend(age)
print(friends)
print(friends.index("Kelly"))
