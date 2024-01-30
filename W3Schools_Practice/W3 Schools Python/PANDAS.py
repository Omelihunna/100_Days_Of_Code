import pandas as pd

mydata = {
    'phones' : ["Oppo", "Apple", "Samsung"],
    'Modelnumber' : [11, 10, 13]
}
walkdata = {
    'Steps' : [2763, 9597, 6355, 1352],
    'Hours' : [3, 9, 6, 2]
}
a = [1, 2, 3, 4, 5]
steps = {"Monday": 4324, "Tuesday": 5436, "Wednesday": 9749, "Thursday": 4235}

myvar = pd.DataFrame(mydata)
amain = pd.Series(a, index=["a", "b", "c", "d", "e"])
stepvar = pd.Series(steps)
specificstepvar = pd.Series(steps, index=["Monday", "Tuesday"])
walkdatavar = pd.DataFrame(walkdata, index=["day1", "day2", "day3", "day4"])
pd.options.display.max_rows = 200
df = pd.read_csv('/Users/User/Downloads/data.csv')


print("Using my C index to print:", amain["c"])
print(myvar)
print(stepvar)
print(specificstepvar)
print(walkdatavar)
print(walkdatavar.loc[["day1", "day2"]])
print(df.to_string())
print(pd.__version__)
print(pd.options.display.max_rows)