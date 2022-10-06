
soft = open("Myfirstfile.txt", "a")
soft.write("I\'ve been able to add more content to the code")
soft.write("""
What is this content""")
soft.close()

soft = open("Myfirstfile.txt", "r")
print(soft.read())
soft.close()


