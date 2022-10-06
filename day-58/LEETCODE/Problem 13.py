roman = input("Enter the Roman Numerals: ").upper()
char = {}
char["I"] = 1
char["V"] = 5
char["X"] = 10
char["L"] = 50
char["C"] = 100
char["D"] = 500
char["M"] = 1000


def calculate(roman):
    sum = 0
    i = 0
    for j in roman:
        while i < (len(roman) - 1):
            if char[roman[i]] < char[roman[i + 1]]:
                sum -= char[roman[i]]
            elif char[roman[i]] >= char[roman[i + 1]]:
                sum += char[roman[i]]
            i += 1
    return sum + char[roman[len(roman) - 1]]

print(calculate(roman))
