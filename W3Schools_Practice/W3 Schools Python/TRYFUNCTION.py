try:
    print(x)
except NameError:
    print("The Variable X is not defined")
else:
    print("Everything is going fine")
finally:
    print("Well I guess we can also try stuff on python.\nNot everything here has to be so serious.")

file = open("Demofile.txt", "at")

price = 49
txt = "I bought this shoe at a price of {} dollars"
txt2 = "I think the price of {} dollars is rather high for just a shoe"
main_txt = txt2.format(price)
print(main_txt)
print(txt.format(price))